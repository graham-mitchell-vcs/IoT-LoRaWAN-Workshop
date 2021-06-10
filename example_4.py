# Released by: Core Electronics Pty Ltd
# Author: Graham Mitchell
# Attribution-ShareAlike 3.0 Australia (CC BY-SA 3.0 AU)
# https://creativecommons.org/licenses/by-sa/3.0/au/

print("Example - All 3 sensors, because why not!")

from network import LoRa
import pycom
import lorawan
import utime
from PiicoDev_TMP117 import PiicoDev_TMP117
from PiicoDev_VEML6030 import PiicoDev_VEML6030
from PiicoDev_VL53L1X import PiicoDev_VL53L1X

# set LED to yellow
pycom.rgbled(0x111100)

# create objects for the piicodev hardware
temp = PiicoDev_TMP117()
laser = PiicoDev_VL53L1X()
light = PiicoDev_VEML6030()

for x in range (0, 5):

    # read the temperature from the sensor
    tempC = temp.readTempC()

    # print the result to the console
    print("Temperature: {:5.2f}".format(tempC))

    # now send over the LoRaWAN network
    lorawan.socket_1.send("T:" + "{:5.2f}".format(tempC))
    utime.sleep(1)

    # measure the light intensity, in lux
    lightVal = light.read()

    # print the result to the console
    print("Sending Light Intensity: {:4.0f}".format(lightVal))

    # now send over the LoRaWAN network
    lorawan.socket_1.send("L:" + "{:4.0f}".format(lightVal))
    utime.sleep(1)

    # measure distance in millimeters
    dist = laser.read()

    # print the result to the console
    print("Sending Distance: {:4d}".format(dist))

    # now send over the LoRaWAN network
    lorawan.socket_1.send("D:" + "{:4d}".format(dist))
    utime.sleep(3)


print("Complete!")

# set LED to green
pycom.rgbled(0x001100)
