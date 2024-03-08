import random

def play_guessing_game():
    try:
        mystery_number = random.randint(1, 100)
        max_tries = 5
        attempts = 0
        print("Welcome to the Number Guessing Game!")
        print(f"Try to guess the secret number between 1 and 100. You have {max_tries} attempts.")

        while attempts < max_tries:
            try:
                user_input = int(input("Enter your guess: "))

                if user_input == mystery_number:
                    print(f"Congratulations! You guessed the correct number {mystery_number}!")
                    return True
                elif user_input < mystery_number:
                    print("Try a larger number.")
                else:
                    print("Try a smaller number.")

                attempts += 1
                remaining_attempts = max_tries - attempts
                print(f"You have {remaining_attempts} attempts remaining.\n")

            except ValueError:
                raise ValueError(f"Invalid input. Please enter a valid number.")

        else:
            print(f"Sorry, you've run out of attempts. The correct number was {mystery_number}.")
            return False

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    play_guessing_game()
