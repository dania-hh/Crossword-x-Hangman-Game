import os
import random

numRows = 15
numCols = 15
hiddenBoard=[]
displayBoard=[]
incorrect_guesses=[]
win=False

crosswords = ["  ship die  t bs  y r i  j r et  p ease o u nr loss c just ee  t s u  r h an  h u s  n   tgive r s wall ht  see i  l a  h  i   o  i b de  s king stonen i l     t r b  couple      ttoe n   b  b c    agriculturalkey     y  t p ", \
            "    essay  rank v r e   c     here l o o  m   g g l c n  a pmedia  c t  i o t o d a earn lwarn e s m  t l b   p i p  e u l  hero oven t e g n n r  a im  u d a a intou bike l r  c ns  l n l y  e  i  t t y       city    scene  ", \
            " c  g d forward oppose         m  o back   f  p  d t o  n a  r d    n couchlevel miss n u  h p    u sell general m  t t  n n g  p  h y  s d a stone   wise i  i  l    v n n  o  e m best swing shop     t     s r plant broad  e ", \
            "kiss        u     o mechanism  c r a      e  boat l e h  d   n   e c a p  c s     o b r  u i defensive  r d   a o t c  rpermit m a i  i r   e y toss cpant    b  e  u b  budget l  l l    i a  y  u e library    m      t   swim ", \
            "f  engineering o  v      i    o  e  c b s    t involvement   p    u a      take leather  g l  r         atemperature   m  a s         el s training l a k          o c   suggestion k     a  i   g  everything          e  k give", \
            "    s   e  feed must m v m        above ally  r  g t r r i s e  e i y k t e s f  v where t palm a h t r t e e  t e i a l case i r n t e t h note g u m    s n    truerough  year e n  p i     o   t comfortable     n t     l    ", \
            "    statement i p    s  a  h n r constitute t o    e  h  m e c  r s       rdecrease y  d e d  g m  e  o s u rule  s port r  l next  r i e cast  e    nb   r  park   ga role   d h m s a y   variousi i      y g s consumer  that ", \
            "foot tunnel     p         k    p meat  singer o  s  a a o x  raise r u with t  e  r c l r human wage e a  n  t  n   door i  i  g r g r  t false e e d  y  l  m g   i   call e a tiny  o y  n r a a work   t d l r   n        e y ",\
            " c   attractivewound           o     taste i spot    n y  n  e e body p  v frame r whisper a p  i h c  s  t e federal t  i r  n r l  i woman t e long  n t  a   y  a w quarter    t i  r  i  streetrefer o        e     n  card  ",\
            "i  a  r  poetryl  s beat      less  s  shall u  o  e  p    ms occur  e  r et  i  v scene ar  a  a  i  g sa  taste f  a ut  i  i minor renjoy o  c  d e   n  n  a film e  k  poll n etactic   l  g n s  n    y    t target   four "]


#choosing one of the 10 strings randomly
stringRandomizer=random.randint(0, len(crosswords)-1)
stringChosen=crosswords[stringRandomizer]

#hiddenBoard creation
characterPosition=0
for row in range(numRows):
	rowList=[]
	for col in range(numCols):
		rowList.append(stringChosen[characterPosition])
		characterPosition+=1
	hiddenBoard.append(rowList)
	
#replacing characters of string chosen in hidden board with _ for display board		
displayBoard=hiddenBoard
for r in range(numRows):
	for c in range(numCols):
		if hiddenBoard[r][c]!=' ':
			displayBoard[r][c]='_'


def winCheck():
	while printBoardDisplay!=printBoardHidden:
		win=False
	if printBoardDisplay==printBoardHidden:
		win=True
		os.system("clear")
		printBoardHidden()
		print('Congratulations! You have completed the crossword')

def printBoardDisplay():
	for cols in range(numCols):
		print ('   ', end='')
	print()
	print("\n "+'____'*numCols)
	for row in range(numRows):
		print('|', end='')
		for col in range(numCols):
			print(displayBoard[row][col]+'   ', end='')
		print('|', end='')	
		print("\n "+"   "*numCols)
	print(' ___'*numCols)
	print()

#characterPosition=0
def printBoardHidden():
	for cols in range(numCols):
		print ('   ', end='')
	print()
	print("\n "+'____'*numCols)
	for row in range(numRows):
		print('|', end='')
		rowList=[]
		for col in range(numCols):
			print(hiddenBoard[row][col]+'   ', end='')
			print('|', end='')	
			print("\n "+"   "*numCols)
		print(' ___'*numCols)
		print()


print('Welcome to the hangman cross-word puzzle game')
print()
printBoardDisplay()

count=0
while win==False:
	printBoardDisplay()
	count+=1
	print('Trial #',count)
	characterChoice=input('Enter a lowercase letter ')
	

#reject input if digit or several charcters or capital letter
	while characterChoice.isdigit() or characterChoice.isupper() or len(characterChoice)!=1:
		print('Invalid input')
		characterChoice=input('Enter a lowercase letter ')
		count+=1
		print('Trial #',count)

#checking if letter is not present		
	if characterChoice not in stringChosen:
		if characterChoice in incorrect_guesses:
			print('Character already chosen previously')
		else:
			print()
			print('Letter not present')
			incorrect_guesses.append(characterChoice)
			incorrect_guesses.sort()
			print('Incorrect guesses: ',incorrect_guesses)

#if characterChoice in stringChosen:
	for row in range(numRows):
		for col in range(numCols):
			if characterChoice==hiddenBoard[row][col]:
				displayBoard[row][col]=hiddenBoard[row][col]

	winCheck()




