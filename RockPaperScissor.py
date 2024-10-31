#Program to develop rock-paper-scissor game
import random
n=int(input("Enter your choice\n0:Rock\n1:Paper\n2:Scissors: "))
'''rock=''*''
paper=''###''
scissor=''$$$'''
if n==0:
	print("*ROCK*")
elif n==1:
	print("##PAPER##")
elif n==2:
	print("$$SCISSORS$$")
#l1=[rock,paper,scissor]
ra=random.randint(0,2)
if ra==0:
	print("ROCK**")
elif ra==1:
	print("PAPER##")
elif ra==2:
	print("SCISSORS$$")
if(n==ra):
    print("Draw")
elif(ra==1 and n==0):
    print("You loose")
elif(ra==0 and n==1):
    print("You Won")
elif(ra==0 and n==2):
    print("You loose")
elif(ra==2 and n==0):
    print("You Won")
elif(ra==2 and n==1):
    print("You loose")
else:
    print("You Won")
