__all__ = 'fetch'

import os, sys

from m3ta import main, join

def browser(name):
    names = {
        'aix': '', 
        'cygwin': '', 
        'darwin': {
            'chrome': '"google chrome"',
            'firefox': 'firefox'
        }, 
        'linux': {
            'chrome': 'google-chrome',
            'firefox': 'firefox'
        }, 
        'win32': {
            'chrome': 'chrome',
            'firefox': 'firefox'
        },
    }
    return names[sys.platform][name]

def privacy(app):
    commands = {
        'chrome': 'incognito',
        'firefox': 'private',
    }
    prefixes = {
        'aix': '--', 
        'cygwin': '--', 
        'darwin': '--', 
        'linux': '--', 
        'win32': '/',
    }
    return prefixes[sys.platform] + commands[app]


def fetch(url:str, app='firefox', private=False):
    """
    Open a webpage in your favourite browser
    """    
    prefixes = {
        'aix': '', 
        'cygwin': '', 
        'darwin': 'open -a', 
        'linux': '', 
        'win32': 'start',
    }
    
    pref = prefixes[sys.platform]
    priv = privacy(app) if private and sys.platform!='win32' else ''
    brow = browser(app)
    terms = [pref, priv, brow, url]
    cmd = join(filter(None, terms), sep=' ')
    print(cmd)
    return os.popen(cmd)




if eval(main):
    url = 'abcd.org'
    url = "https://giphy.com/gifs/reactionseditor-yes-awesome-3ohzdIuqJoo8QdKlnW?utm_source=iframe&utm_medium=embed&utm_campaign=Embeds&utm_term=https%3A%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%3A%2F%2Fgiphy.com%2Fembed%2F3ohzdIuqJoo8QdKlnW%2Ftwitter%2Fiframe&%3Bdisplay_name=Giphy&%3Burl=https%3A%2F%2Fmedia.giphy.com%2Fmedia%2F3ohzdIuqJoo8QdKlnW%2Fgiphy.gif&%3Bimage=https%3A%2F%2Fi.giphy.com%2Fmedia%2F3ohzdIuqJoo8QdKlnW%2Fgiphy.gif&%3Bkey=a19fcc184b9711e1b4764040d3dc5c07&%3Btype=text%2Fhtml&%3Bschema=giphy"
    url = 'http://gph.is/2roKEH4'
    fetch(url)