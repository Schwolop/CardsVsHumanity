import random
import math
import sys
import string

numRows = 5
numColumns = 4
numRowsOnLastPage = 3
numColumnsInLastRow = 2
firstBlackPage = 25
lastBlackPage = 29
aNumberGreaterThanTheTotalNumberOfCards = 100
choicesSoFar = []

def Choose():
	count = 0
	while count < aNumberGreaterThanTheTotalNumberOfCards:
		page = random.randrange(firstBlackPage,lastBlackPage+1)
		row = random.randrange(1,
			numRowsOnLastPage+1 
			if (page==lastBlackPage) 
			else numRows+1)
		col = random.randrange(1,
			numColumnsInLastRow+1 
			if (page==lastBlackPage and row==numRowsOnLastPage) 
			else numColumns+1)
		choice = page * 10000 + row * 100 + col
		if choice not in choicesSoFar:
			choicesSoFar.append(choice)
			return page,row,col
		count += 1
	print("Everything has been chosen (or it just took too damn long!)")
	return None, None, None
	
if __name__ == '__main__':
	c = ''
	while c.lower() != 'x':
		page,row,col = Choose()
		if page is not None:
			print "Page: " + str(page) + ", Row: " + str(row) + ", Column: " + str(col)
		c = sys.stdin.readline()
