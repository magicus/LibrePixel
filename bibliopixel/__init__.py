from . led import Circle, Matrix, POV, Strip, Cube
from . layout import Rotation
from . layout.matrix import gen_matrix
from . layout.circle import gen_circle
from . layout.cube import gen_cube
from . import animation, colors, font, gamma, led, log, util

# These are DEPRECATED
from . led import LEDCircle, LEDMatrix, LEDPOV, LEDStrip, LEDCube


def _get_version():
    from os.path import abspath, dirname, join
    filename = join(dirname(abspath(__file__)), 'VERSION')
    return open(filename).read().strip()


__version__ = _get_version()
VERSION = __version__
