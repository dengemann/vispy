# -*- coding: utf-8 -*-
# Copyright (c) 2013, Vispy Development Team.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

from __future__ import print_function, division, absolute_import

from vispy.visuals import PointsVisual
from ..base import Entity


class PointsEntity(Entity):
    """ An entity that shows a random set of points.
    """
    
    Visual = PointsVisual
    def __init__(self, parent=None, N=1000):
        Entity.__init__(self, parent, N=N)
