# MIMIC WFDB Tutorials
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

This repository contains a Jupyter book called 'MIMIC WFDB Tutorials', which presents tutorials on using the MIMIC Waveform Database for Biomedical Signal Processing.

The book is available [here](https://wfdb.github.io/mimic_wfdb_tutorials/intro.html).

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://peterhcharlton.github.io/"><img src="https://avatars.githubusercontent.com/u/9865941?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Peter H Charlton</b></sub></a><br /><a href="#content-peterhcharlton" title="Content">🖋</a></td>
    <td align="center"><a href="https://github.com/tompollard"><img src="https://avatars.githubusercontent.com/u/822601?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Tom Pollard</b></sub></a><br /><a href="#design-tompollard" title="Design">🎨</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

## Development

This website was created with [JupyterBook](https://jupyterbook.org/). To set up a local development environment, follow the steps below:

1. Navigate to the project directory (e.g. `mimic_wfdb_tutorials`)
2. Install the required packages with `pip install -r requirements.txt` (preferably in a virtual environment using something like venv, virtualenv, conda etc.)
3. Change to the directory with the content (e.g. `cd content`)
4. Run `jupyter-book build --all ./` from within this directory to build the book.
5. The HTML bookfiles should have been created in a `_build` folder.
