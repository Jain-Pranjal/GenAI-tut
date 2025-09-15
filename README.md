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