import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

def get_files_info(working_directory, directory=None):
    try:
        abs_working_directory = os.path.abspath(working_directory)
        abs_directory = os.path.abspath(os.path.join(working_directory, directory))
        if not abs_directory.startswith(abs_working_directory):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        elif not os.path.isdir(abs_directory):
            return f'Error: "{directory}" is not a directory'
        else:
            dir = os.listdir(abs_directory)
            result = []
            for path in dir:
                abs_path = os.path.join(abs_directory, path)
                result.append(f"- {path}: file_syze={os.path.getsize(abs_path)} bytes, is_dir={not os.path.isfile(abs_path)}")
            return "\n".join(result)
    except Exception as e:
        return f"Error: {e}."
