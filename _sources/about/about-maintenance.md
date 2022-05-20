# Maintenance

## Editing the book

There are two ways to edit the book:
```{dropdown} **1. Edit online:** Open to all
- Submit a proposed edit using the instructions provided above under ['Contributing to the book'](#contributing-to-the-book).
- This will be reviewed in due course.
```
```{dropdown} **2. Edit on a local computer:** Only open to project administrators
- Clone the repository

`cd /Users/petercharlton/Documents/GitHub/; git clone https://github.com/mit-lcp/mimic_wfdb_tutorials`
- Make edits to the files on a local computer.
- Upload the files through a git push (as detailed [here](https://jupyterbook.org/start/publish.html#create-an-online-repository-for-your-book)):

`cd /Users/petercharlton/Documents/GitHub/mimic_wfdb_tutorials; git add ./*; git commit -m "brief edit"; git push`
- Build the book locally (as detailed [here](https://jupyterbook.org/start/build.html#build-your-books-html)): 

`cd /Users/petercharlton/Documents/GitHub/mimic_wfdb_tutorials/; jupyter-book build --path-output . content`
- Upload the built book to GitHub pages (as detailed [here](https://jupyterbook.org/start/publish.html#publish-your-book-online-with-github-pages)):

`cd /Users/petercharlton/Documents/GitHub/mimic_wfdb_tutorials/; ghp-import -n -p -f _build/html`
```

## Recognising contributors

Contributors to the Book who have GitHub accounts can be recognised using the 'All Contributors' app (see details [here](https://allcontributors.org/docs/en/bot/usage)).

## Creating the book

The book was created as follows (largely following the instructions provided [here](https://jupyterbook.org/start/your-first-book.html)):
```{dropdown} **Steps to create the book:** 
1. Install Jupyter book via conda-forge (as detailed [here](https://jupyterbook.org/start/overview.html))
2. Create a template book (as detailed [here](https://jupyterbook.org/start/create.html))
3. Modify the template to include content from Peter Charlton's original project guidelines (available [here](https://peterhcharlton.github.io/info/tools/project_guidelines.html)).
4. Build the book (as detailed [here](https://jupyterbook.org/start/build.html)).
5. Publish the book online (storing the source files in a GitHub repository, and publishing the book using GitHub pages, as detailed [here](https://jupyterbook.org/start/publish.html)).
```

