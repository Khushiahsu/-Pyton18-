#Write a program to generate a random integer and match it with the input given by the user?
import random

a = True
num=str(random.randint(0 , 100))#generates one number within the given range
print('I will be gernerating a number between 0-100 and you have to try and guess it!')
print('The game ends as soon as you get 1')
while a:
    b = input('Give me your guess!')
    if num == b:
        print('You have guessed correctly!')
        print("The number is ",num)
        break
    else:
        print('You have sadly got the answer wrong. Please try again!\n')
        print(num)