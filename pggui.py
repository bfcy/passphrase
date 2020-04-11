from tkinter import *
import passgen

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


# O/P: returns a list of random words
	def getWords(self, numWords, wordList, numOfLines):
		rwords = []
		
		for word in range(int(numWords)):
			datum = passgen.randomWord(wordList, numOfLines)
			rwords.append(str(datum).strip())

		return rwords
		

	def process(self, *args):
		numWords = self.t1.get()	# get user input
		
		self.t3.delete('1.0', END)	# clear output window
			
		# Check if input is valid
		status = passgen.checkinput(numWords)
		if not status[0]:
			errmsg = status[1]
			self.t3.insert(1.0, errmsg)		
		else:
			rwords = self.getWords(numWords, self.wordList, self.numOfLines)
			rwords_str = ' '.join(rwords)
			self.t3.insert(1.0, rwords_str)
			

##############################################################
def main():
	fhand = passgen.openWordList()
	wordList, numOfLines = passgen.parsefile(fhand)

	window=Tk()
	window.title('Passphrase Generator')
	window.geometry("350x400+10+10")

	mywin=MyWindow(window, wordList, numOfLines)

	window.mainloop()


if __name__ == '__main__':
    main()