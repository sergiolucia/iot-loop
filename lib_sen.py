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
import components
import pdb
from casadi import *


# u = SX.sym("u")
# trigger = SX.sym("trigger")
def sen_measGaussian(u):
    out = components.component(label = "sensor")
    out.x =
    # The sensor has no own dynamics
    f_x = []
    # The sensor output is a simple measurement with Gaussian noise
    mean = 0
    std  = 0.5
    noise = mean + std * np.random.randn(u.shape[0])
    f_y = Function('f_y', [u, noise],[u + noise])
    # The sensor KPIs are indicated here
    energy = Function("energy",[trigger], [0.1 + 0.5 * trigger])
    software_cost = 0.0 # €/year
    hardware_cost = 100.0 # € for sensor
    maintenance_cost = 50.0 * trigger # €/year for battery replacement
    total_cost = software_cost + hardware_cost + maintenance_cost
    cost = Function("cost", [trigger], [total_cost])
    human_discomfort = 0.0
    f_p = {"energy": energy, "cost":cost, "human_discomfort":human_discomfort}
    # The sensor metadata
    f_q = {}
    for i in range(f_y.numel_out()):
        f_q["y"+i+"_data_ownership"] =
        f_q["y"+i+"_data_price"] =
        f_q["y"+i+"_data_privacy"] = 
