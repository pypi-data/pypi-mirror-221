# GECK (Garden of Eden Creation Kit)

GECK is a Python library and Bash tool for interacting with STC programmatically.
It allows to startup embedded Summa instance, do search queries and iterate over database.

## Install

```bash
pip install stc-geck
```

## Examples

### CLI

```bash
# Iterate over all stored documents
geck --ipfs-http-base-url 127.0.0.1:8080 - documents

# Do a match search by field
geck --ipfs-http-base-url 127.0.0.1:8080 - search doi:10.3384/ecp1392a41

# Do a match search by word
geck --ipfs-http-base-url 127.0.0.1:8080 - search hemoglobin --limit 10
```

### Python

Examples for Python can be found in [examples directory](/geck/examples/search-stc.ipynb)
