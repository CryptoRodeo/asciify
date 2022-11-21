import pytest
from asciify.helpers.map_processor import MapProcessor
from PIL import Image
from pathlib import Path

TEST_IMAGE_PATH = "tests/test_images/"
DEFAULT_CHAR_MAP = "character_maps/default.json"

@pytest.fixture
def image_names():
    source_dir = Path(TEST_IMAGE_PATH)
    files = source_dir.iterdir()
    file_names = []
    for file in files:
        file_names.append(file.name)

    return file_names

@pytest.fixture
def expected_char_for_image():
    return {
        '162.png': ' . ',
        '255.png': '   ',
        '50.png': ' • ',
        '123.png': ' * ',
        '0.png': ' • ',
        '87.png': ' • ',
        '209.png': ' - '
    }

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

        assert all(chars_for_code)
        assert expected_char_for_image[image_name] == chars_for_code[0]