import time
import sys

def slow_print(text, delay=0.03):
    """Prints text character by character with a delay."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()  # Ensure the character is immediately displayed
        time.sleep(delay)
    print() # Add a newline at the end