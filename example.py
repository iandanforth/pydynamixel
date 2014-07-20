import os
import dynamixel
import sys
import subprocess
import optparse
import yaml

""" 
This script will discover available USB ports to which the USB2Dynamixel may
be attached. It will also help you discover the list of servos that are in the
network. Once that has been done these values will be stored in  a local
settings.yaml file.

You will then be shown all of the found servo ids, and be asked if you want to 
set them all to the home position (512).
"""

def main(settings):
    
    # Establish a serial connection to the dynamixel network.
    # This usually requires a USB2Dynamixel
    serial = dynamixel.SerialStream(port=settings['port'],
                                    baudrate=settings['baudRate'],
                                    timeout=1)
    # Instantiate our network object
    net = dynamixel.DynamixelNetwork(serial)

    # Populate our network with dynamixel objects
    for servoId in settings['servoIds']:
        newDynamixel = dynamixel.Dynamixel(servoId, net)
        net._dynamixel_map[servoId] = newDynamixel
    
    if not net.get_dynamixels():
      print 'No Dynamixels Found!'
      sys.exit(0)
    else:
      print "...Done"
    
    # Prompt the user to move servos.
    answer = raw_input("Would you like to move all the servos to the home position?"
                   "\nWARNING: If servos are obstructed this could damage them "
                   "\nor things in their path. [y/N] ")
    if answer in ['y', 'Y', 'yes', 'Yes', 'YES']:

        # Set up the servos
        for actuator in net.get_dynamixels():
            actuator.moving_speed = 50
            actuator.torque_enable = True
            actuator.torque_limit = 800 
            actuator.max_torque = 800
            actuator.goal_position = 512

        # Send all the commands to the servos.
        net.synchronize()

        print("Congratulations! Read the code to find out how that happened!")

def validateInput(userInput, rangeMin, rangeMax):
    '''
    Returns valid user input or None
    '''
    try:
        inTest = int(userInput)
        if inTest < rangeMin or inTest > rangeMax:
            print "ERROR: Value out of range [" + str(rangeMin) + '-' + str(rangeMax) + "]"
            return None
    except ValueError:
        print("ERROR: Please enter an integer")
        return None
    
    return inTest

if __name__ == '__main__':
    
    parser = optparse.OptionParser()
    parser.add_option("-c", "--clean",
                      action="store_true", dest="clean", default=False,
                      help="Ignore the settings.yaml file if it exists and \
                      prompt for new settings.")
    
    (options, args) = parser.parse_args()
    
    # Look for a settings.yaml file
    settingsFile = 'settings.yaml'
    if not options.clean and os.path.exists(settingsFile):
        with open(settingsFile, 'r') as fh:
            settings = yaml.load(fh)
    # If we were asked to bypass, or don't have settings
    else:
        settings = {}
        if os.name == "posix":
            portPrompt = "Which port corresponds to your USB2Dynamixel? \n"
            # Get a list of ports that mention USB
            try:
                possiblePorts = subprocess.check_output('ls /dev/ | grep -i usb',
                                                        shell=True).split()
                possiblePorts = ['/dev/' + port for port in possiblePorts]
            except subprocess.CalledProcessError:
                sys.exit("USB2Dynamixel not found. Please connect one.")
                
            counter = 1
            portCount = len(possiblePorts)
            for port in possiblePorts:
                portPrompt += "\t" + str(counter) + " - " + port + "\n"
                counter += 1
            portPrompt += "Enter Choice: "
            portChoice = None
            while not portChoice:                
                portTest = raw_input(portPrompt)
                portTest = validateInput(portTest, 1, portCount)
                if portTest:
                    portChoice = possiblePorts[portTest - 1]

        else:
            portPrompt = "Please enter the port name to which the USB2Dynamixel is connected: "
            portChoice = raw_input(portPrompt)
    
        settings['port'] = portChoice
        
        # Baud rate
        baudRate = None
        while not baudRate:
            brTest = raw_input("Enter baud rate [Default: 1000000 bps]:")
            if not brTest:
                baudRate = 1000000
            else:
                baudRate = validateInput(brTest, 9600, 1000000)
                    
        settings['baudRate'] = baudRate
        
        # Servo ID
        highestServoId = None
        while not highestServoId:
            hsiTest = raw_input("Please enter the highest ID of the connected servos: ")
            highestServoId = validateInput(hsiTest, 1, 255)
        
        settings['highestServoId'] = highestServoId


        highestServoId = settings['highestServoId']

        # Establish a serial connection to the dynamixel network.
        # This usually requires a USB2Dynamixel
        serial = dynamixel.SerialStream(port=settings['port'],
                                        baudrate=settings['baudRate'],
                                        timeout=1)
        # Instantiate our network object
        net = dynamixel.DynamixelNetwork(serial)
        
        # Ping the range of servos that are attached
        print "Scanning for Dynamixels..."
        net.scan(1, highestServoId)

        settings['servoIds'] = []
        print "Found the following Dynamixels IDs: "
        for dyn in net.get_dynamixels():
            print dyn.id
            settings['servoIds'].append(dyn.id)

        # Make sure we actually found servos
        if not settings['servoIds']:
          print 'No Dynamixels Found!'
          sys.exit(0)

        # Save the output settings to a yaml file
        with open(settingsFile, 'w') as fh:
            yaml.dump(settings, fh)
            print("Your settings have been saved to 'settings.yaml'. \nTo " +
                   "change them in the future either edit that file or run " +
                   "this example with -c.")
    
    main(settings)