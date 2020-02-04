import random

can_copy = True
try:
    import pyperclip
except ImportError:
    can_copy = False

done = False

bomb_emote = ":bomb:"
number_emotes = (
    '0️⃣',
    '1️⃣',
    '2️⃣',
    '3️⃣',
    '4️⃣',
    '5️⃣',
    '6️⃣',
    '7️⃣',
    '8️⃣',
    '9️⃣',
)


def get_size():
    try:
        _size = int(input("Please input the length of the field (You shouldn't go over 12): "))
    except ValueError:
        print("You dumb? Try to input a proper number next time. I'm asking again...")
        return get_size()

    if _size >= 1:
        return _size
    else:
        print("Size can't be less than 1!")
        return get_size()


def get_difficulty():
    try:
        _difficulty = int(input("Please input the difficulty (0-100) (25-30 is ideal): "))
    except ValueError:
        print("You dumb? Try to input a proper number next time. I'm asking again...")
        return get_difficulty()

    if 0 <= _difficulty <= 100:
        return _difficulty
    else:
        print("Try to stick to the 0-100 rule. You must input a number between 0 and 100.")
        return get_difficulty()


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
        return status_check()


def copy_to_clipboard(_text: str):
    if len(_text) > 2000:
        print("The character length exceeds 2000 characters! You'll most likely not able to post this on Discord."
              "However, I'm still going to copy it to your clipboard.")

    if can_copy:
        try:
            pyperclip.copy(_text)
            print("It's been copied to your clipboard!")

        except Exception as e:
            print("An error occured while trying to copy to your clipboard: \n", e)

    else:
        print("I can't copy the game to your clipboard soo here is the text for you to copy yourself:")
        print(_text)


def convert_to_text(_map):
    _text = ""

    for x in range(len(_map)):
        for y in range(len(_map)):
            if _map[x][y] == 1:
                _text += "||" + number_emotes[get_adjacent_bomb_count(_map, x, y)] + "||"
            else:
                _text += "||" + bomb_emote + "||"
        _text += "\n"

    return _text


def get_adjacent_bomb_count(_map, x, y):
    adjacent_coords = (
        (x - 1, y - 1),
        (x - 1, y),
        (x - 1, y + 1),

        (x, y - 1),
        (x, y + 1),

        (x + 1, y - 1),
        (x + 1, y),
        (x + 1, y + 1),
    )

    adjacent_bombs = []
    for coord in adjacent_coords:
        try:
            adjacent_bombs.append(_map[coord[0]][coord[1]])
        except IndexError:  # if outside of the map, pass
            pass

    adjacent_bombs = list(filter(lambda e: e == 0, adjacent_bombs))
    return len(adjacent_bombs)


def create(_size: int, _difficulty: int):
    _map = []

    for x in range(_size):
        _map.append([])
        for y in range(_size):
            _random = random.randrange(101)
            # if difficulty is high, chances of getting a higher number is less
            if _difficulty > _random:  # if bomb
                _map[x].append(0)
            else:
                _map[x].append(1)

    return _map


if __name__ == '__main__':
    while not done:
        size = get_size()

        difficulty = get_difficulty()

        created_map = create(size, difficulty)

        text = convert_to_text(created_map)

        copy_to_clipboard(text)

        status_check()
