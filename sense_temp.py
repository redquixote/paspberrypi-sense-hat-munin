#!/usr/bin/env python

import os
from munin import MuninPlugin
from sense_hat import SenseHat

ADJUSTMENT=9

class TempPlugin(MuninPlugin):
    title = "Adjusted Temperature" 
    # args = "--base 1000 -l 0"
    vlabel = "adjusted temp (-{0})".format(ADJUSTMENT)
    scale = False
    category = "sense"

    @property
    def fields(self):
        warning = str(os.environ.get('temp_warn', 25))
        warning_low = str(os.environ.get('temp_warn_low', 20))
        critical = str(os.environ.get('temp_crit', 30))
        critical_low = str(os.environ.get('temp_crit_low', 17))
        return [("temp", dict(
                label = "temp",
                info = 'The temperature from sensor',
                type = "GAUGE",
                min = "0",
                warning = "{0}:{1}".format(warning_low, warning),
                critical = "{0}:{1}".format(critical_low, critical),
		)),
       		("temp_hum", dict(
                label = "temp_humidity",
                info = 'The temperature from humidity sensor',
                type = "GAUGE",
                min = "0",
                warning = "{0}:{1}".format(warning_low, warning),
                critical = "{0}:{1}".format(critical_low, critical),
		)),
       		("temp_pre", dict(
                label = "temp_pressure",
                info = 'The temperature from pressure sensor',
                type = "GAUGE",
                min = "0",
                warning = "{0}:{1}".format(warning_low, warning),
                critical = "{0}:{1}".format(critical_low, critical)
		))
		]

    def execute(self):
	sense = SenseHat()
	temp = sense.get_temperature()-ADJUSTMENT
	temp_hum = sense.get_temperature_from_humidity()-ADJUSTMENT
	temp_pre = sense.get_temperature_from_pressure()-ADJUSTMENT
        return dict(temp=temp, temp_hum=temp_hum, temp_pre=temp_pre)

if __name__ == "__main__":
    TempPlugin().run()
