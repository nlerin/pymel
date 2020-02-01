"""Low-level maya and pymel utilities.  Functions in this module are used by both `pymel.api` and `pymel.core`,
and are able to be defined before maya.standalone is initialized.
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
from builtins import *
from .plogging import getLogger
