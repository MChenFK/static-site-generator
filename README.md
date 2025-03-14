# static-site-generator
- The static site generator generates a static site similar to Jekyll, Hugo, or Gatsby using python
- The generator converts markdown files from placed in the content folder to html files viewable on the host and port localhost:8888
- Content can contain subdirectories

## Steps to use:
1. Place markdown files / directories for markdown files in content folder
2. Run ./main.sh
3. Open http://localhost:8888

## content
Contains markdown files and directories of markdown files to be converted to html in local public folder

## static
Contains static website to generate local public directory

## src
### textnode.py
Generates textnodes in Markdown given raw text and a text type
Accepts:
- text
- bold
- italic
- code
- image
- link

### test_textnode.py
Contains all test cases related to textnodes and conversions from Markdown to textnodes

### htmlnode.py
Contains classes htmlnode, leafnode, and parentnode

### test_htmlnode.py
Contains all test cases related to htmlnodes, leafnodes, and parentnodes

### inline_markdown.py
Splits markdown into corresponding textnodes for text types

### test_inline_markdown.py
Test cases for inline_markdown.py

### markdown_blocks.py
Converts markdown to corresponding blocks

### test_markdown_blocks.py
Test cases for markdown_blocks.py

### generate_page.py

### test_generate_page.py

