# Markdown document builder

this builder can batch compile markdown documents to html/css/js docs.it's based on [vue-markdown](https://github.com/miaolz123/vue-markdown).

## Supported Platforms:
* Linux
* Mac OS
* Docker

## Quick Start
```sh
git clone https://github.com/colin-chang/md2html.git && cd src
python3 app.py input output
```
be sure to custom the input and output parameter before executing. input can be a markdown file(.md) or a directory contains markdown files.

* Node v12.13.0 and Python 3.x are required


## Docker

https://hub.docker.com/r/colinchang/md2html

```
# build a specify markdown file
docker run -it -v /readme.md:/app/input/readme.md -v /your_output_dir:/app/output colinchang/md2html:alpine

# scan a directory and build all markdown files recursively 
docker run -it -v /your_input_dir:/app/input -v /your_output_dir:/app/output colinchang/md2html:alpine
```

## Tips
in addition to outer links, we currently only support associated resources of markdown files from its peer directory or subdirectories.
