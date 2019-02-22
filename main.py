import random
import pyperclip

done = False
true_emote = ":green_heart:"
false_emote = ":bomb:"


def get_size():
    try:
        size = int(input("Please input the length of the field (You shouldn't go over 12): "))
        if size >= 1:
            return size
        else:
            print("You must input a positive integer!")
            get_size()

    except ValueError:
        print("You dumb? Try to input a proper number next time. I'm asking again...")
        get_size()


def get_difficulty():
    try:
        difficulty = int(input("Please input the difficulty (0-100) (35-40 is ideal): "))
        if 0 <= difficulty <= 100:
            return difficulty
        else:
            print("Try to stick to the 0-100 rule. You must input a number between 0 and 100.")
            get_difficulty()

    except ValueError:
        print("You dumb? Try to input a proper number next time. I'm asking again...")
        get_difficulty()


def status_check():
    status = input("Type 1 to continue creating, or 0 to leave the program: ")
    if status == "1":
        return
    elif status == "0":
        global done
        done = True
        return
    else:
        print("You dumb? I'm asking again...")
        status_check()


def copy_to_clipboard(text):
    if len(text) > 2000:
        print("The character length exceeds 2000 characters! You'll most likely not able to post this on Discord."
              "However, I'm still going to copy it to your clipboard.")
    try:
        pyperclip.copy(text)
        print("It's been copied to your clipboard!")
    except Exception as e:
        print("An error occured: \n", e)


def convert_to_text(_map):
    text = ""
    for x in range(len(_map)):
        for y in range(len(_map)):
            if _map[x][y] == 1:
                text += "||" + true_emote + "||"
            else:
                text += "||" + false_emote + "||"
        text += "\n"

    return text


def create(size, difficulty):
    _map = []

    try:
        for x in range(size):
            _map.append([])
            for y in range(size):
                _random = random.randrange(101)
                # if difficulty is high, chances of getting a higher number is less
                if difficulty > _random:
                    _map[x].append(0)
                else:
                    _map[x].append(1)

    except Exception as e:
        print(f"An error occurred while creating: \n", e)

    return _map


while not done:
    size = get_size()

    difficulty = get_difficulty()

    _map = create(size, difficulty)

    text = convert_to_text(_map)

    copy_to_clipboard(text)

    status_check()

