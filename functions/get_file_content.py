import os
from google.genai import types
from config import MAX_CHARS

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Return a string representing the contents of a file given the relative file path, truncates to {MAX_CHARS} characters, constrained to the working directory.",
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
    abs_working_directory = os.path.abspath(working_directory)
    tgt_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not tgt_file_path.startswith(abs_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(tgt_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(tgt_file_path, "r") as f:
            file_content = f.read(MAX_CHARS + 1)
            if len(file_content) > MAX_CHARS:
                file_content = file_content[:-1] + '[...File "{file_path}" truncated at 10000 characters]'
            return file_content
    except Exception as err:
        return f'Error reading file "{file_path}": {err}'
