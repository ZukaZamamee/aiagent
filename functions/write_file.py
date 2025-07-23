import os
from google.genai import types # type: ignore

def write_file(working_directory, file_path, content):
     
    full_file_path = os.path.join(working_directory, file_path)
    abs_file_path = os.path.abspath(full_file_path)
    abs_working_directory_path = os.path.abspath(working_directory)

    if not abs_file_path.startswith(abs_working_directory_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    #check if file_path exists
    try:
        file_dir = os.path.dirname(abs_file_path)
        os.makedirs(file_dir, exist_ok=True)

        with open(abs_file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to the file at the specified file path, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of a file to write to, relative to the working directory. If not provided, creates the file at the specified file path",
            ),
           "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the specified file",
            ), 
        },
    ),
)