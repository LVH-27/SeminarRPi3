#!/usr/bin/python

from LIS3DH import LIS3DH
from time import sleep

if __name__ == '__main__':
    sensor = LIS3DH(debug=True)
    sensor.setRange(LIS3DH.RANGE_2G)
    sensor.setClick(LIS3DH.CLK_SINGLE,80,mycallback=clickcallback)

    print "Starting stream"
    while True:
        x = sensor.getX()
        y = sensor.getY()
        z = sensor.getZ()

# raw values
        print "\rX: %.6f\tY: %.6f\tZ: %.6f" % (x,y,z)
        sleep(0.1)
