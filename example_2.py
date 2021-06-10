# Released by: Core Electronics Pty Ltd
# Author: Graham Mitchell
# Attribution-ShareAlike 3.0 Australia (CC BY-SA 3.0 AU)
# https://creativecommons.org/licenses/by-sa/3.0/au/

print("Example - Measure lux - lumens per square metre")

from network import LoRa
import pycom
import lorawan
import utime
from PiicoDev_VEML6030 import PiicoDev_VEML6030

# set LED to yellow
pycom.rgbled(0x111100)

# create an object for the piicodev hardware
light = PiicoDev_VEML6030()

for x in range (0, 5):

    # measure the light intensity, in lux
    lightVal = light.read()

    # print the result to the console
    print("Sending Light Intensity: {:4.0f}".format(lightVal))

    # now send over the LoRaWAN network
    lorawan.socket_1.send("L:" + "{:4.0f}".format(lightVal))

    utime.sleep(2)


print("Complete!")

# set LED to green
pycom.rgbled(0x001100)
