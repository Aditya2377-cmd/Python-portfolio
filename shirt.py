import sys
import os
from PIL import Image, ImageOps


def main():
    check_args()
    try:
        user_photo = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
        size = shirt.size
        fitted_photo = ImageOps.fit(user_photo, size)
        fitted_photo.paste(shirt, shirt)
        fitted_photo.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Input does not exist")


def check_args():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    ext1 = os.path.splitext(sys.argv[1])[1].lower()
    ext2 = os.path.splitext(sys.argv[2])[1].lower()

    valid_exts = [".jpg", ".jpeg", ".png"]
    if ext1 not in valid_exts or ext2 not in valid_exts:
        sys.exit("Invalid input")
    if ext1 != ext2:
        sys.exit("Input and output have different extensions")


if __name__ == "__main__":
    main()
