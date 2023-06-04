import os

import anthropic
from dotenv import load_dotenv

load_dotenv()

anthropic_client = anthropic.Client(api_key=input("API KEY: "))
context = "Help with the creation of original worlds and narrative concepts, and the revision of existing concepts, for the purpose of creative writing. Your end result will be a concise and detailed description of the concept. When provided an existing concept, give a detailed criticism of the concept including both positive and negative points when relevant. When discussing specific concepts, always end your messages with the concept's updated ComCard. A ComCard is a format designed to convey concepts as efficiently as possible. ComCards are formatted like[ Concept Name[ A concise and detailed description Additional aspects separated by newlines Use as many categories as is appropriate. ] When asked to change a concept, update their ComCard in addition to your normal reply."
while True:
    user_inp = input("I am Flint , the Muse of Worlds. Tell me about your world, and together we will fill it with life.: ")

    current_inp = anthropic.HUMAN_PROMPT + user_inp + anthropic.AI_PROMPT
    context += current_inp

    prompt = context

    completion = anthropic_client.completion(
        prompt=prompt, model="claude-v1.3-100k", max_tokens_to_sample=1000
    )["completion"]

    context += completion

    print("Anthropic: " + completion)
  