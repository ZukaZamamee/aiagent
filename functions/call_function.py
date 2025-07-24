import os
from google.genai import types # type: ignore
from .get_file_content import get_file_content
from .get_files_info import get_files_info
from .run_python_file import run_python_file
from .write_file import write_file

def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    function_call_part.args.update(working_directory="./calculator")

    match function_call_part.name:
        case "get_file_content":
            function_result = get_file_content(**function_call_part.args)
        case "get_files_info":
            function_result = get_files_info(**function_call_part.args)
        case "run_python_file":
            function_result = run_python_file(**function_call_part.args)
        case "write_file":
            function_result = write_file(**function_call_part.args)
        case _:
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_call_part.name,
                        response={"error": f"Unknown function: {function_call_part.name}"},
                    )
                ],
            )
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,
                response={"result": function_result},
            )
        ],
    )  