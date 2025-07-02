import os
from google.genai import types
import subprocess

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute a python file  constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
            "args": types.Schema(
                type=types.Type.STRING,
                description="Arguments for whatever python file.",
            ),
        },
    ),
)

def run_python_file(working_directory, file_path, args=None):
    abs_working_directory = os.path.abspath(working_directory)
    tgt_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not tgt_file_path.startswith(abs_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working direction'
    if not os.path.exists(tgt_file_path):
        return f'Error: File "{file_path}" not found.'

    if not file_path[-3:] == ".py":
        return f'Error: "{file_path}" is not a Python file.'

    try:
        command = ["python", tgt_file_path]
        if args:
            command.extend(args)
        process = subprocess.run(command, timeout=30, capture_output=True, text=True, cwd=abs_working_directory)
        result = []
        if process.stdout:
            result.append(f"STDOUT: {process.stdout}\n")
        if process.stderr:
            result.append(f"STDERR: {process.stderr}")
        if process.returncode != 0:
            result.append(f"Process exited with code {process.returncode}\n")
        
        return "\n".join(result) if result else "No output produced."

    except Exception as e:
        return f"Error: executing Python file: {e}"
