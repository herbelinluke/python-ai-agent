import os

def write_file(working_directory, file_path, content):
    try:
        abs_working_directory = os.path.abspath(working_directory)
        tgt_file_path = os.path.abspath(os.path.join(working_directory, file_path))

        if not tgt_file_path.startswith(abs_working_directory):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.exists(os.path.dirname(tgt_file_path)):
            os.makedirs(os.path.dirname(tgt_file_path))
        
        with open(tgt_file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as err:
        return f'Error: {err}'

