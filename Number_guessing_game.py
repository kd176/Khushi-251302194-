import random

#  Difficulty selection
def choose_difficulty():
    print("\nSelect Difficulty:")
    print("1. Easy (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard (1-500, 5 attempts)")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        return 1, 50, 10
    elif choice == "2":
        return 1, 100, 7
    elif choice == "3":
        return 1, 500, 5
    else:
        print("Invalid choice! Defaulting to Medium.")
        return 1, 100, 7


#  Hint system
def give_hint(secret, guess):
    diff = abs(secret - guess)
    
    if diff == 0:
        return "🎉 Perfect guess!"
    elif diff <= 5:
        return "🔥 Very very close!"
    elif diff <= 10:
        return "😊 Close!"
    else:
        return "😐 Far away!"


# 🎮 Main game function
def number_guessing_game():
    print("\n🎮 Welcome to Number Guessing Game!")

    low, high, max_attempts = choose_difficulty()
    secret_number = random.randint(low, high)
    
    attempts = 0

    print(f"\nI have selected a number between {low} and {high}.")
    print(f"You have {max_attempts} attempts. Good luck!\n")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            
            #  Range validation
            if guess < low or guess > high:
                print(f" Please enter a number between {low} and {high}")
                continue
            
            attempts += 1

            #  Hint system
            print(give_hint(secret_number, guess))

            if guess < secret_number:
                print("⬇️ Too low!")
            elif guess > secret_number:
                print("⬆️ Too high!")
            else:
                print(f"\n Correct! You guessed it in {attempts} attempts.")
                
                #  Score system
                score = max(0, 100 - attempts * 10)
                print(f" Your score: {score}")
                return

            print(f"Attempts left: {max_attempts - attempts}\n")

        except ValueError:
            print(" Please enter a valid number!")

    #  If user loses
    print(f"\n You lost! The number was {secret_number}")


#  Play again loop
def main():
    while True:
        number_guessing_game()
        
        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again != "yes":
            print(" Thanks for playing!")
            break


#  Start game
main()
