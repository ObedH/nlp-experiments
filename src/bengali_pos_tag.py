from bnlp import BengaliPOS

# Compares BengaliPOS from bnlp's ability to POS tag sentences with a manually tagged dataset
pos = BengaliPOS()

text = "আমি বাংলায় কথা বলি।"

tags = pos.tag(text)

for word, tag in tags:
    print(f"{word}\t{tag}")

