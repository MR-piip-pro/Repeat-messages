
# Auto Message Typing Script

## Description
This script simulates typing a message repeatedly using the `pyautogui` library. You can specify the message, the number of times it will be typed, the time interval between each message, and a delay before starting the typing process.

## Requirements

To run this script, you need the following:

- Python 3
- `pyautogui` library
  
You can install `pyautogui` using pip:

```bash
pip install pyautogui
```

## How to Use

1. Run the script using Python:

```bash
python script.py
```

2. Enter the message you want to type.
3. Specify the number of times the message should be sent.
4. Set the time interval between each message (in seconds).
5. Set the delay before the typing starts (in seconds).

For example:

```plaintext
Please enter the message to type: Hello, world!
Please enter the number of messages you want to send: 5
Please enter the time interval between each message (e.g., 0.1): 1
Please enter the duration to wait before you start typing (in seconds): 3
```

In this example, the message "Hello, world!" will be typed 5 times, with a 1-second interval between each message, after waiting for 3 seconds before starting.

## Code Details

The script uses two main libraries:
- `pyautogui`: to control the keyboard and simulate key presses.
- `time`: to manage timing and delays.

### Function `type_message`
This function simulates typing a message a specified number of times, with a delay between each repetition.

#### Arguments:
- `message` (string): The message to be typed.
- `num_times` (int): The number of times the message will be typed.
- `interval_seconds` (float): The time interval between each message.
- `tim` (float): The delay before typing starts.

## Important Notes
- Ensure you have the necessary permissions to control the keyboard.
- The script sends messages to whichever window or program is in focus, so make sure the target window is open and ready to receive input before running the script.
