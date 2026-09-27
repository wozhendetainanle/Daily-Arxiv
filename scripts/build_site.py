#!/usr/bin/env python3
"""Build the static paper-card catalog from the archived Markdown reports."""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
DAILY = ROOT / "daily"
OUTPUT = ROOT / "data" / "papers.json"
ENRICHMENT = ROOT / "data" / "enrichment.json"
ARXIV = re.compile(r"https://arxiv\.org/abs/(\d{4}\.\d{4,5})(?:v\d+)?")
MARKDOWN_LINK = re.compile(r"\[([^]]+)\]\([^)]+\)")


def parse_row(line: str) -> dict | None:
    if not line.startswith("|"):
        return None
    cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
    if len(cells) < 8 or not cells[0].isdigit():
        return None
    link_cell = next((index for index in (1, 2) if ARXIV.search(cells[index])), None)
    if link_cell is None:
        return None
    match = ARXIV.search(cells[link_cell])
    offset = 0 if link_cell == 1 else 1
    if len(cells) < 8 + offset:
        return None
    title = MARKDOWN_LINK.sub(lambda item: item.group(1), cells[1]).split(" / PDF")[0].strip()
    if not title:
        return None
    score_match = re.search(r"\d+(?:\.\d+)?", cells[5 + offset])
    relevance = float(score_match.group()) if score_match else None
    if relevance is not None and relevance > 10:
        relevance /= 10
    return {
        "rank": int(cells[0]), "id": match.group(1), "title": title,
        "authors": cells[3 + offset], "category": cells[2 + offset],
        "affiliation": cells[4 + offset], "relevance": relevance,
        "priority": cells[7 + offset],
    }


def topic(title: str) -> str:
    value = title.lower()
    if any(word in value for word in ("contact", "force", "tactile", "haptic", "physics", "physical", "dynamic", "deform", "simulation", "sim-to-real", "torque")):
        return "3D × Physics"
    if any(word in value for word in ("robot", "manipulation", "grasp", "dexterous", "locomotion", "vla")):
        return "3D × Robotics"
    if any(word in value for word in ("3d", "4d", "scene", "reconstruction", "geometry", "gaussian", "splat", "point cloud", "mesh")):
        return "3D Vision"
    return "Research"


def safe_url(value: object) -> str | None:
    if not isinstance(value, str):
        return None
    parsed = urlparse(value)
    if parsed.scheme == "https" and parsed.netloc:
        return value
    return None


def safe_image(value: object) -> str | None:
    if not isinstance(value, str) or not value.startswith("assets/papers/"):
        return None
    path = ROOT / value
    if path.is_file() and path.resolve().is_relative_to((ROOT / "assets" / "papers").resolve()):
        return value
    return None


def main() -> None:
    enrichment = json.loads(ENRICHMENT.read_text()) if ENRICHMENT.exists() else {}
    dates = []
    for report in sorted(DAILY.glob("*/*.md"), reverse=True):
        date = report.stem
        papers = []
        seen_ids = set()
        for line in report.read_text(encoding="utf-8").splitlines():
            row = parse_row(line)
            if not row or row["id"] in seen_ids:
                continue
            seen_ids.add(row["id"])
            arxiv_id = row["id"]
            title = row["title"]
            paper_url = f"https://arxiv.org/abs/{arxiv_id}"
            extra = enrichment.get(arxiv_id, {})
            links = {"Paper": paper_url}
            for label in ("Code", "Project", "Video", "Data"):
                url = safe_url(extra.get(label.lower()))
                if url:
                    links[label] = url
            papers.append({
                **row,
                "topic": topic(title),
                "venue": extra.get("venue") if isinstance(extra.get("venue"), str) else None,
                "image": safe_image(extra.get("image")),
                "imageSource": safe_url(extra.get("image_source")),
                "links": links,
            })
        dates.append({"date": date, "report": report.relative_to(ROOT).as_posix(), "papers": papers})
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps({"dates": dates}, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    print(f"Built {len(dates)} dates and {sum(len(item['papers']) for item in dates)} cards: {OUTPUT}")


if __name__ == "__main__":
    main()
