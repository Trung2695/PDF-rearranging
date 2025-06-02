# PDF-rearranging
To reorder the pdfs when you can only scan 1 side in bulk and your paperwork is double sided (or for worse situations)

This code requires the [pypdf package](https://pypdf.readthedocs.io/en/stable/user/installation.html)

In the terminal `pip install pypdf`

The package, in turn, requires Python 3.8+

The program works by receiving user input on the order of the pages (pages can be repeated).

It has a built in functionality to automatically undo the page ordering when you scan all odd side pages first then even side pages first,
i.e. when you use a one-sided scanner to scan double sided pages in bulk.

The file needs to be in the same folder as the .py, and the default output pdf is called <ins>reordered_output.pdf</ins>
