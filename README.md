# notipy
Humble try to get a cross-platform notification mechanism for different OS.

## Status
This is a **work in progress**. Take a look at the *Supported OS* sub-section.

### Supported OS
* OSX (osascript since 10.9 Mavericks)
* Ubuntu (notify-send from [libnotify package](https://launchpad.net/ubuntu/+source/libnotify))

**Warning:** Minimal support for OSX and Ubuntu relying on (*usually-preinstalled*) OS packages

## Installation
#### When available on pypi
`$ pip install notipy`
#### Until then... *(might need sudo for the last part)*
```bash
$ git clone https://github.com/aaronfc/notipy.git
$ cd notipy
$ pip install .
```

## Usage
### From command line
`$ notipy "Cool message"`
### From python
```python
from notipy.cli import Notipy
Notipy().send("Awesome message")
```

## Screenshots
![OSX Screenshot](https://github.com/aaronfc/notipy/raw/master/docs/images/screenshot-osx.png "OSX Screenshot")
![Ubuntu Screenshot](https://github.com/aaronfc/notipy/raw/master/docs/images/screenshot-ubuntu.png "Ubuntu Screenshot")
