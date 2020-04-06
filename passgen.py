'''
File Name    : 	passgen.py
Author       : 	BFCY
Description  : 	This program creates passwords using words
             : 	instead of random letters, numbers and special 
				characters
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

# Returns a random line number for wordlist 
# I/P: number of words in the wordlist file
# O/P: a random number within that range
def randomNum(maxVal):
	rnum=random.random()
	rlinenum = int(rnum*maxVal)
	return(rlinenum)


# Ask user for input 
# I/P: user entered number
# O/P: returns that number as a string
def getinput():
	print("Pass Phrase Generator")
	numOfWords = input("Number of words: ")

	return numOfWords

# Prints words if user input is valid
# I/P: user entered number and wordlist
# O/P: words from the wordlist
def printWords(numWords, wordList, numOfLines):
	if checkinput(numWords):
		for word in range(int(numWords)):
			rword = randomWord(wordList, numOfLines)
			print(rword)


# Check to see if user entered a valid number
# I/P: user entered number
# O/P: True if i/p is valid, false and msg if invalid
def checkinput(numOfWords):

	try:
		testinput = int(numOfWords)
		if testinput < 0:
			print('positive integers only')
			return False
	except ValueError:
		try:
			testinput = float(numOfWords)
			print("ValueError: Positive integers only")
			return False
		except ValueError:
			print("TypeError: Please enter a nonnegative number")
			return False

	return True


def main():

	#fhand = open('wordlists/word-list-65635.txt')
	fhand = open('wordlists/eff_large_wordlist.txt')
	#fhand = open('wordlists/eng_words.txt')
	
	wordList, numOfLines = parsefile(fhand)
	numWords = getinput()

	printWords(numWords, wordList, numOfLines)



if __name__ == '__main__':
	main()
