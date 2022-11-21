
import pytest
from PIL import Image
from pathlib import Path

TEST_IMAGE_PATH = "tests/test_images/"
@pytest.fixture
def image_names():
    source_dir = Path(TEST_IMAGE_PATH)
    files = source_dir.iterdir()
    file_names = []
    for file in files:
        file_names.append(file.name)

    return file_names

def test_image_pixel_value(image_names):
    """Test that the correct pixel value gets returned for the image

    Args:
        image_names (List[string]): list of names for our test images
    """
    for image_name in image_names:
        # text image names follow this format: gray-scale-pixel-val.png

        # lets grab the pixel val we should expect for this image.
        pixel_val = int(image_name.split(".")[0])
        with Image.open(TEST_IMAGE_PATH + image_name) as img:
            # process image as grayscale so we only get back one RGB value
            img = img.convert('L')
            width, height = img.size
            for y in range(height):
                for x in range(width):
                    expected_pixel_val = img.getpixel((x,y))
                    # all these values should be the same and they should equal
                    # the same value as their names imply
                    assert expected_pixel_val == pixel_val