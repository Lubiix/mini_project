import random

number_to_guess = random.randrange(100)
guesses_chance = 0

print("How many times to guess ?")
guesses_chance = int(input())
print("Please enter a number:")
user_number = int(input())

while user_number != number_to_guess:
    guesses_chance -=1
    if guesses_chance > 0:
        if user_number > number_to_guess:
            print(f"The number is lower,{guesses_chance} try left")
            print("Please enter a number:")
            user_number = int(input())
        elif user_number < number_to_guess:
            print(f"The number is higher,{guesses_chance} try left")
            print("Please enter a number:")
            user_number = int(input())
    else:
        print(f"You lost the number was {number_to_guess}")
        break
else: 
    print("You won")
