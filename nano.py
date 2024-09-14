import pyautogui as pg  # Import pyautogui library for controlling the mouse and keyboard
import time             # Import time library for handling time delays
from os import system

def Repeat_messages():
    def type_message(message, num_times, interval_seconds, tim):
        """
        Simulates typing a message repeatedly.

        Args:
            message (string): The message to be typed.
            num_times (int): The number of times the message will be typed.
            interval_seconds (float): The time interval (in seconds) between each message.
            tim (float): The waiting duration (in seconds) before starting to type.
        """

        # Validate inputs to prevent incorrect values
        if num_times <= 0 or interval_seconds < 0 or tim < 0:
            print("\033[1;31m Error: All numeric inputs must be non-negative, and num_times must be greater than 0.")
            return

        # Print information about the operation to be performed
        print(f"\033[1;32mTyping \033[1;31m'{message}'\033[1;32m the number of messages \033[1;31m{num_times}\033[1;32m times with an interval of \033[1;31m{interval_seconds}\033[1;32m seconds after waiting \033[1;31m{tim}\033[1;32m seconds:")

        # Wait for 'tim' seconds before starting to type
        time.sleep(tim)

        # Loop to type the message repeatedly
        for i in range(num_times):
            pg.write(message, interval=0.00000001)  # Type the message with a small delay between each character
            pg.press("Enter")  # Press the Enter key after each message
            time.sleep(interval_seconds)  # Wait for the specified interval before typing the next message
            print(f"\033[1;36mMessage \033[1;31m{i+1}\033[1;36m/\033[1;31m{num_times} \033[1;36msent")  # Inform the user about the progress
        
        # Print a message indicating that typing is complete
        print("\033[1;32mMessage typing complete \033[0m")  # Reset color to default after completion

    # Function to get user input with validation
    def get_user_input(prompt, input_type=float, condition=lambda x: x >= 0):
        while True:
            try:
                user_input = input_type(input(prompt))
                if condition(user_input):
                    return user_input
                else:
                    print("\033[1;31mInvalid input. Please try again.")
            except ValueError:
                print("\033[1;31mInvalid input type. Please enter a valid number.")

    while True:
        # Ask the user to input the message
        print("\033[1;35m═════════════════════════════════════════════════════════════════════════════════════════")    
        message = input("\033[1;36mPlease enter the message to type: \033[1;31m")
        print("\033[1;35m═════════════════════════════════════════════════════════════════════════════════════════")
        # Ask the user for the number of times to send the message (must be positive)
        num_times = get_user_input("\033[1;36mPlease enter the number of messages you want to send: \033[1;31m", int, lambda x: x > 0)
        print("\033[1;35m═════════════════════════════════════════════════════════════════════════════════════════")
        # Ask the user for the time interval between each message (must be non-negative)
        interval_seconds = get_user_input("\033[1;36mPlease enter the time interval between each message (e.g., 0.1): \033[1;31m", float)
        print("\033[1;35m═════════════════════════════════════════════════════════════════════════════════════════")
        # Ask the user for the duration to wait before starting to type (must be non-negative)
        tim = get_user_input("\033[1;36mPlease enter the duration to wait before you start typing (in seconds): \033[1;31m", float)
        print("\033[1;35m═════════════════════════════════════════════════════════════════════════════════════════")
        # Call the function to type the user's message with the specified interval
        type_message(message, num_times, interval_seconds, tim)
        
        

        # Ask the user if they want to repeat the process or exit
        repeat = input("\033[1;34mDo you want to type another message (yes/no)? (y/n): \033[1;31m").strip().lower()
        system("cls")
        if repeat != 'y':    
            print("\033[1;32mExiting program. Goodbye! \033[0m")
            break
Repeat_messages()

