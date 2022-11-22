import pytest
from asciify.helpers.map_processor import MapProcessor
from tests.fixtures.image_names import image_names, TEST_IMAGE_PATH
from tests.fixtures.expected_char_for_image import expected_char_for_image
from PIL import Image

DEFAULT_CHAR_MAP = "character_maps/default.json"

def test_image_char_value(image_names, expected_char_for_image):
    """Test that the correct value gets returned for a pixel value

    Args:
        image_names (List[string]): list of names for the test images
        expected_char_for_image (Dictionary[string]=string): Dictionary that holds the expected character for the pixel value
    """
    m = MapProcessor(DEFAULT_CHAR_MAP)
    for image_name in image_names:
        chars_for_code = []
        with Image.open(TEST_IMAGE_PATH + image_name) as img:
            img = img.convert('L')
            width, height = img.size
            for y in range(height):
                for x in range(width):
                    pixel_val = img.getpixel((x,y))
                    chars_for_code.append(m.get_char(pixel_val))

        # All the characters should be the same since the image is grayscale
        # and each image is a single color
        assert all(chars_for_code)
        # each image should generate one specific character
        assert expected_char_for_image[image_name] == chars_for_code[0]
