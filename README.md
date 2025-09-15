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

using the best prompt , we can fine tune the ai model that how it will respond to the user query and what not to respond to the user query.