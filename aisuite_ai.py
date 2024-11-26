from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access your API keys
openai_api_key = os.getenv("OPENAI_API_KEY")
# anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

import aisuite as ai
client = ai.Client()

models = ["groq:grok-beta"]

messages = [
    {"role": "system", "content": "Respond in Pirate English."},
    {"role": "user", "content": "Tell me a joke."},
]

for model in models:
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.75
    )
    print(response.choices[0].message.content)

