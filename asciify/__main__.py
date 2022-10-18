import argparse
from ascii_converter import AsciiConverter

def asciify(file_name, shrink_ratio, output_file):
    try:
        AsciiConverter(
            file_name=file_name,
            shrink_ratio=shrink_ratio,
            output_file=output_file
        ).run()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file_name', help="image file to process", default=None, type=str)
    parser.add_argument('-s', '--shrink_ratio', help="shrink ratio for image", default=15, type=int)
    parser.add_argument('-o', '--output_file', help='file to output to', default='res.txt', type=str)
    parser.add_argument('-m', '--image-map', help="image map file to map pixel values to characters", type=str)
    args = parser.parse_args()
    asciify(args.file_name, args.shrink_ratio, args.output_file)