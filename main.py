'''
snake = 1
water =-1
Gun   = 0
'''

import random

computer= random.choice([1,0,-1])
you= input("Enter your choice :")
youdict={'snake':1,'gun':0,'water':-1}
reversedict={1:'snake',0:'gun',-1:'water'}

me= youdict[you]

print(f"your choice is {you} and computer choice is {reversedict[computer]} ")

if me==computer:
    print("It's a tie")
else:
    if(me==1 and computer==-1):
        print("You win")
    elif(me==-1 and computer==0):
        print("You win")
    elif(me==0 and computer==1):
        print("You win")
    elif(me==-1 and computer==1):
        print("Computer wins")
    elif(me==0 and computer==-1):
        print("Computer wins")
    elif(me==1 and computer==0):
        print("Computer wins")




