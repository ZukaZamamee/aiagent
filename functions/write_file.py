import os

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