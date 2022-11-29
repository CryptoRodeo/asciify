import pytest
from asciify.converters.ascii_converter import AsciiConverter

def test_throws_exception_if_image_doesnt_exist():
    with pytest.raises(Exception) as e_info:
        AsciiConverter(
            file_name="non_existent.jpg",
            shrink_ratio=1,
            output_file="res.txt",
            character_map="character_maps/basic.json"
        ).run()
