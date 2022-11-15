from converters.ascii_converter import AsciiConverter
from helpers.map_processor import MapProcessor


def run(file_name, shrink_ratio, output_file):
    try:
        AsciiConverter(
            file_name=file_name,
            shrink_ratio=shrink_ratio,
            output_file=output_file
        ).run()
        MapProcessor().test()
    except Exception as e:
        print(e)

