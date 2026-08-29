# NLP Experiments
## Description
This repository is made up of two projects in NLP with python. The first one is a generator for sentences in the Dyck Language (balanced parentheses) using Context Free Grammars. The second project evaluates the accuracy of a POS tagger for the Bengali language.
- ```src``` The source code for the python projects
- ```scripts``` Shell scripts for automating things like downloading training data
## Setup
To run the experiments in this project, you must clone the github repository using: ```git clone https://github.com/ObedH/nlp-experiments``` and ```cd nlp-experiments```.
This project requires Python version 3.11. You can check your python version using ```python --version```. If you do not have Python 3.11, run ```sudo apt update && sudo apt install python3.11 python3.11-venv```.
Create a virtual environment with the command ```python3.11 -m venv nlp```. Then activate the virtual environment with ```source nlp/bin/activate```.
Next, you must install the necessary python packages. You can update pip using ```python -m pip install --upgrade pip```. Then, use the command ```python -m pip install -r requirements.txt``` to install the packages.

## Getting the Training Data
Note: Training data is only required for the Bengali POS Tagging experiment.
You can download the training data automatically using the following command: ```./scripts/download_bengali_pos_tag_data.py```.


## Running Experiments
### Dyck Language CFG
You can run this experiment using the command ```python src/balanced_parentheses.py```.
This will generate all the possible strings of balanced parentheses with a maximum recursion depth of 5, all on separate lines.
### Bengali POS Tagging
Use the command ```python src/bengali_pos_tag.py```.
You will see many lines starting with "Incorrect tag. Bengali word: ___, Predicted: ___, Actual: ___". This is expected behavior. The "Bengali word" field is the word found in the dataset. The "Predicted" field is what the BengaliPOS model thought the part of speech was. The "Actual" field is what the dataset listed as the part of speech for that word.
Finally, you can see the accuracy of the model.
