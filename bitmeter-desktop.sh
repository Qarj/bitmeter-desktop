#!/bin/sh
# Initialize conda for the current shell session
. ~/miniconda3/etc/profile.d/conda.sh
conda activate bitmeter
cd /usr/local/bin/bitmeter-desktop
python main.py