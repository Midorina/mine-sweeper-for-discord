import random
from typing import List

done = False

BOMB_EMOTE = ":bomb:"
NUMBER_EMOTES = (
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


class MineSweeper:
    def __init__(self):
        self.size: int = 0
        self.difficulty: int = 0

        self.map: List[List[int]] = []
        self.map_text: str = ""

    def set_size(self):
        while True:
            try:
                _size = int(input("Please input the length of the field (You shouldn't go over 12): "))
            except ValueError:
                print("You dumb? Try to input a proper number next time. I'm asking again...")
            else:
                if _size < 1:
                    print("Size can't be less than 1!")
                else:
                    self.size = _size
                    return

    def set_difficulty(self):
        while True:
            try:
                _difficulty = int(input("Please input the difficulty (0-100) (25-30 is ideal): "))
            except ValueError:
                print("You dumb? Try to input a proper number next time. I'm asking again...")
            else:
                if not 0 <= _difficulty <= 100:
                    print("Try to stick to the 0-100 rule. You must input a number between 0 and 100.")
                else:
                    self.difficulty = _difficulty
                    return

    def create_and_set_map(self):
        _map = []

        for x in range(self.size):
            _map.append([])
            for y in range(self.size):
                _random = random.randrange(101)
                # if difficulty is high, chances of getting a higher number is less
                if self.difficulty > _random:  # if bomb
                    _map[x].append(0)
                else:
                    _map[x].append(1)

        self.map = _map

    def convert_to_text(self):
        _text = ""

        for x in range(len(self.map)):
            for y in range(len(self.map)):
                if self.map[x][y] == 1:
                    _text += "||" + NUMBER_EMOTES[self._get_adjacent_bomb_count(x, y)] + "||"
                else:
                    _text += "||" + BOMB_EMOTE + "||"
            _text += "\n"

        self.map_text = _text

    def _get_adjacent_bomb_count(self, x, y):
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
                adjacent_bombs.append(self.map[coord[0]][coord[1]])
            except IndexError:  # if outside of the map, pass
                pass

        adjacent_bombs = list(filter(lambda e: e == 0, adjacent_bombs))
        return len(adjacent_bombs)

    def copy_to_clipboard(self):
        if len(self.map_text) > 2048:
            print("The character length exceeds 2048 characters! You'll most likely not able to post this on Discord."
                  "However, I'm still going to copy it to your clipboard.")

        try:
            from pyperclip import copy
        except ImportError:
            print("I can't copy the game to your clipboard, soo here is the text for you to copy yourself:\n")
            print(self.map_text)
        else:
            try:
                copy(self.map_text)
                print("It's been copied to your clipboard! Go to Discord and do CTRL+V in chat.")

            except Exception as e:
                print("An error has occurred while trying to copy to your clipboard: \n", e)

    @staticmethod
    def status_check():
        while True:
            status = input("Type 1 to continue creating, or 0 to leave the program: ")

            if status == "1":
                return
            elif status == "0":
                global done
                done = True
                return
            else:
                print("You dumb? I'm asking again...")

    def run(self):
        self.set_size()
        self.set_difficulty()
        self.create_and_set_map()
        self.convert_to_text()
        self.copy_to_clipboard()
        self.status_check()


if __name__ == '__main__':
    while not done:
        MineSweeper().run()
