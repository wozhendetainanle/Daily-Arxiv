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
ROW = re.compile(r"^\|\s*(\d+)\s*\|\s*(.*?)\s*\|\s*\[arXiv:([\d.]+)\]\((https://arxiv\.org/abs/[\d.]+)\)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*([\d.]+)\s*\|\s*([\d.]+)\s*\|\s*(.*?)\s*\|\s*$")


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
        for line in report.read_text(encoding="utf-8").splitlines():
            match = ROW.match(line)
            if not match:
                continue
            rank, title, arxiv_id, paper_url, category, authors, affiliation, relevance, institution, priority = match.groups()
            extra = enrichment.get(arxiv_id, {})
            links = {"Paper": paper_url}
            for label in ("Code", "Project", "Video", "Data"):
                url = safe_url(extra.get(label.lower()))
                if url:
                    links[label] = url
            papers.append({
                "rank": int(rank),
                "id": arxiv_id,
                "title": title,
                "authors": authors,
                "category": category,
                "affiliation": affiliation,
                "relevance": float(relevance),
                "priority": priority,
                "topic": topic(title),
                "venue": extra.get("venue") if isinstance(extra.get("venue"), str) else None,
                "image": safe_image(extra.get("image")),
                "imageSource": safe_url(extra.get("image_source")),
                "links": links,
            })
        if papers:
            dates.append({"date": date, "report": report.relative_to(ROOT).as_posix(), "papers": papers})
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps({"dates": dates}, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    print(f"Built {len(dates)} dates and {sum(len(item['papers']) for item in dates)} cards: {OUTPUT}")


if __name__ == "__main__":
    main()
