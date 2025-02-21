from openai import OpenAI

# Create OpenAI Client
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o",
    store=True,
    messages=[
        {"role": "user", "content": "write a haiku about ai"}
    ]
)

print(response.choices[0].message.content)