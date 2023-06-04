import os

import anthropic
from dotenv import load_dotenv

load_dotenv()

anthropic_client = anthropic.Client(api_key=input("API KEY: "))
context = "Using the following world info and any story outlines or feedback given, write a detailed, complex, compelling, and stylish chapter of a contemporary novel. Each chapter should be about 2000 words. Worldinfo:"
while True:
    user_inp = input("I am Eithne, the Muse of Inkwells. Show me your story, and I shall write you a masterpiece.: ")

    current_inp = anthropic.HUMAN_PROMPT + user_inp + anthropic.AI_PROMPT
    context += current_inp

    prompt = context

    completion = anthropic_client.completion(
        prompt=prompt, model="claude-v1.3-100k", max_tokens_to_sample=1000
    )["completion"]

    context += completion

    print("Anthropic: " + completion)
  