# Veris-Priv-Tab

## Description
Veris-Priv-Tab is a Python package that generates a "private duplicate" of a given table, obfuscating any potential Personally Identifiable Information (PII) in the process. 

## Installation
Veris-Priv-Tab can be installed via pip:

```bash
pip install veris-priv-tab
```

After installation, you can import the `generate` function and use it as follows:

```python
from veris_priv_tab import generate

new_df = generate("path_to_the_original_table")
```

This will create a new dataframe `new_df` that is a "private" version of the original table.

## Troubleshooting and Known Issues
This section will be updated as new issues are identified and solutions or workarounds are developed.

## License
Veris-Priv-Tab is open source and free for use. Please use responsibly and respect the privacy of all individuals. 