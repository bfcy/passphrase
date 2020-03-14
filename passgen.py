'''
File Name    : passgen.py
Author       : BFCY
Description  : This program creates passwords using words
             : instead of random letters and numbers.
'''

import random

# I/P: filehandle to a wordlist text file
# O/P: returns a list of words and random word from the list
def parsefile(filehandle):
	linecount = 0
	lines = filehandle.readlines()
	linecount = len(lines)

	return lines, linecount

# I/P: wordList and numOfLines
def randomWord(wordList, numOfLines):
	randomline = randomNum(numOfLines)

	wordsPerLine = len(wordList[randomline].split())

	if (wordsPerLine == 2):
		return(wordList[randomline].split()[1])
	elif (wordsPerLine == 1): 	
		return(wordList[randomline])


# I/P: maximum int
# O/P: a random number within that range
def randomNum(maxVal):
	rnum=random.random()
	rlinenum = int(rnum*maxVal)
	return(rlinenum)



def main():

	#fhand = open('words/word-list-65635.txt')
	fhand = open('words/eff_large_wordlist.txt')
	#fhand = open('words/eng_words.txt')
	passphrasewords = int(input("Number of words in pass phrase: "))

	wordList, numOfLines = parsefile(fhand)

	for passphraseword in range(passphrasewords):
		rword = randomWord(wordList, numOfLines)
		print(rword)


if __name__ == '__main__':
	main()