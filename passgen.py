'''
File Name    : 	passgen.py
Author       : 	BFCY
Description  : 	This program creates passwords using words
             : 	instead of random letters, numbers and special 
				characters
'''
import random


# I/P: filehandle to a wordlist text file
# O/P: returns a list of words and number of words in the list
def parsefile(filehandle):
	linecount = 0
	lines = filehandle.readlines()
	linecount = len(lines)

	return lines, linecount


# I/P: wordList and numOfLines
# O/P: one random word from wordlist
def randomWord(wordList, numOfLines):
	randomline = randomNum(numOfLines)

	return(wordList[randomline])

# Returns a random line number from wordlist 
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


# Check to see if user entered a valid number
# I/P: user entered number
# O/P: True if i/p is valid, false and msg if invalid
def checkinput(numOfWords):
	try:
		testinput = int(numOfWords)
		if testinput < 0:
			msg = 'positive integers only'
			return [False, msg]
	except ValueError:
		try:
			testinput = float(numOfWords)
			msg = 'ValueError: Positive integers only'
			return [False, msg]
		except ValueError:
			msg = 'TypeError: Please enter a nonnegative number'
			return [False, msg]

	return [True, '']


def openWordList():
	#fhand = open('wordlists/word-list-65635.txt')
	fh = open('wordlists/eff_large_wordlist_wordsonly.txt')
	#fhand = open('wordlists/eng_words.txt')
	return fh

def main():

	fhand = openWordList()
	wordList, numOfLines = parsefile(fhand)
	numWords = getinput()

	# If checkinput returns false, print error msg
	if not checkinput(numWords)[0]:
		print(checkinput(numWords)[1])
	else:
		for word in range(int(numWords)):
			rword = randomWord(wordList, numOfLines).rstrip()
			print(rword)



if __name__ == '__main__':
	main()
