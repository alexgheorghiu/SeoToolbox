"""
Alter a list of keywords by combining each keyword with every altering.txt keyword
"""
import re
import argparse
from list_utils import *

# altering_words = ['iasi', 'online']
INCLUDE_ROOT = 2

def remove_altering_words(str):
    global altering_words
    r = str
    for altering_word in altering_words:
        r = r.replace(altering_word, '')
        r = re.sub("\s+", ' ', r)
    return r



def prime_lines(lines):
    """Clear lines"""
    clear_lines2 = set(map(remove_altering_words, lines))
    return clear_lines2



def generate(clear_lines, altering_words, policy = 0):
    """Generates a list of word by taking all the keywords from clear_lines and combine them with keywords from
    altering_words.
    policy - can be 0 - which does not includes the root of the keyword or 2 - which includes the root
    """
    generated = []
    for line in clear_lines:
        if line not in generated:
            #add initial keyword
            if policy & INCLUDE_ROOT:
                generated.append(line)

            #add altering.txt keywords
            for altering_word in altering_words:
                new_word = line + ' ' + altering_word
                if new_word not in generated:
                    generated.append(new_word)
    return generated


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Alter a list')
    parser.add_argument('--input', default='alter_input.txt')
    parser.add_argument('--altering', default='altering.txt')
    parser.add_argument('--output', default='alter_output.txt')

    args = parser.parse_args()
    file_path = args.input
    lines = read_file(file_path)
    altering_words = read_file(args.altering)

    clear_lines = prime_lines(lines)
    generated_lines = generate(clear_lines, altering_words)

    print("\n".join(generated_lines))

    write_lines(generated_lines, args.output)









