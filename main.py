import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
def main():

    if len(sys.argv) < 2:
        print("error: no prompt given!")
        sys.exit(1)
    elif len(sys.argv) == 2 or 3:
        prompt = sys.argv[1]
    
    else:
        print("error: need to provide prompt in double braces")
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
    contents=messages
    )
    print(response.text)
    if len(sys.argv)==3 and sys.argv[2]=="--verbose":
        prompt =sys.argv[1]
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
