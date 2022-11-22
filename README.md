# Asciify (WIP)
Transform images to ascii text

# Quick Start Guide
```bash
git clone git@github.com:CryptoRodeo/asciify.git

cd ./asciify

docker build . -t asciify

docker run -it --name="asciify" asciify

# Check help menu
$ python asciify -h
usage: asciify [-h] [-f FILE_NAME] [-s SHRINK_RATIO] [-o OUTPUT_FILE] [-m CHAR_MAP]

options:
  -h, --help            show this help message and exit
  -f FILE_NAME, --file_name FILE_NAME
                        image file to process
  -s SHRINK_RATIO, --shrink_ratio SHRINK_RATIO
                        shrink ratio for image
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        file to output to
  -m CHAR_MAP, --char_map CHAR_MAP
                        char map file to map pixel values to characters

# Asciify one of the test images
python asciify -f images/test.png -s 20 -o res.txt

# Change the character map to get different results
python asciify -f images/peng.png -s 20 -o res.txt -m character_maps/default.json
```