from input_handler import get_key
from colorama import Fore, Style, init
import sys
import time
import os

init(autoreset=True)

# First 100 digits of pi (after 3)
PI_DIGITS = (
    "14159265358979323846264338327950288419716939937510"
    "58209749445923078164062862089986280348253421170679"
    "82148086513282306647093844609550582231725359408128"
)

def play_game():
    print(Style.BRIGHT + Fore.CYAN + "Welcome to Pinfinite! Let's test how many numbers of π your remember.")
    print("Press 'q' at any time to quit.")

    streak = "3."
    index = 0
    start_time = time.time()

    print(streak, end="", flush=True)

    while True: 
        expected_digit = PI_DIGITS[index]
        user_input = get_key()

        if index >= len(PI_DIGITS):
            print(Fore.MAGENTA + "Congratulations! You've completed the game!")
            break

        # quit game
        if user_input.lower() == 'q':
            print(Fore.YELLOW + "Game aborted. Thanks for playing!")
            break

        if user_input == expected_digit: 
            streak += user_input
            # print(f"\r{streak}", end="", flush=True)
            index += 1

            sys.stdout.write("\r" + " " * 80)
            sys.stdout.flush()
            sys.stdout.write("\r" + Fore.GREEN + streak)
            sys.stdout.flush()
            
        else:
            print(Fore.RED + f"{expected_digit}")
            print(Fore.YELLOW + f"Score: {index}")
            elapsed_time = time.time() - start_time
            print(Fore.YELLOW + f"Time taken: {elapsed_time:.2f}s")
            print(Fore.CYAN + "Restarting in 3 seconds...")
            time.sleep(3)

            # reset fields
            streak = "3."
            index = 0
            start_time = time.time()
            print(streak, end="", flush=True)

if __name__ == "__main__":
    play_game()