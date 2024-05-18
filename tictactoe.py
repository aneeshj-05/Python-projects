board={'top-L':'','top-M':'','top-R':'',
	'mid-L':'','mid-M':'','mid-R':'',					#SETTING UP AN EMPTY GRID
	'low-L':'','low-M':'','low-R':''}
def printboard(board):
	print(board['top-L'],'|',board['top-M'],'|',board['top-R'],'|')
	print('--+--+--+')
	print(board['mid-L'],'|',board['mid-M'],'|',board['mid-R'],'|')		#PRINTING THE EMPTY BOARD OF TIC-TAC-TOE
	print('--+--+--+')
	print(board['low-L'],'|',board['low-M'],'|',board['low-R'],'|')
print('Welcome to tic-tac-toe')
printboard(board)
print('enter the respective choices of player1 and player2 separated by a space!')
pl1,pl2=set(map(int,input().split()))								#TWO INPUTS SEPARATED BY A SPACE
flag1=0
for i in range(9):
	if flag1==0:								#B IS EQUAL TO ZERO ONLY IF THE ENTERED POSTION IS EMPTY
		print(' _________')
		print('|PLAYER 1:|')
		print('enter the position where you wanna insert ',pl1,':(top-L/top-M/top-R/mid-L/mid-M/mid-R/low-L/Low-M/Low-R)')#THE POSITION WHERE YOU WANNA ENTER YOUR CHOICE
		pos=input()
		if board[pos]=='':						#CHECKS WHETHER THE ENTERED POSTITION IS EMPTY OR NOT!
			board[pos]=pl1						#ASSIGNING THE RESPECTIVE VALUE TO THAT POSITION
			printboard(board)
			flag1=1							#A RANDOM VARIABLE USED TO DENOTE THAT THE ENTERED POSTION IS FILLED
			if (board['top-L']==board['top-M']==board['top-R']==pl1) or (board['mid-L']==board['mid-M']==board['mid-R']==pl1) or (board['low-L']==board['low-M']==board['low-R']==pl1) or (board['top-L']==board['mid-L']==board['low-L']==pl1) or (board['top-M']==board['mid-M']==board['low-M']==pl1) or (board['top-R']==board['mid-R']==board['low-R']==pl1) or (board['top-L']==board['mid-M']==board['low-R']==pl1) or (board['top-R']==board['mid-M']==board['low-L']==pl1):
				flag2=1						#A IS ASSIGNED TO 1 ONLY IF PLAYER 1 WINS
				break
		else:								#WHEN THE POSITION IS NOT EMPTY THE VALUE OF B IS NOT EQUAL TO 0
			print('the position that you have entered is already filled!,try some other position')
			continue
	if flag1==1:								#B IS ASSIGNED THE VALUE 1 ONLY IF THE PLAYER 1 HAS SUCCESFULLY INSERTED HIS CHOICE IN THE RESPECTIVE POSITON
		print(' _________')
		print('|PLAYER 2:|')
		print('enter the position where you wanna insert ',pl2,':(top-L/top-M/top-R/mid-L/mid-M/mid-R/low-L/Low-M/Low-R)')#THE POSITION WHERE PLAYER 2 WANNA ENTER HIS CHOICE
		poe=input()
		if board[poe]=='':						#CHECKS WHETHER THE POSITION IS EMPTY OR NOT!
			board[poe]=pl2
			printboard(board)
			flag1=0							#B IS ASSIGNED TO ZERO AGAIN SO THAT IT GOES BACK TO PLAYER 1
			if (board['top-L']==board['top-M']==board['top-R']==pl2) or (board['mid-L']==board['mid-M']==board['mid-R']==pl2) or (board['low-L']==board['low-M']==board['low-R']==pl2) or (board['top-L']==board['mid-L']==board['low-L']==pl2) or (board['top-M']==board['mid-M']==board['low-M']==pl2) or (board['top-R']==board['mid-R']==board['low-R']==pl2) or (board['top-L']==board['mid-M']==board['low-R']==pl2) or (board['top-R']==board['mid-M']==board['low-L']==pl2):
				flag2=2						#GOES TO THE 49TH LINE AND EXECUTES THE PRINT STATEMENT
				break
		else:
			print('the position that you have entered is already filled,try some other position')
			flag1=1							#GOES BACK TO LINE 31
			continue
if flag2==1:									#FROM LINE 26
	print('CONGO player1!, you won!')
else:
	print('CONGO player2!, you won!')					#FROM LINE 41
