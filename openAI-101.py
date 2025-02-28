# Importações
from dotenv import load_dotenv
from openai import OpenAI
import os

# Carregando variáveis .env
load_dotenv()
api_key = os.getenv("API_KEY")

# Create OpenAI Client
client = OpenAI(api_key=api_key)

messages = [{"role": "system", "content": "You are a helpful math tutor."}]
user_msgs = ["Explain what pi is.", "Summarize this in two bullet points."]

for q in user_msgs:
    # print("User: ", q)

    # Create a dictionary for the user message from q and append to messages
    user_dict = {"role":"user", "content": q}
    messages.append(user_dict)

    # Create de API request
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages=messages,
        max_tokens=100
    )

    # Convert the assistant's message to a dict and append to message
    assistant_dict = {
        "role": "assistant",
        "content": response.choices[0].message.content
    }

    messages.append(assistant_dict)
    print("Assistant: ", response.choices[0].message.content, "\n")

print(messages)
