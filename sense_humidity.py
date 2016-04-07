#!/usr/bin/env python

import os
from munin import MuninPlugin
from sense_hat import SenseHat


class SensePlugin(MuninPlugin):
    title = "Humidity"
    # args = "--base 1000 -l 0"
    vlabel = "rel Humidity"
    scale = False
    category = "sense"

    @property
    def fields(self):
        warning = os.environ.get('humidity_warn', 50)
        critical = os.environ.get('humidity_crit', 60)
        return [("humidity", dict(
                label = "humidity",
                info = 'humidity from sensor',
                type = "GAUGE",
                min = "0",
                warning = "40:60",
                critical = "30:70",
		)),
		]

    def execute(self):
	sense = SenseHat()
	humidity = sense.get_humidity()
        return dict(humidity=humidity)

if __name__ == "__main__":
    SensePlugin().run()
