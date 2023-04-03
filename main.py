import pyautogui as gui
import time

minutes = 0.1
seconds = minutes * 60


while True:
    user_input = input("Enter delay time in minutes:"
                       "Note: 0.1 = 10 seconds, 1 = 60 seconds, etc\n>")

    if user_input.isnumeric():
        if int(user_input) <= 0:
            print("Negative values aren't accepted")
            continue

    if user_input.isalpha():
        print("Input must be an integer value between 0.1 and "
              "<SOME UNGODLY LARGE NUMBER>")
        continue

    if user_input == "":
        user_input = 10

    minutes = user_input

    print("To quit, use CTRL-C, or simply close this window.")
    while True:
        x, y = gui.position()
        gui.moveTo(x + 5, y + 5)
        gui.moveTo(x, y)
        time.sleep(seconds)
