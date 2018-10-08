#
# This file is part of the iot-loop toolbox
#
# This file defines the main classes for each component of an IoT Loop
# Copyright (C) 2018 Sergio Lucia, TU Berlin
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.



import numpy as np
import pdb

class component:
    """ A class for each component of the iot-loop """
    def __init__(x = None, u = None, p = None, y = None, q = None, comp_type = None):
        self.x = x # dynamics
        self.u = u # inputs
        self.y = y # outputs
        self.p = p # kpis
        self.q = q # metadata

        self.type = comp_type
        
