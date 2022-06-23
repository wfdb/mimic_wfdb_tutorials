# Maintenance

## Editing the book

There are two ways to edit the book:
```{dropdown} **1. Edit online:** Open to all
- Submit a proposed edit using the instructions provided above under ['Contributing to the book'](#contributing-to-the-book).
- This will be reviewed in due course.
```
```{dropdown} **2. Edit on a local computer:** Only open to project administrators
- If you don't already have the _mimic_wfdb_tutorials_ repository on your computer, then clone the repository

`cd /Users/petercharlton/Documents/GitHub/; git clone https://github.com/wfdb/mimic_wfdb_tutorials`
- If you do already have the repository, then pull the latest version:

`cd /Users/petercharlton/Documents/GitHub/mimic_wfdb_tutorials; git pull https://github.com/wfdb/mimic_wfdb_tutorials main`
- Make edits to the files on a local computer:
   - `cd /Users/petercharlton/Documents/GitHub/mimic_wfdb_tutorials` - make the current directory the repo directory.
   - `git checkout -b <branch name>` - Creates a new branch on which to make the edits(specified by `<branch name>`), and makes it the current branch.
   - edit the files ([Atom](https://atom.io/) is a helpful text editor for this).
   - `git add .` - adds all changed files to the staging area.
   - `git commit -m "<message describing changes>"` - commit the changes to the current branch.
   - `git push https://github.com/wfdb/mimic_wfdb_tutorials <branch name>` - pushes the changes to the remote repo on GitHub.
- Log in to GitHub via a web browser, and go to the [repo home page](https://github.com/wfdb/mimic_wfdb_tutorials). Assuming you have access, then you should see a message at the top of the page allowing you to create a pull request, to pull the changes from your new branch over to the main branch.

_The following are legacy instructions, which may or may not still be required when making changes to a Jupyter notebook:_

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
