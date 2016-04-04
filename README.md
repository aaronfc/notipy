# notipy
Humble try to get a cross-platform notification mechanism for different OS.

## Supported
- OSX (osascript)
- Ubuntu (send-notify)

## Installation
`$ pip install notipy # When available on pypi`

## Usage
### From command line
`$ notipy "Cool message"`
### From python
```python
from notipy import Notipy
Notipy().send("Awesome message")
```

## Screenshots
![OSX Screenshot](https://github.com/aaronfc/notipy/raw/master/docs/images/screenshot-osx.png "OSX Screenshot")
