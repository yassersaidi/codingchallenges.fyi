import sys
import os
import argparse
import pathlib
from PIL import Image
from collections import Counter

def read_image(file):
    try:
        with Image.open(file, "r") as image: 
            width, height = image.size
            color_counter = Counter()
            print("Starting...")
            for x in range(width):
                for y in range(height):
                    rgb_value = image.getpixel((x,y))
                    color_counter[rgb_value] += 1
            rgb_color, size = color_counter.most_common(1)[0]
            r, g, b = rgb_color
            return rgb2hex(r,g,b)
    except FileNotFoundError:
        print(f"Error: File {file} does not exist.")
        sys.exit(1)


def rgb2hex(r,g,b):
    return "#{:02x}{:02x}{:02x}".format(r,g,b)

def main():
    parser = argparse.ArgumentParser(description="Most color indicator for jpeg and png images")
    parser.add_argument("filename", nargs="?", help="Most color indicator for jpeg and png images")
    args = parser.parse_args()

    if args.filename:
        if os.path.isfile(args.filename):
            if pathlib.Path(args.filename).suffix.lower() in [".jpeg",".png"]:
                print(f"Most common color in {args.filename} is: {read_image(args.filename)}")
        else:
            print(f"Error: {args.filename} is not a file, check the file type too it should jpeg or png ")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()