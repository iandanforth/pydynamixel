import os
import dynamixel
import time
import random
import sys
import subprocess

###############################################################################
# The end point of the servos we will scan for.
#
# If you have servos with ids 3, 12, and 15 this value should be 15.
# This will scan at approximately one servo id a second so don't worry if it
# takes a little bit.

lastServoId = 16

# Set your serial port accordingly.
if os.name == "posix":
  portName = None
  if not portName:
    print ('You will need to edit this example and set a value for "portName".\n'
          'Here are a few possible ports you might want to try if you do not\n'
          'know exactly where your USB2Dynamixel is attached:')
    # Get a list of ports that mention USB
    possiblePorts = subprocess.check_output('ls /dev/*usb*', shell=True).split()
    for port in possiblePorts:
      print '\t' + port
    sys.exit(1)
else:
    portName = "COM11"

# Default baud rate of the USB2Dynamixel device.
baudRate = 1000000

serial = dynamixel.SerialStream( port=portName, baudrate=baudRate, timeout=1)
net = dynamixel.DynamixelNetwork( serial )
net.scan( 1, lastServoId )

myActuators = list()

print "Scanning for Dynamixels..."
for dyn in net.get_dynamixels():
    print dyn.id
    myActuators.append(net[dyn.id])

if not myActuators:
  print 'No Dynamixels Found!'
  sys.exit(0)
else:
  print "...Done"

for actuator in myActuators:
    actuator.moving_speed = 50
    actuator.synchronized = True
    actuator.torque_enable = True
    actuator.torque_limit = 800
    actuator.max_torque = 800

while True:
    for actuator in myActuators:
        actuator.goal_position = random.randrange(450, 600)
    net.synchronize()
    for actuator in myActuators:
        actuator.read_all()
        time.sleep(0.01)
    for actuator in myActuators:
        print actuator.cache[dynamixel.defs.REGISTER['Id']], actuator.cache[dynamixel.defs.REGISTER['CurrentPosition']]
    time.sleep(2)
