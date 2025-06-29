import os
MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    try:
        abs_working_directory = os.path.abspath(working_directory)
        tgt_file_path = os.path.abspath(os.path.join(working_directory, file_path))
        if not tgt_file_path.startswith(abs_working_directory):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        elif not os.path.isfile(tgt_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        else:
            with open(tgt_file_path, "r") as f:
                file_content_string = f.read(MAX_CHARS + 1)
            if len(file_content_string) > MAX_CHARS:
                return file_content_string[:-1] + '[...File "{file_path}" truncated at 10000 characters]'
            else:
                return file_content_string
    except Exception as err:
        return f'Error: {err}'
