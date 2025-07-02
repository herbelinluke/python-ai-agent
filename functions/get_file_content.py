import os
from google.genai import types
MAX_CHARS = 10000

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Return a string representing the contents of a file given the relative file path, truncates to 10000 characters, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to the file to read from, relative to the working directory. Required for the function.",
            ),
        },
    ),
)

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
