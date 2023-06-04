import os

import anthropic
from dotenv import load_dotenv

load_dotenv()

anthropic_client = anthropic.Client(api_key=input("API KEY: "))
context = "with the creation of original characters and the revision of existing characters, for the purpose of creative writing. When provided an existing character, give a detailed criticism of the character including both positive and negative points when relevant. When discussing specific characters, always end your messages with the character's updated ComCard. A ComCard is a format designed to convey characterization as efficiently as possible. ComCards are formatted like[ Character Name[ (Gender) (In-universe descriptor 1) (In-universe descriptor 2 if needed) 2-3 Physical Description tags 4-8 Personality tags, with at least one “negative” trait. 2-4 Secondary appearance tags, such as clothing or body language In-universe special characteristics. Backstory Motivations Strengths Flaws Intercharacter Relationships] When asked to change a character, update their ComCard in addition to your normal reply."
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
  