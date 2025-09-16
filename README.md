# GenAI-tut
This repository contains tutorials and resources related to Generative AI. It includes code examples, datasets, and documentation to help users understand and implement generative AI models.

To make the venv
```bash
python3 -m venv ./venv
source ./venv/bin/activate
pip install -r requirements.txt
```

Making the venv using the <mark>**uv**</mark> 
```bash
pip install uv (already installed)
uv venv 
source .venv/bin/activate
uv pip install requests

```

- package is the collection of all the code files that is called module
so when we import a package all the code files inside that package is imported 
but if we use the 
```python
from package import module

# this will import only the specific module from the package
```
 
## prompts
Giving the right prompt can basically increase the performance of the model and accuracy of giving the response. by prompt only we can change the behaviour of the model that in what basis we need to give the response.
we have various types of prompts
1. zero shot prompt - no context is given to the model (direct instruction given ke do the work)
2. one shot prompt - one example is given to the model 
3. few shot prompt - few examples are given to the model
4. chain of thought prompt - the model is guided to think step by step
5. persona based prompt - the model is given a specific persona to follow while giving the response

using the best prompt , we can fine tune the ai model that how it will respond to the user query and what not to respond to the user query. We can make the output resposne more structured and formatted using the prompt only.

## running the model via docker 
we can pull the image of the ollama and open-web UI for the ui interface to interact with the ollma and using þhe various model 
[link](https://docs.openwebui.com/getting-started/quick-start/)
by this we can run the UI interface of the ollama 



So we have the new CLI command docker-model that enables us to run the model via docker , no need to use the ollama 
[link](https://docs.docker.com/ai/model-runner/get-started/#enable-docker-model-runner)


## hugging face 
we can also run the model via hugging face using the **transformers** library . using hugging face we can run the model locally on our machine without any api calls and no need to use the openai or any other api key.
Just we need to setup the transformwer library and then we can run the model locally on our machine.
for the model to use we can use the CLI commannd and also we need to pass the token whcih we can get from the hugging face website by creating an account. ACCESS TOKENN 
[link](https://huggingface.co/docs/huggingface_hub/en/guides/cli)

```bash