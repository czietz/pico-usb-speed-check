#!/usr/bin/python3

import usb.core
import usb.util
import time

TOTALSIZE = 2*1024*1024
XFERSIZE  = 2048

# find our device
dev = usb.core.find(idVendor=0xcafe, idProduct=0x4010)

# was it found?
if dev is None:
    raise ValueError('Device not found')

# set the active configuration. With no arguments, the first
# configuration will be the active one
dev.set_configuration()

# get an endpoint instance
cfg = dev.get_active_configuration()
intf = cfg[(0,0)]

epout = usb.util.find_descriptor(
    intf,
    # match the first OUT endpoint
    custom_match = \
    lambda e: \
        usb.util.endpoint_direction(e.bEndpointAddress) == \
        usb.util.ENDPOINT_OUT)

epin  = usb.util.find_descriptor(
    intf,
    # match the first IN endpoint
    custom_match = \
    lambda e: \
        usb.util.endpoint_direction(e.bEndpointAddress) == \
        usb.util.ENDPOINT_IN)


assert epout is not None
assert epin  is not None

done = 0
start = time.perf_counter()
while done < TOTALSIZE:
    done = done + epout.write(b'X' * XFERSIZE)
stop = time.perf_counter()
print("Host -> Device: %.2f kBytes/s" % (done/(stop-start)/1024))

done = 0
start = time.perf_counter()
while done < TOTALSIZE:
    done = done + len(epin.read(XFERSIZE))
stop = time.perf_counter()
print("Device -> Host: %.2f kBytes/s" % (done/(stop-start)/1024))

