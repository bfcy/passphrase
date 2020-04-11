from tkinter import *
import random

class MyWindow:
	def __init__(self, win, wordList, numOfLines):
		self.lbl1=Label(win, text='Number of Words')
		self.lbl2=Label(win, text='Answer')
		self.t1=Entry(justify=RIGHT)
		self.t3=Text(win, height=15, width=30, wrap=WORD)
		self.b1=Button(win, text='Submit', command=self.process)
		self.t1.bind('<Return>', self.process)


		self.lbl1.place(x=20, y=30)				
		self.lbl2.place(x=20, y=110)
		self.t1.place(x=150, y=30)				
		self.b1.place(x=230, y=55)

		self.t3.place(x=80, y=110)        

		self.wordList = wordList
		self.numOfLines = numOfLines


	def checkinput(self,numOfWords):

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


	def randomNum(self, maxVal):
		rnum=random.random()
		rlinenum = int(rnum*maxVal)
		return(rlinenum)
		

	def randomWord(self,wordList, numOfLines):
		randomline = self.randomNum(numOfLines)

		return(wordList[randomline])


	def printWords(self, numWords, wordList, numOfLines):
		rwords = []
		for word in range(int(numWords)):
			datum = self.randomWord(wordList, numOfLines)
			rwords.append(str(datum).strip())

		return rwords
		

	def process(self, *args):
		numWords = self.t1.get()	# get user input
		
		self.t3.delete('1.0', END)	# clear output window
			
		# Check if input is valid
		if not self.checkinput(numWords)[0]:
			errmsg = self.checkinput(numWords)[1]
			self.t3.insert(1.0, errmsg)		
		else:
			rwords = self.printWords(numWords, self.wordList, self.numOfLines)
			rwords_str = ' '.join(rwords)
			self.t3.insert(1.0, rwords_str)
			

##############################################################
def parsefile(filehandle):
	linecount = 0
	lines = filehandle.readlines()
	linecount = len(lines)

	return lines, linecount

def openWordList():
	#fhand = open('wordlists/word-list-65635.txt')
	fh = open('wordlists/eff_large_wordlist_wordsonly.txt')
	
	return fh

def main():
	fhand = openWordList()
	wordList, numOfLines = parsefile(fhand)

	window=Tk()
	window.title('Passphrase Generator')
	window.geometry("350x400+10+10")

	mywin=MyWindow(window, wordList, numOfLines)

	window.mainloop()


if __name__ == '__main__':
    main()


