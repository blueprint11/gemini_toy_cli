import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from prompts import system_prompt
from call_function import available_functions
def main():

    if len(sys.argv) < 2:
        print("error: no prompt given!")
        sys.exit(1)
    elif len(sys.argv) == 2 or 3:
        prompt = sys.argv[1]
    
    else:
        print("error: need to provide prompt in double braces")
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I fix the calculator?"')
        sys.exit(1)

    

    messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]
    
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    
    
    client = genai.Client(api_key=api_key)
    print("Hello from toyccai!")
    response = client.models.generate_content(
                model='gemini-2.0-flash-001', 
                contents=messages,
                config=types.GenerateContentConfig(
                tools=[available_functions],system_instruction=system_prompt
                ),
    )
    if not response.function_calls:
        return response.text

    for function_call_part in response.function_calls:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")

    if len(sys.argv)==3 and sys.argv[2]=="--verbose":
        prompt =sys.argv[1]
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
