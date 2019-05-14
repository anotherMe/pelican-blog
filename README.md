
# pelican-blog

These are the markdown files that make up my blog, currently hosted at memoryleak.it/blog

## Setup

You'll need **python**, **pip** and **virtualenv** already set up.

Create virtualenv:

```$ virtualenv venv```

Activate virtualenv:

```$ source venv/bin/activate```

Install required dependencies:

```(venv)$ pip install pelican markdown```

## Generate site

```(venv)$ pelican```

### Test

Launch Pelican web server:

```(venv)$ pelican --listen```

then point browser to [localhost:8000](http://localhost:8000) .
