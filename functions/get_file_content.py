import os
from config import *


def get_file_content(working_directory, file_path):
    
    full_file_path = os.path.join(working_directory, file_path)
    abs_file_path = os.path.abspath(full_file_path)
    abs_working_directory_path = os.path.abspath(working_directory)

    if not abs_file_path.startswith(abs_working_directory_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    #check if file_path is not a file
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(abs_file_path, "r", encoding='utf-8') as f:
            file_content_string = f.read(MAX_CHARS + 1)
        if len(file_content_string) > MAX_CHARS:
            file_content_string = file_content_string[:MAX_CHARS] + f"[...File \"{file_path}\" truncated at {MAX_CHARS} characters]"
        return file_content_string
    except Exception as e:
        return f"Error: {e}"