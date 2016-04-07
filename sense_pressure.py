#!/usr/bin/env python

import os
from munin import MuninPlugin
from sense_hat import SenseHat


class SensePlugin(MuninPlugin):
    title = "Pressure"
    # args = "--base 1000 -l 0"
    vlabel = "milibars"
    scale = False
    category = "sense"

    @property
    def fields(self):
        warning = os.environ.get('pressure_warn', 1100)
        #critical = os.environ.get('pressure_crit', 1100)
        return [("pressure", dict(
                label = "pressure",
                info = 'pressure from sensor',
                type = "GAUGE",
                min = "900", # milibars
                warning = str(warning),
                #critical = str(critical)
		)),
		]

    def execute(self):
	sense = SenseHat()
	pressure = sense.get_pressure()
        return dict(pressure=pressure)

if __name__ == "__main__":
    SensePlugin().run()
