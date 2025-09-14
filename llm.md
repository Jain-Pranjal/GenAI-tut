
LLM is called the Large Language Model. These model are trained on a large corpus of text data to understand and **generate human-like text**. They can perform various natural language processing tasks, such as text generation, translation, summarization, and question-answering.

yeha jitne bhi humare pass llm hai vo sare ke sare transformer architecture pe based hai. 
GPT= Generative Pre-trained Transformer and all these text based models are based on transformer architecture that is generative in nature and pre-trained on large corpus of text data.

Chatgpt is the chatbot interface that is usingt the GPT model to generate human-like text based on the input provided by the user.

These LLm model are pre trained to understand the human language and generate text in the format that humans can understand.

- Generative : these models can generate text based on the input provided to them. They are actully generating new text based on the patterns and structures they have learned during their training.
- Pre-trained : these models are pre-trained on a large corpus of text data, which allows them to understand the patterns and structures of human language. This pre-training helps the models to generate text that is coherent and contextually relevant.
- Transformer : this is the reality behind all these models. 

in short 
```bash 
All the llm model like gpt , gemini , claude  etc all are transformer that are generative in nature and pre-trained on large corpus of text data.

At the end , all the LLM are just transformer models that are generative in nature and pre-trained on large corpus of text data.
```

The Gpt bascially uses the transformer architecture that takes the input tokens and just <mark> **predict the next token**</mark> based on the input tokens provided to it.
![GPT Transformer Architecture](/images/GPT_transformer.png)

### The Gpt or the other text based model are predicting the next token based on the input tokens provided to it.(ONLY THE TEXT GENNERATIVE MODELS) and it will go loop and loop until it reach the max token limit or the end token is reached.
```
basically llm (text based model) aapke lie next token ko predict kargee loop wise matlab ke jaise jaise ek output ka new token mielga vo usko firse input me daal ke next token ko predict kargee and this will go on until the max token limit is reached or the end token is reached.
```
```
WORKING OF GPT MODEL
✅ In short the llm model is using the transformer that us just predict the next token based on the input tokens provided to it. so yeah sare aapke text based model like gpt , gemini , claude  etc all are transformer that are generative in nature and pre-trained on large corpus of text data.
Thats why they are cpu intensive task as we are just looping again and again with the input and output tokens to predict the next token.
```

## TOKENS
so basciaily the character or the symbol , they are mapped to the number and all thre mdoel follow the diff token system as computer are very well understanding the numbers rather than the characters. so it will just map the characters to the numbers and then it will process the numbers rather than the characters and the predict the next token based on the input tokens provided to it.

These number will sent to the transformer and the transformer will predict the next token and the we detokenize the number to the characters and then we will get the output in the form of characters.

![Tokenization and Detokenization](/images/tokenization.png)
