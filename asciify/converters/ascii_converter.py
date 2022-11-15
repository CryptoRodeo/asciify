from PIL import Image, ImageOps
import os

class AsciiConverter:

    def __init__(self, file_name="", shrink_ratio=15, output_file="res.txt"):
        self.file_name = file_name
        self.shrink_ratio = shrink_ratio
        self.output_file = output_file

    def get_char(self, code):
        if code < 120:
            return ' • '
        if 120 <= code < 140:
            return ' * '
        elif 140 <= code < 180:
            return ' . '
        elif 180 <= code < 220:
            return ' - '
        elif 220 <= code <= 255:
            return '   '

    def __generate_temp_name(self, original_img_name):
        if original_img_name is None:
            raise Exception('Error: No file has been specified')

        new_name = original_img_name.replace('.png', '-temp.png')
        return new_name

    def __setup(self, img_name=None, shrink_ratio=1):
        # Generate a name for the temp file
        temp_img_name = self.__generate_temp_name(img_name)
        with Image.open(img_name) as img:
            # Get height, width and apply shrink ratio
            height = int( img.height / shrink_ratio)
            width = int(img.width / shrink_ratio)
            # resize image
            img = img.resize((width, height))
            # Convert image to grayscale so it's easier
            # to generate characters based on it's RGB value
            img = ImageOps.grayscale(img)
            # save changes to new image
            img.save(temp_img_name)

        return temp_img_name

    def __convert(self, img_name):
        data = []
        with Image.open(img_name) as img:
            width, height = img.size
            for y in range(height):
                data.append('')
                for x in range(width):
                    val = img.getpixel((x,y))
                    char = self.get_char(val)
                    if char is None:
                        raise Exception(f"No character mapped for value {val}")
                    data[y] += (self.get_char(val))
        return data

    def __write_to_file(self, file_name: str, data: list):
        """Writes the ascii characters to the specified file

        Args:
            file_name (str): Name of file to write ascii characters to
            data (list): list of ascii characters
        """
        with open(file_name, 'w') as txt:
            for s in data:
                print(s, file=txt)

    def __clean_up(self, temp_file_name: str):
        """Removes the temp operating file

        Args:
            temp_file_name (string): Name of the temp file we're operating on

        Raises:
            Exception: File {temp_file_name} not found
        """
        if os.path.exists(temp_file_name):
            os.remove(temp_file_name)
        else:
            raise Exception(f"File: {temp_file_name} not found.")

    def run(self):
        """Runs the conversion process
        """
        temp_file_name = self.__setup(self.file_name, self.shrink_ratio)
        data = self.__convert(temp_file_name)
        self.__write_to_file(file_name=self.output_file, data=data)
        self.__clean_up(temp_file_name)
