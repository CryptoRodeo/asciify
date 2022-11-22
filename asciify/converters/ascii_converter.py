import os

from helpers.map_processor import MapProcessor
from PIL import Image, ImageOps


class AsciiConverter:
    """ Converts an image to ascii using specified parameters
    """

    def __init__(self, file_name=None, shrink_ratio=None, output_file=None, character_map=None):
        self.file_name = file_name
        self.shrink_ratio = shrink_ratio
        self.output_file = output_file

        # create map processor, import character map
        self.map_processor = MapProcessor(character_map)

    def get_char(self, pixel_value: int):
        """Gets the character for the pixel value

        Args:
            pixel_value (int): the pixel value

        Returns:
            str: character that maps to that pixel value
        """
        return self.map_processor.get_char(pixel_value)

    def __generate_temp_name(self, original_img_name: str):
        """generates a temporary file name for the temp image we'll operate on.

        Args:
            original_img_name (str): name of the original image

        Raises:
            Exception: No image file has been specified

        Returns:
            str: temp file name
        """
        if original_img_name is None:
            raise Exception('Error: No image file has been specified')

        new_name = original_img_name.replace('.png', '-temp.png')
        return new_name

    def __setup(self, img_name:str=None, shrink_ratio:int=1):
        """Sets up the image we'll be operating on by:
            - creating a temporary file name
            - resizing the image based on the shrink ratio
            - converting the image to grayscale
            - saving those changes on a temporary image file

        Args:
            img_name (str, optional): name of image we'll operate on. Defaults to None.
            shrink_ratio (int, optional): how much we want to shrink the image. Defaults to 1.

        Returns:
            str: name of the temp image we'll operate on
        """
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

    def __convert(self, img_name:str):
        """Converts the image to ascii by:
            - looping through the image's height and width
            - getting the pixel value for the image at x,y coordinate
            - getting the character for the pixel value
            - appending that value to a list

        Args:
            img_name (str): name of image we'll be converting

        Raises:
            Exception: No character mapped for value {val}

        Returns:
            list: the list of the ascii characters generated for that image
        """
        data = []
        with Image.open(img_name) as img:
            width, height = img.size
            for y in range(height):
                data.append('') # start off the row with an empty string
                for x in range(width):
                    val = img.getpixel((x,y))
                    char = self.get_char(val)
                    if char is None:
                        raise Exception(f"No character mapped for value {val}")
                    data[y] += (self.get_char(val)) # append character to that row
        return data

    def __write_to_file(self, file_name: str, data: list):
        """Writes the ascii characters to the specified file

        Args:
            file_name (str): Name of file to write ascii characters to
            data (list): list of ascii characters
        """
        with open(file_name, 'w') as f:
            for section in data:
                print(section, file=f)

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
