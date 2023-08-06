# VerisPTab

## Description
VerisPTab is a Python package that generates a "private duplicate" of a given table, obfuscating any potential Personally Identifiable Information (PII) in the process. 

## Installation
VerisPTab can be installed via pip:

```bash
pip install verisptab
```

After installation, you can import the `generate` function and use it as follows:

```python
from verisptab import generate

new_df = generate.generate("path_to_the_original_table")
```

This will create a new dataframe `new_df` that is a "private" version of the original table.

## Troubleshooting and Known Issues
This section will be updated as new issues are identified and solutions or workarounds are developed.

## License
VerisPTab is open source and free for use. Please use responsibly and respect the privacy of all individuals. 
