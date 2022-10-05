import random
import os

from art import logo
print(logo)

print("Welcome to the Number Guessing Game!\n\nI am thinking of a number between 1 and 100.")

def Ran_Num():
    ran_number = random.randint(1,100)
    return ran_number

c_random_num = Ran_Num()
print(c_random_num)

Difficulty_type = input("\nChoose a difficulty type. Type 'easy' or 'hard' : ").lower()

def attempts(Difficulty_type):
    if Difficulty_type == "easy":
        attempts = 10
    elif Difficulty_type == "hard":
        attempts = 5
        
    return attempts

attempt_count = attempts(Difficulty_type)
print(attempt_count)

play = True

while (play == True):
    
    for i in range(attempt_count,-1,-1):
        
        if i == 0:
            break
        
        print(f"you have {i} attempts remaining to guess the number.")
        guess  = int(input("Make a Guess : "))
                
        if guess == c_random_num:
            print(f"You got it!, The answer was {c_random_num}\n")
            break
        elif guess < c_random_num:
            print("Too Low..\n")
        elif guess > c_random_num:
            print("Too High..\n")
        
    
    if (i == 0):
        re_play = input(f"You have ran out of guessess!. The correct answer was {c_random_num}\n. Would you like to play again ?\n Enter 'y' for yes or 'n' for no.")
            
        if re_play == "y":
            play = True
            os.system("clear")
            c_random_num = Ran_Num()
            print(c_random_num)

        else:
            play = False
    elif (guess == c_random_num):
        re_play = input("Would you like to play again ?\n Enter 'y' for yes or 'n' for no.")
            
        if re_play == "y":
            play = True
            os.system("cls")
            c_random_num = Ran_Num()
            print(c_random_num)

        else:
            play = False
    


