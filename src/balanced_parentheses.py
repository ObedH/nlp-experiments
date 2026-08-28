from nltk import CFG
from nltk.parse.generate import generate

grammar = CFG.fromstring("""
    S -> '(' S ')' S | ''
""")

def gen_balanced_parentheses(max_depth):
    sentences = list(generate(grammar, depth=max_depth))
    for sentence in sentences:
        print(''.join(sentence))

print("Generating all possible sentences composed of balanced parentheses with a maximum recursion depth of 5:")
gen_balanced_parentheses(5)
