# deviuce EUI


# code needed to get the device EUI
from network import LoRa
import binascii
lora = LoRa(mode=LoRa.LORAWAN)
print(binascii.hexlify(lora.mac()).upper().decode('utf-8'))

# payload encoder javascript
function Decoder(bytes, port) {
  var receivedStr = String.fromCharCode.apply(null, bytes);
  if (receivedStr.indexOf("T:") !== -1) {
    return { Data_Temperature: receivedStr.split(":")[1] };
  } else if (receivedStr.indexOf("L:") !== -1) {
    return { Data_Lux: receivedStr.split(":")[1] };
  } else if (receivedStr.indexOf("D:") !== -1) {
    return { Data_Distance: receivedStr.split(":")[1] };
  } else {
    return { Value: receivedStr };
  }
}



# python course by Google
https://developers.google.com/edu/python/introduction

# pycom docs
https://docs.pycom.io/

# pycom update tool
https://docs.pycom.io/gettingstarted/installation/firmwaretool

# how to setup Pycom LoPy on TTN (note: NEED to use AS923)
https://www.thethingsnetwork.org/docs/devices/lopy/
https://www.thethingsnetwork.org/docs/devices/lopy/usage.html

# how to get your app "using" ttn data
https://www.thethingsnetwork.org/docs/applications/

# how to customise payload functions on TTN - this is very handy
https://www.youtube.com/watch?v=nT2FnwCoP7w

# our  guide for using LoRa + TTN + NodeRed
https://core-electronics.com.au/tutorials/iot-with-lorawan-pycom-the-things-network-and-node-red.html

# working with struct.pack / unpack
https://docs.python.org/3/library/struct.html
https://docs.pycom.io/firmwareapi/micropython/ustruct

# fast and easy way to get fancy dashboards and widgets
http://miscellany.bouillot.org/post/153134895780/data-storage-and-visualization-for-the-things

# How to get Node Red on AWS 'near always uptime'
https://nodered.org/docs/platforms/aws

# data limits for TTN
https://www.thethingsnetwork.org/forum/t/limitations-data-rate-packet-size-30-seconds-uplink-and-10-messages-downlink-per-day-fair-access-policy/1300

# where to buy pycom hardware in Australia
https://core-electronics.com.au/pycom.html
