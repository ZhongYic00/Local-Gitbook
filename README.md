_The Project Is Not Actively Maintained Now_
------

# Local Gitbook

This is a simple client aimed at download, managing and reading gitbooks offline just on your computer.

## Why do we need to read gitbook offline?

Benefits varies from stability, availability and accessibility.

- Stability. Since the gitbook-old project has reached EOL, many books are now served by private servers or sites as github where you may experience high latency.
- Availability. When we search for some resources online, what frequently occurs is that the resource is deleted some time ago. Download & save the book offline, then you won't suffer from losing the resources.
- Accessibility. Troubled by the huge mess of bookmarks? The app provides you a SPA(single-paged-application) where you can download books, see all your downloaded books, edit book-infos, save your reading progress etc. Thus a mess of bookmarks aren't needed anymore!

## Usage

### Dependencies

- docker
- flask
- gitpython
- pybase62
- @angular/cli

### Running

```shell
# build angular app
cd local-gitbook
npm install
ng build
mv dist/local-gitbook ../flaskr/static/

# run flask server
export FLASK_APP=__init__.py; python3 -m flask run

# open localhost:5000 and you can use the app
```

## Bug Report

The app is just for fun, so I cannot guarantee any bug to be repaired. However, **any issue is welcomed** although the fix just depends.
