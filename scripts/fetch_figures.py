#!/usr/bin/env python3
"""Save source-linked arXiv figures for one daily Markdown card grid."""

from __future__ import annotations

import argparse
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from html.parser import HTMLParser
from io import BytesIO
from pathlib import Path
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

from PIL import Image, ImageOps

from build_cards import ENRICHMENT, ROOT, parse_row


class FigureImages(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.sources: list[str] = []

    def handle_starttag(self, tag: str, attributes: list[tuple[str, str | None]]) -> None:
        if tag != "img":
            return
        attrs = dict(attributes)
        if "ltx_graphics" not in (attrs.get("class") or ""):
            return
        try:
            width = int(attrs.get("width") or "0")
            height = int(attrs.get("height") or "0")
        except ValueError:
            return
        if width >= 220 and height >= 100 and attrs.get("src"):
            self.sources.append(attrs["src"])


def read_url(url: str, maximum: int = 12_000_000) -> bytes:
    request = Request(url, headers={"User-Agent": "Daily-Arxiv-card-figures/1.0"})
    with urlopen(request, timeout=15) as response:
        if urlparse(response.url).hostname != "arxiv.org":
            raise ValueError("Unexpected image host")
        data = response.read(maximum + 1)
    if len(data) > maximum:
        raise ValueError("Figure exceeds size limit")
    return data


def image_from_html(arxiv_id: str) -> tuple[Image.Image, str]:
    page_url = f"https://arxiv.org/html/{arxiv_id}"
    parser = FigureImages()
    parser.feed(read_url(page_url, maximum=4_000_000).decode("utf-8", errors="replace"))
    for source in parser.sources[:8]:
        figure_url = urljoin(page_url, source)
        if urlparse(figure_url).hostname != "arxiv.org":
            continue
        try:
            image = Image.open(BytesIO(read_url(figure_url)))
            image.load()
            if min(image.size) >= 100:
                return image, figure_url
        except (OSError, ValueError):
            continue
    raise ValueError("No usable figure in arXiv HTML")


def image_from_pdf(arxiv_id: str, pdf_dir: Path) -> tuple[Image.Image, str]:
    from pypdf import PdfReader

    pdf = pdf_dir / f"{arxiv_id}.pdf"
    if not pdf.is_file():
        pdf.parent.mkdir(parents=True, exist_ok=True)
        pdf.write_bytes(read_url(f"https://arxiv.org/pdf/{arxiv_id}", maximum=40_000_000))
    reader = PdfReader(pdf)
    candidates = []
    for page_number, page in enumerate(reader.pages[:5]):
        for extracted in page.images:
            try:
                image = Image.open(BytesIO(extracted.data))
                image.load()
                width, height = image.size
                if width < 320 or height < 180:
                    continue
                aspect = width / height
                if not 0.45 <= aspect <= 5:
                    continue
                # Favor prominent figures and earlier pages over small icons.
                score = min(width * height, 3_000_000) / (1 + page_number * 0.4)
                candidates.append((score, image))
            except (OSError, ValueError):
                continue
    if not candidates:
        raise ValueError("No usable raster figure in PDF")
    return max(candidates, key=lambda item: item[0])[1], f"https://arxiv.org/pdf/{arxiv_id}"


def save_card_image(image: Image.Image, target: Path) -> None:
    image = ImageOps.exif_transpose(image)
    image.thumbnail((900, 430), Image.Resampling.LANCZOS)
    if image.mode == "RGBA":
        background = Image.new("RGBA", image.size, "white")
        background.alpha_composite(image)
        image = background.convert("RGB")
    else:
        image = image.convert("RGB")
    canvas = Image.new("RGB", (900, 430), "#f7f8fa")
    canvas.paste(image, ((900 - image.width) // 2, (430 - image.height) // 2))
    target.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(target, "WEBP", quality=85, method=6)


def fetch_one(arxiv_id: str, date: str, pdf_dir: Path) -> tuple[str, dict | None, str]:
    target = ROOT / "assets" / "papers" / date / f"{arxiv_id}.webp"
    try:
        image, source = image_from_html(arxiv_id)
        method = "HTML"
    except Exception as html_error:
        try:
            image, source = image_from_pdf(arxiv_id, pdf_dir)
            method = "PDF"
        except Exception as pdf_error:
            return arxiv_id, None, f"HTML: {html_error}; PDF: {pdf_error}"
    save_card_image(image, target)
    return arxiv_id, {"image": target.relative_to(ROOT).as_posix(), "image_source": source}, method


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True, help="Report date, for example 2026-09-26")
    parser.add_argument("--pdf-dir", type=Path, default=Path("/private/tmp/daily-arxiv-figures-pdf"))
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()
    report = ROOT / "daily" / args.date[:4] / f"{args.date}.md"
    papers = [parse_row(line) for line in report.read_text().splitlines()]
    ids = list(dict.fromkeys(paper["id"] for paper in papers if paper))
    if args.limit:
        ids = ids[:args.limit]
    enrichment = json.loads(ENRICHMENT.read_text())
    todo = [arxiv_id for arxiv_id in ids if not (
        enrichment.get(arxiv_id, {}).get("image")
        and (ROOT / enrichment[arxiv_id]["image"]).is_file()
    )]
    with ThreadPoolExecutor(max_workers=5) as pool:
        futures = {pool.submit(fetch_one, arxiv_id, args.date, args.pdf_dir): arxiv_id for arxiv_id in todo}
        for future in as_completed(futures):
            arxiv_id, result, message = future.result()
            if result:
                enrichment.setdefault(arxiv_id, {}).update(result)
                print(f"{arxiv_id}: {message}", flush=True)
            else:
                print(f"{arxiv_id}: MISSING {message}", flush=True)
    ENRICHMENT.write_text(json.dumps(enrichment, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Saved {sum(arxiv_id in enrichment and 'image' in enrichment[arxiv_id] for arxiv_id in ids)}/{len(ids)} figures")


if __name__ == "__main__":
    main()
