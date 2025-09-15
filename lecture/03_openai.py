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
# passing the context to the model that what he is and what to do so that it can give the best response
        {"role": "system", "content": "you are an expert python programmer. write a python function to calculate factorial of a number. Give me the. response in the form of JSON only. The JSON should have two keys function and explanation. function key will have the python function as the value and explanation key will have the explanation of the function as the value. Do not include any text other than the JSON in your response."},

        # user prompt that what the user wants
        {"role": "user", "content": "write the function for factorial"},
    ]
)

airesponse=(response.choices[0].message.content)

print(airesponse)

