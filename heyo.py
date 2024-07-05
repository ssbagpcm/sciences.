import os
from groq import Groq

client = Groq( 
    api_key=os.environ.get("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"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)