# Ledger & Lime - Production

- `video-engine/`: Automated Etsy Video Engine V1 (config-driven, Python + FFmpeg). See [video-engine/README.md](video-engine/README.md).
- [LEDGER-LIME-AUTOMATED-ETSY-VIDEO-ENGINE-V1.md](LEDGER-LIME-AUTOMATED-ETSY-VIDEO-ENGINE-V1.md): design, product-truth rules, QA definitions, P13 V3 status.

Render a product:

```
cd video-engine && bash tools/setup_env.sh   # once
python render_video.py configs/product13_iep_tracker.json
```
