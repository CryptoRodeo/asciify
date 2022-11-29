import pytest

from asciify.helpers.map_processor import MapProcessor

def test_throws_exception_if_image_map_doesnt_exist():
    with pytest.raises(Exception) as e_info:
        MapProcessor("invalid_file.json")
