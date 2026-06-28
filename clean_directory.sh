#!/bin/bash
# 清理目录无用文件脚本 / Directory cleanup script

echo "Cleaning useless files..."

# Find and remove .tmp files
find . -type f -name "*.tmp" -exec rm -f {} +
echo "Removed .tmp files."

# Find and remove __pycache__ directories
find . -type d -name "__pycache__" -exec rm -rf {} +
echo "Removed __pycache__ directories."

# Find and remove .DS_Store files (macOS specific, often useless in repos)
find . -type f -name ".DS_Store" -exec rm -f {} +
echo "Removed .DS_Store files."

# Find and remove empty files in RESEARCH/daily/ (except .gitkeep if any)
# Note: Doing this cautiously to avoid deleting anything important, but empty files are generally useless here.
# But we won't delete empty files by default without knowing if they are intentional.
# We'll stick to known temp files.

echo "Cleanup complete."
