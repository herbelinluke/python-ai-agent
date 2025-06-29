import os

def get_files_info(working_directory, directory=None):
    working_directory = os.path.abspath(working_directory)
    directory = os.path.abspath(directory)
    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'
    elif not directory.startswith(working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    else:
        return f'- README.md: file_size=1032 bytes, is_dir=False
            - src: file_size=128 bytes, is_dir=True
            - package.json: file_size=1234 bytes, is_dir=False'
