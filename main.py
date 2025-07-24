import os
import time
from dotenv import load_dotenv # type: ignore
from google import genai
import sys
from google.genai import types # type: ignore
from config import *
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from functions.call_function import call_function


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

system_prompt = """
IMPORTANT: Always start by using tools immediately. Never explain your plan first.
You are an AI coding agent. When asked a question, immediately use tools to find the answer.

Available tools:
- get_files_info: List files and directories
- get_file_content: Read file contents  
- run_python_file: Execute Python files
- write_file: Write or overwrite files

START WITH ACTION. Do not explain what you will do - just do it.

Example: If asked about a calculator, immediately call get_files_info to see the project structure, then read relevant files.
"""
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file,
    ]
)

def get_response(messages):
        response = client.models.generate_content(
            model=MODEL_NAME, contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions], system_instruction=system_prompt
            ),
        )

        prompt_tokens = response.usage_metadata.prompt_token_count
        response_tokens = response.usage_metadata.candidates_token_count

        return response, prompt_tokens, response_tokens

def main():
    if len(sys.argv) > 1:
        user_prompt = sys.argv[1]
        verbose = "--verbose" in sys.argv
        messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]

        for step in range(20):
            try:
                response, prompt_tokens, response_tokens = get_response(messages)
                model_message = response.candidates[0].content
                messages.append(model_message)

                if verbose:
                    print(f"\nUser prompt: {user_prompt}\n")
                    print(f"Prompt tokens: {prompt_tokens}")
                    print(f"Response tokens: {response_tokens}")

                found_function_call = False
                text_found = False 
                for part in model_message.parts:
                    for part in model_message.parts:
                        #print(f"Part type: {type(part)}, has function_call: {hasattr(part, 'function_call')}, function_call value: {getattr(part, 'function_call', 'N/A')}")
                        if part.function_call and part.function_call.name:
                            function_call = part.function_call
                            try:
                                function_call_result = call_function(function_call, verbose)
                                print(f"Function result: {function_call_result}")  # Add this debug line
                            except Exception as tool_err:
                                print(f"Function call failed: {tool_err}")
                                return
                            
                            messages.append(function_call_result)
                            found_function_call = True

                            print(f"- Calling function: {function_call.name}")
                            break
                
                        elif part.text:
                            print("\nFinal response:")
                            print(part.text)
                            text_found = True
                            return
                    
                if text_found:
                    return
                    
                if not found_function_call:
                    break
                time.sleep(0.5)

            except Exception as err:
                print(f"Error during agent iteration: {err}")
                break
    else:
        print("No Prompt Entered.")
        sys.exit(1)

if __name__ == "__main__":
    main()
