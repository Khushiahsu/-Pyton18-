#Create a program to play rock, paper, and scissors. Use a random module to select from the given options Check whether the random guess matches the user’s answer
import random

a = str(input('We are playing rock paper scissors so pick your choice!'))

options=['rock','paper','scissors']

choice=str(random.choice(options))

print('Users choice:',a)
print('Programs choice:',choice)
if a == choice:
    print('We have tied!')
elif a == 'rock' and choice=='scissors':
    print('You have won the round!')
elif a == 'scissors' and choice =='rock':
    print('The program has won the round!')
elif a == 'paper' and choice == 'rock':
    print('You have won this round!')
elif a == 'rock' and choice == 'paper':
    print('The program has won this round!')
    
else:
    print("Invalid Input")





