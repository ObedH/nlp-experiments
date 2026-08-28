#!/bin/bash
DATA_URL="https://raw.githubusercontent.com/bnlp-resources/pos/main/train_data_IITKGP.tsv"
OUTPUT="data/bengali_pos_tag/train_data_IITKGP.tsv"

mkdir -p "$(dirname "$OUTPUT")"

curl -L --fail --show-error --output "$OUTPUT" "$URL"

echo "Successfully downloaded POS tagged Bengali data to $OUTPUT"
