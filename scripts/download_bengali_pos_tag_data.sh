#!/bin/bash
set -euo pipefail
DATA="https://raw.githubusercontent.com/banglanlp/bnlp-resources/refs/heads/main/pos/pos_tag_data_bangla_tagged_corpus.tsv"
OUTPUT="data/bengali_pos_tag/train_data_IITKGP.tsv"

mkdir -p "$(dirname "$OUTPUT")"

curl -L --fail --show-error --output "$OUTPUT" "$DATA"

echo "Successfully downloaded POS tagged Bengali data to $OUTPUT"
