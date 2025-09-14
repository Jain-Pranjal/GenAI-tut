import tiktoken

enc1=tiktoken.encoding_for_model("gpt-3.5-turbo")
enc2=tiktoken.encoding_for_model("gpt-4o")
print(enc1.encode("Hello World!"))
print(enc2.encode("Hello World!"))

# so the model has its own tokenizer and all the model have their own tokenizers

# Also detokenization is also possible
print(enc2.decode([13225, 5922, 0]))

# so basically these tokens are passed to the transformer and then transformer just predicts the next token based on the previous tokens and then it generates the text and then give the detokenized text as the output