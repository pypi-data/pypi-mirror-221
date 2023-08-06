from ._confutil import *

__all__ = ['__version__', 'check_config']
__version__ = '1.0.3'


def check_config(_object=None, _filename='config'):
    return confutil.check_config(_object, _filename)
