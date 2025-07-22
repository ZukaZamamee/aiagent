import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def get_response(user_prompt):
        messages = [
            types.Content(role="user", parts=[types.Part(text=user_prompt)]),
        ]

        response = client.models.generate_content(
            model='gemini-2.0-flash-001', contents=messages,
        )

        prompt_tokens = response.usage_metadata.prompt_token_count
        response_tokens = response.usage_metadata.candidates_token_count

        return response, prompt_tokens, response_tokens

def main():
    if len(sys.argv) > 2:
        user_prompt = sys.argv[1]
        if sys.argv[2] == "--verbose":
            response, prompt_tokens, response_tokens = get_response(user_prompt)

            print(f"User prompt: {user_prompt}")
            print(response)
            print(f"Prompt tokens: {prompt_tokens}")
            print(f"Response tokens: {response_tokens}")

    elif len(sys.argv) > 1:
        user_prompt = sys.argv[1]
        response, prompt_tokens, response_tokens = get_response(user_prompt)

        print(response)

    else:
        print("No Prompt Entered.")
        sys.exit(1)

if __name__ == "__main__":
    main()
