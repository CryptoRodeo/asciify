from converters.ascii_converter import AsciiConverter


def run(file_name, shrink_ratio, character_map, output_file):
    try:
        AsciiConverter(
            file_name=file_name,
            shrink_ratio=shrink_ratio,
            character_map=character_map,
            output_file=output_file
        ).run()
    except Exception as e:
        print(e)

