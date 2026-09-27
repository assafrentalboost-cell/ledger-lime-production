#!/usr/bin/env bash
# One-time environment setup (free / open-source only). Ubuntu/Debian.
set -euo pipefail
sudo_=""; [ "$(id -u)" -ne 0 ] && sudo_="sudo"
$sudo_ apt-get update -qq || true
# ffmpeg/ffprobe: render + QA. tesseract: OCR readback + text locating.
# libreoffice-calc + poppler-utils: recalculate workbooks and capture sheets as PNG.
DEBIAN_FRONTEND=noninteractive $sudo_ apt-get install -y -qq --no-install-recommends \
  ffmpeg tesseract-ocr tesseract-ocr-eng libreoffice-calc poppler-utils
pip3 install -q -r "$(dirname "$0")/../requirements.txt"
ffmpeg -version | head -1; tesseract --version | head -1; soffice --version
