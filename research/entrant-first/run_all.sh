#!/bin/sh
# Reproduce every number in ENTRANT-FIRST-DISCOVERY-2026-10-07.md (EVERBEE ESTIMATE — NOT ETSY TRANSACTION DATA).
# raw/*.json are the frozen EverBee pulls (Q- entrant pulls, F- flood pulls, K- keyword pulls). Rebuilding raw/ needs the session transcript:
#   python3 -I raw/extract_from_transcript.py <transcript.jsonl> 2026-10-07T09:00
set -e
cd "$(dirname "$0")"
python3 entrants.py                          # classify + dedupe -> all_listings_classified.json
python3 grouping.py > grouping_output.txt    # buyer/job clusters + ADHD overlay -> clusters.json, overlay_adhd.json
python3 clone_check.py > clone_check_output.txt   # clone/flood -> clone_check.json
python3 entrant_table.py                     # -> ENTRANT-TABLE.md
python3 summary.py > summary_output.txt      # gates, depth, provisional -> adhd_depth.json
python3 keyword_map.py > keyword_map_output.txt   # -> keyword_map.json
