# html-content-extractor

This Python package provides a function to extract the "main content" from HTML documents.

## Installation

You can install this package via pip:

```sh
pip install html-content-extractor

```

## Usage

```python
from html_content_extractor import extract_content

>>> html = "<div><h1>An HTML Page</h1><p>This is some HTML content.</p></div>"
>>> content = extract_content(html, format='plaintext')
>>> print(content)
"An HTML Page\n\nThis is some HTML content."

>>> markdown = extract_content(html, format='markdown')
>>> print(content)
"# An HTML Page\n\nThis is some HTML content."
```
