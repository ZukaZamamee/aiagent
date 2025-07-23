import os
from google.genai import types # type: ignore

def get_files_info(working_directory, directory="."):
    #directory is outside the working directory
    full_directory_path = os.path.join(working_directory, directory)
    abs_directory_path = os.path.abspath(full_directory_path)
    abs_working_directory_path = os.path.abspath(working_directory)

    if not abs_directory_path.startswith(abs_working_directory_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    #check if directory is not a directory
    if not os.path.isdir(abs_directory_path):
        return f'Error: "{directory}" is not a directory'
    
    try:
        dir_contents = os.listdir(abs_directory_path)

        dir_contents_string_list = []
        for content in dir_contents:
            content_path = os.path.join(abs_directory_path, content)
            content_size = os.path.getsize(content_path)
            content_is_dir = os.path.isdir(content_path)
            content_string = " - " + content + ": file_size=" + str(content_size) + " bytes, is_dir=" + str(content_is_dir)
            dir_contents_string_list.append(content_string)
        return "\n".join(dir_contents_string_list)
    except:
        return f"Error: something went wrong"
    
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

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)