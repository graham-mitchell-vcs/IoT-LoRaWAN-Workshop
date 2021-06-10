# Released by: Core Electronics Pty Ltd
# Author: Graham Mitchell
# Attribution-ShareAlike 3.0 Australia (CC BY-SA 3.0 AU)
# https://creativecommons.org/licenses/by-sa/3.0/au/

print("Example - Measuring *really* accurate temperature")

from network import LoRa
import pycom
import lorawan
import utime
from PiicoDev_TMP117 import PiicoDev_TMP117

# set LED to yellow
pycom.rgbled(0x111100)

# create an object for the piicodev hardware
temp = PiicoDev_TMP117()

for x in range (0, 5):

    # read the temperature from the sensor
    tempC = temp.readTempC()

    # print the result to the console
    print("Temperature: {:5.2f}".format(tempC))

    # now send over the LoRaWAN network
    lorawan.socket_1.send("T:" + "{:5.2f}".format(tempC))

    utime.sleep(2)

# set LED to green
pycom.rgbled(0x001100)

print("Complete!")

# set LED to green
#pycom.rgbled(0x001100)
