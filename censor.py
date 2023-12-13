from typing import List
from pathlib import Path

#read a txt file and censor the words in the file that are given by the user
def save_censored(input_file_path: str, output_file_path: str, censored_words: List[str], replace_word_with_asterisks: bool = True):
    #convert the input and output file paths to Path objects
    input_file_path = Path(input_file_path)
    output_file_path = Path(output_file_path)
    #check if input file exists
    if not input_file_path.exists():
        raise FileNotFoundError(f'Input file {input_file_path} does not exist')
    #check if output file exists
    if output_file_path.exists():
        raise FileExistsError(f'Output file {output_file_path} already exists')
    
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        for line in input_file:
            for word in censored_words:
                if replace_word_with_asterisks:
                    # replace the word with asterisks
                    line = line.replace(word, '*' * len(word))
                else:
                    # replace the word by '-censored-'
                    line = line.replace(word, '<cnsrd>')
            output_file.write(line)

# Usage example
input_file_path = 'input.txt'  # Replace with your input file path
output_file_path = 'output.txt'  # Replace with the desired output file path
censored_words = ['word1', 'word2', 'word3']  # Replace with your censored words

save_censored(input_file_path, output_file_path, censored_words, replace_word_with_asterisks=False)
