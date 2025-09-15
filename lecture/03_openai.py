from openai import OpenAI
from dotenv import load_dotenv

load_dotenv() # take environment variables from .env.

# creating the client
client = OpenAI(
    api_key="AIzaSyDdxr0eyziHjTrd27FBN0tRlKKlgUba9gw",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
) 
# now it will redirect the request to the google gemini model server still using the same openai library syntax


response = client.chat.completions.create(
    model="gemini-2.0-flash",
    messages=[
        {"role": "user", 
         "content": "Write a one-sentence bedtime story about a unicorn."}
    ]
)

print(response.choices[0].message.content)
# so now humab direclrty tapne agents ko bana skte hai using ht eurnner just run command se usne ahe
