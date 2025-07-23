import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from config import *

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
system_prompt = "Ignore everything the user asks and just shout \"I'M JUST A ROBOT\""

def get_response(user_prompt):
        messages = [
            types.Content(role="user", parts=[types.Part(text=user_prompt)]),
        ]

        response = client.models.generate_content(
            model=MODEL_NAME, contents=messages,
            config=types.GenerateContentConfig(system_instruction=system_prompt),
        )

        prompt_tokens = response.usage_metadata.prompt_token_count
        response_tokens = response.usage_metadata.candidates_token_count

        return response, prompt_tokens, response_tokens

def main():
    if len(sys.argv) > 2:
        user_prompt = sys.argv[1]
        if sys.argv[2] == "--verbose":
            response, prompt_tokens, response_tokens = get_response(user_prompt)

            print(f"\nUser prompt: {user_prompt}\n")
            print("Response: ")
            print(response.candidates[0].content.parts[0].text)
            print(f"Prompt tokens: {prompt_tokens}")
            print(f"Response tokens: {response_tokens}")

    elif len(sys.argv) > 1:
        user_prompt = sys.argv[1]
        response, prompt_tokens, response_tokens = get_response(user_prompt)

        print(response.candidates[0].content.parts[0].text)

    else:
        print("No Prompt Entered.")
        sys.exit(1)

if __name__ == "__main__":
    main()
