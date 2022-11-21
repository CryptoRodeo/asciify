import pytest

@pytest.fixture
def expected_char_for_image():
    """Returns the expected character for the file we're testing

    Returns:
        Dictionary[string] -> string: Dictionary where the key is the file name 
        and the value is the expected character
    """
    return {
        '162.png': ' . ',
        '255.png': '   ',
        '50.png': ' • ',
        '123.png': ' * ',
        '0.png': ' • ',
        '87.png': ' • ',
        '209.png': ' - '
    }