from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv() # take environment variables from .env.

# creating the client
client = OpenAI(
    api_key="AIzaSyDdxr0eyziHjTrd27FBN0tRlKKlgUba9gw",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
) 
# now it will redirect the request to the google gemini model server still using the same openai library syntax


SYSTEM_PROMPT = '''you are an expert python programmer. write a python function to calculate factorial of a number. Give me the. response in the form of JSON only. The JSON should have two keys function and explanation. function key will have the python function as the value and explanation key will have the explanation of the function as the value. Do not include any text other than the JSON in your response.


example output response:
eg : {
    "function": "def factorial(n):\n    if n == 0 or n == 1:\n        return 1\n    else:\n        return n * factorial(n - 1)",
    "explanation": "This function calculates the factorial of a given number n using recursion. If n is 0 or 1, it returns 1. For any other positive integer, it multiplies n by the factorial of (n-1)."
}

eg: {
    "function": "def factorial(n):\n    result = 1\n    for i in range(2, n + 1):\n        result *= i\n    return result",
    "explanation": "This function calculates the factorial of a given number n using an iterative approach. It initializes a result variable to 1 and then multiplies it by each integer from 2 to n. Finally, it returns the computed factorial."
}


'''

response = client.chat.completions.create(
    model="gemini-2.0-flash",
    messages=[
# passing the context to the model that what he is and what to do so that it can give the best response
        {"role": "system", "content": SYSTEM_PROMPT},

        # user prompt that what the user wants
        {"role": "user", "content": "write the function for fibonacci series"},
    ]
)

airesponse=(response.choices[0].message.content)
print(airesponse)


# 0 shot prompt - direct instruction is given to the model with no example
# few shot prompt - few examples are given along with the instruction to the model so that it can understand the pattern and then give the response accordingly
# chain of thought prompt - the model is guided to think step by step
