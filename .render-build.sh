#!/usr/bin/env bash
# Exit on error
set -o errexit

echo "1. Cài đặt Python Dependencies..."
pip install -r requirements.txt

echo "2. Cài đặt cơ sở dữ liệu và công cụ..."
# Cài đặt Node modules cho tool Discord-Auto-Quest
if [ -d "Discord-Auto-Quests-Discord-Tool" ]; then
    echo "Phát hiện tool Discord-Auto-Quests, đang cài đặt node_modules..."
    cd Discord-Auto-Quests-Discord-Tool
    npm install
    cd ..
fi

echo "Build hoàn tất!"
