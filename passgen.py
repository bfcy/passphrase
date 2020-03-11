'''
This program creates passwords using words
instead of random letters and numbers.
'''

import random


complexityLevel = 2


#fhand = open('words/word-list-65635.txt')
fhand = open('words/eff_large_wordlist.txt')
#fhand = open('words/eng_words.txt')

contents = fhand.readlines()

counts = 0
for line in contents:
	counts = counts + 1

print(counts)
rnum=random.random()
print(rnum)
rlinenum = int(rnum*counts)
print(rlinenum)

print(contents[rlinenum].split()[1])