from bnlp import BengaliPOS

# Evaluates BengaliPOS's ability to POS tag
pos = BengaliPOS()

max_sentences = 10

correct = 0
total = 0
incorrect = []

sentences = []

with open("data/bengali_pos_tag/train_data_IITKGP.tsv", "r", encoding="utf-8") as file:
    sentence = []
    for line in file:
        stripped_line = line.strip()
        if len(stripped_line) == 0:
            # line is empty
            sentences.append(sentence)
            sentence = []
            continue
        row = stripped_line.split('\t')
        if len(row) < 2:
            continue
        bengali_word = row[0]
        part_of_speech = row[1]

        sentence.append((bengali_word, part_of_speech))

for sentence in sentences[:max_sentences]:
    bengali_words = ' '.join([pair[0] for pair in sentence])

    tags = pos.tag(bengali_words)
    for (bengali_word, pos_tag), (_, dataset_tag) in zip(tags, sentence):

        if pos_tag == dataset_tag:
            correct += 1
        else:
            incorrect.append((bengali_word, dataset_tag, pos_tag))
        
        total += 1


for example in incorrect:
    bengali_word, dataset_tag, pos_tag = example
    print(f"Mismatch: Bengali word: {bengali_word}, Dataset: {dataset_tag}, Tagger: {pos_tag}")
print(f"Accuracy: {(correct * 100 / total):.2f}")
