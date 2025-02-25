# Importações

from dotenv import load_dotenv
from openai import OpenAI
import os

# Carregando variáveis .env
load_dotenv()
api_key = os.getenv("API_KEY")

# Create OpenAI Client
client = OpenAI(api_key=api_key)
response = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
        {"role": "user", "content": "Meu marido, Vitor, esta me traindo?"}
    ]
)

print(response.choices[0].message.content)

