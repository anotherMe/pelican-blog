
# pelican-blog

This was my blog. Really nothing more than a place to save some notes.

## Setup

You'll need **python**, **pip** and **virtualenv** already set up.

Create virtualenv:

```
$ virtualenv venv
```

Activate virtualenv:

```
$ source venv/bin/activate
```

Install required dependencies:

```
(venv)$ pip install pelican markdown
```


## Get started

### Write something

Add new content in *content* folder or *content/page* folder.


### Generate site

```
(venv)$ pelican
```

### Testing

Launch Pelican web server:

```
(venv)$ pelican --listen
```

then point browser to [localhost:8000](http://localhost:8000) .

### publishing

When you run *pelican* command, it defaults to the configuration specified in the *pelicanconf.py* file.

The file *publishconf.py* file, if kept up to date, is useful for keeping publishing configuration separated.

When packing your site for deploying, issue the command:

```
pelican -s publishconf.py
```
