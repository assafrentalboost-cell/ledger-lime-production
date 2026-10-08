#!/bin/sh
# Entrant-first discovery V2 — regenerates every number in ENTRANT-FIRST-V2-DISCOVERY-2026-10-08.md.
# EVERBEE ESTIMATE — NOT ETSY TRANSACTION DATA. Inputs are the frozen pulls in raw/ (Q-/V1-Q- entrant, F- young-listing, X- exploratory, K- keyword).
set -e
cd "$(dirname "$0")"
python3 entrants.py                          # dedupe + CLEAN/NEAR/REJECT + health      -> all_listings_classified.json
python3 buyers.py > buyers_output.txt        # Stage 2 exact-buyer grouping              -> buyers.json
python3 jobs.py > jobs_output.txt            # Stages 3-5,7-10,15 five-job test + gates  -> jobs.json
python3 keyword_map.py > keyword_map_output.txt   # Stage 13 keyword doors              -> keyword_map.json
python3 tables.py                            # Stage 16 CSV tables
