"""
Alter a list of keywords by combining each keyword with every altering keyword
"""
import re

altering_words = ['iasi', 'online']
INCLUDE_ROOT = 2

def remove_altering_words(str):
    global altering_words
    r = str
    for altering_word in altering_words:
        r = r.replace(altering_word, '')
        r = re.sub("\s+", ' ', r)
    return r

f = open('list1.txt', 'r')
lines = f.readlines();
f.close()

# lines = ['psiholog iasi', 'psihoterapeut', 'terapie online']

clear_lines = set(map(lambda l: l.strip(), lines))
clear_lines2 = set(map(remove_altering_words, clear_lines))

# for line in clear_lines2:
#     print(line)
# policy = 0 | INCLUDE_ROOT
policy = 0

generated = []
for line in clear_lines2:
    if line not in generated:
        #add initial keyword
        if policy & INCLUDE_ROOT:
            generated.append(line)

        #add altering keywords
        for altering_word in altering_words:
            new_word = line + ' ' + altering_word
            if new_word not in generated:
                generated.append(new_word)

print("\n".join(generated))








