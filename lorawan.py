from network import LoRa
import socket
import binascii
import utime
import machine
import pycom

# disable the LED heartbeat
pycom.heartbeat(False)

# set LED to red
pycom.rgbled(0x110000)

# lora config
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.AS923)

# access info from ttn console (note; we just need the app id & app key)
app_eui = binascii.unhexlify('XXXXXXXXXXXXXX')
app_key = binascii.unhexlify('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

def join():
    global lora
    global app_eui
    global app_key
    global socket_1

    print("Connecting to the LoRaWAN network")

    # attempt join - continues attempts background every 15 seconds
    lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

    # wait for a connection to be established
    while not lora.has_joined():
        if utime.time() > 7:
            print("possible timeout")
            machine.reset()

        utime.sleep(0.1)
        pass

    print("Success, connected")

    # setup the socket - of note is port number is configured with s.bind
    socket_1 = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    socket_1.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
    socket_1.setblocking(False)
    socket_1.bind(1)

    # set LED to green
    pycom.rgbled(0x001100)
