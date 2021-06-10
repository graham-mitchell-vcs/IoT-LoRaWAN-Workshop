# Released by: Core Electronics Pty Ltd
# Author: Graham Mitchell
# Attribution-ShareAlike 3.0 Australia (CC BY-SA 3.0 AU)
# https://creativecommons.org/licenses/by-sa/3.0/au/

print("Example - Laser distance sensor - super precise millimeter readings")

from network import LoRa
import pycom
import lorawan
import utime
from PiicoDev_VL53L1X import PiicoDev_VL53L1X

# set LED to yellow
pycom.rgbled(0x111100)

# create objects for the piicodev hardware
laser = PiicoDev_VL53L1X()

for x in range (0, 5):

    # measure distance in millimeters
    dist = laser.read()

    # print the result to the console
    print("Sending Distance: {:4d}".format(dist))

    # now send over the LoRaWAN network
    lorawan.socket_1.send("D:" + "{:4d}".format(dist))

    utime.sleep(2)


print("Complete!")

# set LED to green
pycom.rgbled(0x001100)
