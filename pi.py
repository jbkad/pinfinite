from input_handler import get_key
import time
import os

# First 100 digits of pi (after 3)
PI_DIGITS = (
    "14159265358979323846264338327950288419716939937510"
    "58209749445923078164062862089986280348253421170679"
    "82148086513282306647093844609550582231725359408128"
)

def play_game():
    print("Welcome to pinfinite, the pi memory game! Let's test how many numbers your remember.")
    print("Press 'q' at any time to quit.")

    index = 0;
    start_time = time.time()

    while True: 
        expected_digit = PI_DIGITS[index]
        print(f"Digit #{index + 1}: ", end="", flush=True)
        user_input = get_key()

        print(user_input)

        # quit game
        if user_input.lower() == 'q':
            print("Thanks for playing!")
            break

        if user_input == expected_digit: 
            index += 1
            
        else:
            print(f"Wrong! The correct digit was '{expected_digit}'.")
            print(f"Final score: {index}")
            elapsed_time = time.time() - start_time
            print(f"Time taken: {elapsed_time:.2f} seconds")

            # reset fields
            index = 0
            start_time = time.time()

if __name__ == "__main__":
    play_game()