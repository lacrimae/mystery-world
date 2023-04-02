import sys
import time

from threading import Thread

waiting_time = 0.05


# Uncomment the following line to test the game without delayed printing (for debugging purposes only)
# waiting_time = 0


# todo: implement interruption of typing (when a player presses "enter", text should be typed instantly)
# def check():
#     i = input()
#     sys.stdout.flush()
#     global waiting_time
#     waiting_time = 0
#
#
# Thread(target=check).start()


def print_slow(message):
    global waiting_time
    for character in message:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(waiting_time)
