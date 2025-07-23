import os
import subprocess
from config import MAX_RUN_TIME
from google.genai import types # type: ignore

def run_python_file(working_directory, file_path, args=[]):
    full_file_path = os.path.join(working_directory, file_path)
    abs_file_path = os.path.abspath(full_file_path)
    abs_working_directory_path = os.path.abspath(working_directory)
    if not abs_file_path.startswith(abs_working_directory_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    
    if not file_path.split(".")[-1] == "py":
        return f'Error: "{file_path}" is not a Python file.'

    try:    
        subprocess_args = ["python", abs_file_path,] +  args
        completed_process = subprocess.run(
            subprocess_args,
            capture_output=True,
            timeout=MAX_RUN_TIME,
            cwd=abs_working_directory_path,
            text=True
            )
        
        if len(completed_process.stdout) == 0 and len(completed_process.stderr) == 0:
            return "No output produced"
        else:
            completed_process_stdout = f"STDOUT: {completed_process.stdout}"
            completed_process_stderr = f"STDERR: {completed_process.stderr}"
            stdout_stderr_result = f"{completed_process_stdout}\n{completed_process_stderr}\n"
        
        completed_process_returncode = completed_process.returncode
        returncode_error = ""
        if not completed_process_returncode == 0:
            returncode_error =  f"Process exited with code {completed_process_returncode}\n"
        
        return stdout_stderr_result + returncode_error

    except Exception as e:
        return f"Error: executing Python file: {e}"
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs the python file at the specified file path, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of a python file to run, relative to the working directory. If not provided or not a python file, returns an error",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Optional arguments for the specified python file",
                items=types.Schema(
                    type=types.Type.STRING,
                ),
            ),
        },
    ),
)