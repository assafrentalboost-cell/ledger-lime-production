#!/bin/sh
# Rebuild COMPETITORS.csv from raw/ EverBee pulls. EVERBEE ESTIMATE — NOT ETSY TRANSACTION DATA.
cd "$(dirname "$0")" && python3 -I competitors.py
