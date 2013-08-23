import os
import dynamixel
import time
import sys
import subprocess
import optparse
import yaml

from itertools import count

from dynamixel.defs import DEVICE

AX12 = DEVICE['AX12']
AXS1 = DEVICE['AXS1']

"""
EXAMPLE
 
The sensor module can play sounds, measure distance through IR, count claps,
and a few other things. Below you'll see how to take advantage of these
abilities.
"""

def main(settings):

    portName = settings['port']
    baudRate = settings['baudRate']
    
    # Establish a serial connection to the dynamixel network.
    # This usually requires a USB2Dynamixel
    serial = dynamixel.SerialStream(port=portName, baudrate=baudRate, timeout=1)
    net = dynamixel.DynamixelNetwork(serial)
        
    # Create our sensor object. Sensor is assumed to be at id 100
    sensor = dynamixel.SensorModule(100, net)
    
    ######################
    # Playing sounds
    
    # How long we want the note to play (.3s to 5s in tenths of seconds)
    # Notes:
    #   This resets after the note is played
    #   Use 254 as the value for continual play and then 0 to turn it off.
    sensor.buzzer_time = 10
    

    # Play a note (0-41)
    print 'Playing a note ...'
    sensor.buzzer_index = 19

    time.sleep(2)

    # Play one of the short sound sequences the S1 knows
    print "Playing a tune ..."
    sensor.buzzer_time = 255
    sensor.buzzer_index = 1

    time.sleep(2)
    
    #######################
    # Reading values from environment
    print 'Reading values from the world ...'
    
    # The sensor can hear itself play notes, so reset the counter
    sensor.sound_detected_count = 0
    
    print "Left IR \tCenter IR\tRight IR\tTemperature\tVoltage"

    for i in count(1):
        if i % 10 == 0:
            print "CLAP TWICE TO EXIT"
        if sensor.sound_detected_count >= 2:
            sys.exit(0)
        # Get our sensor values
        lir = sensor.left_ir_sensor_value
        cir = sensor.center_ir_sensor_value
        rir = sensor.right_ir_sensor_value
        temp = sensor.current_temperature
        volts = sensor.current_voltage
        print lir, '\t\t', cir, '\t\t', rir, '\t\t', temp, '\t\t', volts
        time.sleep(.5)
        
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
        
        # Save the output settings to a yaml file
        with open(settingsFile, 'w') as fh:
            yaml.dump(settings, fh)
            print("Your settings have been saved to 'settings.yaml'. \nTo " +
                   "change them in the future either edit that file or run " +
                   "this example with -c.")
    
    main(settings)