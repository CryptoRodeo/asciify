import pytest
from pathlib import Path

TEST_IMAGE_PATH = "tests/test_images/"

@pytest.fixture
def image_names():
    """Get the names of the image file's we'll need for testing

    Returns:
        List[string]: name of image file names
    """
    source_dir = Path(TEST_IMAGE_PATH)
    files = source_dir.iterdir()
    file_names = []
    for file in files:
        file_names.append(file.name)

    return file_names

