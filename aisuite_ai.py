import os
import aisuite as ai
client = ai.Client()


os.environ['GROQ_API_KEY'] = "gsk..."
os.environ['OPENAI_API_KEY']="sk.."


models = ["openai:gpt-4o", "groq:llama3-groq-8b-8192-tool-use-preview"]

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
