import json

class MapProcessor:

    def __init__(self, file_name: str):
        self.data = {}
        with open(file_name, 'r') as char_map:
            self.data = json.load(char_map)

    def get_char(self, code: int):
        for char, range in self.data.items():
            if self.out_of_range(code, range):
                continue
            else:
                return char

    def out_of_range(self, val: int, range: list):
        low, high = range[0], range[1]
        if val < low or val > high:
            return True
        return False
