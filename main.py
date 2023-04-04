import pyautogui as gui
import time


while True:
    user_input = input("-- Enter delay time in minutes and press ENTER to accept --\n"
                       "\tNote: 0.1 = 10 seconds, 1 = 60 seconds, etc\n"
                       "\tDefault delay time is 10 minutes, press ENTER through\n"
                       "\tthis prompt to accept the default value.\n>")

    if user_input == "":
        user_input = 10

    elif user_input[0] == '-':
        print("Negative values aren't accepted.")
        continue

    elif user_input.isnumeric():
        # print(user_input)
        if int(user_input) <= 0:

            print("Negative values aren't accepted")
            continue

    elif user_input.isalpha():
        print("Input must be a number value between 0.1 and "
              "<SOME UNGODLY LARGE NUMBER>")
        continue

    wiggle_distance = input("-- Now enter the wiggle distance --\n"
                            "\tNote: Large values are very noticeable.\n"
                            "\tDefault = 2\n"
                            "\tKeep this number between 1-10 for best results.\n>")

    print()

    if wiggle_distance == "":
        wiggle_distance = 2

    elif wiggle_distance[0] == '-':
        print("Negative values aren't accepted.")
        continue

    elif wiggle_distance.isnumeric():
        # print(user_input)
        if int(wiggle_distance) <= 0:

            print("Negative values aren't accepted")
            continue

    elif wiggle_distance.isalpha():
        print("Input must be a number value between 0.1 and "
              "<SOME UNGODLY LARGE NUMBER>")
        continue

    minutes = float(user_input)
    # minutes = 0.1
    seconds = minutes * 60

    print("To quit, use CTRL-C, or simply close this window.")
    while True:
        x, y = gui.position()
        gui.moveTo(x + wiggle_distance, y + wiggle_distance)
        gui.moveTo(x, y)
        time.sleep(int(seconds))
