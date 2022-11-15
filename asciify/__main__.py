import argparse
import app

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file_name', help="image file to process", default=None, type=str)
    parser.add_argument('-s', '--shrink_ratio', help="shrink ratio for image", default=15, type=int)
    parser.add_argument('-o', '--output_file', help='file to output to', default='res.txt', type=str)
    parser.add_argument('-m', '--char_map', help="char map file to map pixel values to characters", default="character_maps/default.json", type=str)
    args = parser.parse_args()
    app.run(args.file_name, args.shrink_ratio, args.char_map, args.output_file)

if __name__ == "__main__":
    main()
