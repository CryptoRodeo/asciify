import argparse
import app

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file_name', help="image file to process (required)", default=None, type=str)
    parser.add_argument('-s', '--shrink_ratio', help="shrink ratio for image, defaults to 1", default=1, type=int)
    parser.add_argument('-o', '--output_file', help='file to output to, defaults to res.txt', default='res.txt', type=str)
    parser.add_argument('-m', '--char_map', help="char map file to map pixel values to characters, defaults to character_maps/default.json", default="character_maps/default.json", type=str)
    args = parser.parse_args()
    app.run(args.file_name, args.shrink_ratio, args.char_map, args.output_file)

if __name__ == "__main__":
    main()
