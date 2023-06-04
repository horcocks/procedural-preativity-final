import os

import anthropic
from dotenv import load_dotenv

load_dotenv()

anthropic_client = anthropic.Client(api_key=input("API KEY: "))
context = "Help with the creation of detailed story outlines following a 27-chapter format. The story is broken up into three acts. Each act has three arcs usually consisting of a setup, journey or examination, and payoff. Each arc is divided into three story beats. Each story beat is detailed enough to generate roughly ten pages of a novel. The world info is:"
while True:
    user_inp = input("I am T'Sha, the Muse of Fable. Tell me about your story, and together we will make it sing.: ")

    current_inp = anthropic.HUMAN_PROMPT + user_inp + anthropic.AI_PROMPT
    context += current_inp

    prompt = context

    completion = anthropic_client.completion(
        prompt=prompt, model="claude-v1.3-100k", max_tokens_to_sample=1000
    )["completion"]

    context += completion

    print("Anthropic: " + completion)
  