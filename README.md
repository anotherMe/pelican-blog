
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

### Build

```(venv)$ pelican```

### Test

```(venv)$ pelican --listen```
