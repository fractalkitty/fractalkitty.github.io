#!/bin/bash
source myenv/bin/activate
pip install numbers_parser
python3 updateHtml.py
git add .
git commit -m "Auto-update from Numbers - $(date)"
git push origin main
echo "Rebuild complete at $(date)" >> /tmp/rebuild.log