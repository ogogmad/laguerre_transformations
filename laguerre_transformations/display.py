try:
    from .display_via_tk import display_tk_multiprocess
    from .display_via_matplotlib import display_via_matplotlib
    from .display_via_moviepy import display_via_moviepy
    from .display_using_moviepy_and_browser_launch import display_using_moviepy_and_browser_launch
    from .display_via_videofig import display_via_videofig
except ImportError:
    from display_via_tk import display_tk_multiprocess
    from display_via_matplotlib import display_via_matplotlib
    from display_via_moviepy import display_via_moviepy
    from display_using_moviepy_and_browser_launch import display_using_moviepy_and_browser_launch
    from display_via_videofig import display_via_videofig

options =  ['tk_multiprocess',
            'matplotlib',
            'moviepy',
            'moviepy_launch_browser',
            'videofig']

def display(images, title, via='tk_multiprocess'):
    """Display an animated sequence of images in a new window and process.
    The keyword argument `via` dictates the method that's used.
    `via` can be one of ['tk_multiprocess',
                         'matplotlib',
                         'moviepy',
                         'moviepy_launch_browser'],
                         'videofig'"""
    if via == 'tk_multiprocess':
        display_tk_multiprocess(images, title)
    elif via == 'matplotlib':
        display_via_matplotlib(images, title)
    elif via == 'moviepy':
        display_via_moviepy(images, title)
    elif via == 'moviepy_launch_browser':
        display_using_moviepy_and_browser_launch(images, title)
    elif via == 'videofig':
        display_via_videofig(images, title)
    else:
        raise ValueError("""`via` must be one of """ + str(options))