import json
import argparse

class MapProcessor:

    def __init__(self):
        self.data = {}

    def import_file(self, file_name: str):
        with open(file_name, 'r') as char_map:
            self.data = json.load(char_map)

    def print_data(self):
        print(self.data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--image-map', help="image map file to map pixel values to characters", type=str)
    args = parser.parse_args()
    mp = MapProcessor()
    mp.import_file(args.image_map)
    mp.print_data()