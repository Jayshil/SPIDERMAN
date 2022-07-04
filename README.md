# SPIDERMAN

welcome to spiderman!

Read the docs at [spiderman.readthedocs.io](http://spiderman.readthedocs.io)

Or check out some of the example ipython notebooks in the example folder


## Changes in this fork:

in setup.py, line 16:

#license = ['GNU GPLv3'],
license = 'GNU GPLv3',


in spiderman/plot.py:

#from matplotlib._png import read_png
from cv2 import imread as read_png


in spiderman/stellar_grid.py, line 27
#warned = False
warned = True

## Changes made:
Changed setup.py ([line 6](https://github.com/Jayshil/SPIDERMAN/blob/a40d56d532d8229bcbddf12262968c98d535c5fb/setup.py#L6)) to add the following argument:

include_dirs=[numpy.get_include()]

in Extension command of setup.py.
