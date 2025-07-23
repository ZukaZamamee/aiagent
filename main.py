import os
from dotenv import load_dotenv # type: ignore
from google import genai
import sys
from google.genai import types # type: ignore
from config import *
from functions.get_files_info import schema_get_files_info, available_functions

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""


def get_response(user_prompt):
        messages = [
            types.Content(role="user", parts=[types.Part(text=user_prompt)]),
        ]

        response = client.models.generate_content(
            model=MODEL_NAME, contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions], system_instruction=system_prompt
            ),
        )

        prompt_tokens = response.usage_metadata.prompt_token_count
        response_tokens = response.usage_metadata.candidates_token_count

        for part in response.candidates[0].content.parts:
            if hasattr(part, 'function_call'):
                function_call = part.function_call
                print(f"Calling function: {function_call.name}({function_call.args})")
            elif hasattr(part, 'text') and part.text:
                print(part.text)

        return response, prompt_tokens, response_tokens

def main():
    if len(sys.argv) > 2:
        user_prompt = sys.argv[1]
        if sys.argv[2] == "--verbose":
            response, prompt_tokens, response_tokens = get_response(user_prompt)

            print(f"\nUser prompt: {user_prompt}\n")
            print(f"Prompt tokens: {prompt_tokens}")
            print(f"Response tokens: {response_tokens}")

    elif len(sys.argv) > 1:
        user_prompt = sys.argv[1]
        response, prompt_tokens, response_tokens = get_response(user_prompt)

    else:
        print("No Prompt Entered.")
        sys.exit(1)

if __name__ == "__main__":
    main()
