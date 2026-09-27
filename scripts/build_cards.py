#!/usr/bin/env python3
"""Embed GitHub-rendered paper cards into every archived Markdown report."""

from __future__ import annotations

import html
import json
import os
import re
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
DAILY = ROOT / "daily"
ENRICHMENT = ROOT / "data" / "enrichment.json"
START = "<!-- PAPER_CARDS_START -->"
END = "<!-- PAPER_CARDS_END -->"
ARXIV = re.compile(r"https://arxiv\.org/abs/(\d{4}\.\d{4,5})(?:v\d+)?")
MARKDOWN_LINK = re.compile(r"\[([^]]+)\]\([^)]+\)")
CATEGORY_CODE = re.compile(r"\b(?:cs|stat|eess|math|physics|cond-mat)\.[A-Za-z.-]+\b")


def parse_row(line: str) -> dict | None:
    if not line.startswith("|"):
        return None
    cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
    if len(cells) < 8 or not cells[0].isdigit():
        return None
    link_cell = next((i for i in (1, 2) if ARXIV.search(cells[i])), None)
    if link_cell is None:
        return None
    match = ARXIV.search(cells[link_cell])
    offset = 0 if link_cell == 1 else 1
    if len(cells) < 8 + offset:
        return None
    title = MARKDOWN_LINK.sub(lambda item: item.group(1), cells[1]).split(" / PDF")[0].strip()
    if not title:
        return None
    return {
        "rank": int(cells[0]),
        "id": match.group(1),
        "title": title,
        "category": cells[2 + offset],
        "authors": cells[3 + offset],
    }


def safe_url(value: object) -> str | None:
    if not isinstance(value, str):
        return None
    parsed = urlparse(value)
    return value if parsed.scheme == "https" and parsed.netloc else None


def inline(value: str) -> str:
    return html.escape(value, quote=False).replace("|", "&#124;").replace("\n", " ")


def image_for(report: Path, paper: dict, extra: dict) -> tuple[str, str]:
    value = extra.get("image")
    image = ROOT / "assets" / "card-placeholder.svg"
    alt = "论文配图待补"
    if isinstance(value, str) and value.startswith("assets/papers/"):
        candidate = ROOT / value
        if candidate.is_file() and candidate.resolve().is_relative_to((ROOT / "assets" / "papers").resolve()):
            image = candidate
            alt = "论文或项目配图"
    return os.path.relpath(image, report.parent).replace(os.sep, "/"), alt


def card(report: Path, paper: dict, enrichment: dict) -> str:
    extra = enrichment.get(paper["id"], {})
    image, alt = image_for(report, paper, extra)
    paper_url = f"https://arxiv.org/abs/{paper['id']}"
    code = CATEGORY_CODE.search(paper["category"])
    category = code.group() if code else paper["category"].split(";")[0][:24]
    venue = extra.get("venue") if isinstance(extra.get("venue"), str) else None
    label = venue or f"arXiv {report.stem} · {category}"
    authors = paper["authors"]
    if len(authors) > 125:
        authors = authors[:122].rstrip(" ，,;") + "…"
    links = [f"[Paper]({paper_url})"]
    for name in ("Code", "Project", "Video", "Data"):
        url = safe_url(extra.get(name.lower()))
        if url:
            links.append(f"[{name}]({url})")
    image_source = safe_url(extra.get("image_source"))
    if image_source and alt != "论文配图待补":
        links.append(f"[图源]({image_source})")
    return (
        f"![{inline(alt)}]({image})<br>"
        f"<sub>{inline(label)} · #{paper['rank']}</sub><br>"
        f"**[{inline(paper['title'])}]({paper_url})**<br>"
        f"<sub>{inline(authors)}</sub><br>"
        + " · ".join(links)
    )


def cards_section(report: Path, papers: list[dict], enrichment: dict) -> str:
    rows = []
    for start in range(0, len(papers), 3):
        cells = [card(report, paper, enrichment) for paper in papers[start:start + 3]]
        rows.append("| " + " | ".join(cells + [" "] * (3 - len(cells))) + " |")
    return (
        f"{START}\n## 论文卡片\n\n"
        "按原日报排名展示；点击标题或 Paper 查看原文，详细中文分析见下方。\n\n"
        "| 论文 | 论文 | 论文 |\n|---|---|---|\n"
        + "\n".join(rows) + f"\n{END}"
    )


def main() -> None:
    enrichment = json.loads(ENRICHMENT.read_text(encoding="utf-8")) if ENRICHMENT.exists() else {}
    reports = 0
    cards = 0
    for report in sorted(DAILY.glob("*/*.md")):
        source = report.read_text(encoding="utf-8")
        body = source
        if START in body:
            body = re.sub(rf"{re.escape(START)}.*?{re.escape(END)}\n*", "", body, count=1, flags=re.S)
        papers = []
        seen = set()
        for line in body.splitlines():
            paper = parse_row(line)
            if paper and paper["id"] not in seen:
                papers.append(paper)
                seen.add(paper["id"])
        if not papers:
            if source != body:
                report.write_text(body, encoding="utf-8")
            continue
        lines = body.splitlines(keepends=True)
        first_heading = next((i for i, line in enumerate(lines) if line.startswith("# ")), None)
        position = first_heading + 1 if first_heading is not None else 0
        insertion = "\n" + cards_section(report, papers, enrichment) + "\n\n"
        output = "".join(lines[:position]) + insertion + "".join(lines[position:]).lstrip("\n")
        if output != source:
            report.write_text(output, encoding="utf-8")
        reports += 1
        cards += len(papers)
    print(f"Embedded {cards} cards in {reports} Markdown reports")


if __name__ == "__main__":
    main()
