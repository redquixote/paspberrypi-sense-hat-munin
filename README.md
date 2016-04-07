# Raspberry pi, sense-hat and munin
Candid Munin scripts for Raspberry Pi and Sense Hat

## To install:
- Install dependencies
```
pip -r requirements.txt 
```

- create sym links for munin

```
ln -s /home/pi/workspace/munin/sense_humidity.py /etc/munin/plugins/sense_humidity
ln -s /home/pi/workspace/munin/sense_pressure.py /etc/munin/plugins/sense_pressure 
ln -s /home/pi/workspace/munin/sense_temp.py /etc/munin/plugins/sense_temp 
```

- restart munin
```
service munin-node restart
```

## Requires
- munin preinstalled
- python

## Screenshots
![munin-screenshot2-pi-sense](https://raw.githubusercontent.com/redquixote/paspberrypi-sense-hat-munin/master/screenshots/munin-screenshot2-pi-sense.png)
![munin-screenshot1-pi-sense](https://raw.githubusercontent.com/redquixote/paspberrypi-sense-hat-munin/master/screenshots/munin-screenshot1-pi-sense.png)



