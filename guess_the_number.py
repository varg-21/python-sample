import random

def enter_choice():
    ch = int(input("Enter your choice (0/1): "))
    if ch == 0:
        guess(10)
    elif ch == 1:
        computer_guess(100)

def guess(x):
    random_number = random.randint(1, x)
    
    guess = 0

    while guess != random_number:
        guess = int(input(f"Enter a guess between 1 and {x}: "))    
        if guess > random_number:
            print("Guess is too high")
        elif guess < random_number:
            print("Guess is too low")
    print(f"The number is {random_number}. You guessed it right.")

def computer_guess(x):
   low = 1
   high = x
   
   feedback = ''

   while feedback != 'c':
       guess = random.randint(low, high)
       feedback = input(f"Is {guess} higher(h) or lower(l) than your number or correct (c): ")
       if feedback == 'h':
           high = guess - 1
       elif feedback == 'l':
            low = guess + 1
       elif feedback == 'c':
           print("I guessed it right")

enter_choice()