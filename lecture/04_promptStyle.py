'''
so right now we are just simply talking to llm by passing the prompt with role and content but we do have diff style of prompting like 
- ALPECA style prompt
- CHATML (we use this )
- INST prompt 


Alpaca-style data is usually formatted as simple, single-turn instructions and outputs, often like:

### Instruction:
Write a poem about the sea.

### Response:
The sea is blue, vast and grand...

'''
# in this we use the ### and then it will start to predict the next token after that so it will give the response accordingly

# Currently we are using the CHATML prompt style to make the prompt more structured and formatted

{
    "role":"system"|"user"|"assistant",
    "content":"string"
}

# this is called the chatML prompt style where we have the roles of the messages defined and then the content of the messages defined so that the model can understand the context of the conversation and give the response accordingly.