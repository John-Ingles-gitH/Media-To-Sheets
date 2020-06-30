[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](http://choosealicense.com/licenses/mit/)

Media-To-Sheets is a tool to search for media attributes from a variety of sources and update a Google Sheets document with them.  The Google Sheets document will them be used to store the info needed to create a website for browsing the attributes.

## Anaconda Install

* Create a conda environment using `conda env create -f environment.yml`


### Using `virtualenv` and `virtualenvwrapper`
After installing `virtualenv` and `virtualenvwrapper`
```sh
git clone https://github.com/John-Ingles-gitH/Media-To-Sheets.git
virtualenv myproject
source myproject/venv/bin/activate
pip install -r requirements.txt
```
## Using Media-To-Sheets
Run the Following:
```sh
python media_to_sheets.py
```