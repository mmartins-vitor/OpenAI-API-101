# Importações
from dotenv import load_dotenv
from openai import OpenAI
import os

# Carregando variáveis .env
load_dotenv()
api_key = os.getenv("API_KEY")

prompt="""Replace car with plane and adjust phrase: A car is a vehicle that is typically 
powered by an internal combustion engine or an electric motor. It has four wheels, and is 
designed to carry passengers and/or cargo on roads or highways. Cars have become a ubiquitous 
part of modern society, and are used for a wide variety of purposes, such as commuting, travel, 
and transportation of goods. Cars are often associated with freedom, independence, and mobility."""

# Create OpenAI Client
client = OpenAI(api_key=api_key)
response = client.chat.completions.create(
    model="gpt-4o-mini",
    #store=True,
    messages=[
        {"role": "system",
        "content": "You are a helpful data science tutor."},
        {"role": "user",
        "content": "Qual é a diferença entre um loop for e um loop while?"}
        ],

    max_tokens=100,
    temperature=0
)

# 
print(response.choices[0].message.content)

