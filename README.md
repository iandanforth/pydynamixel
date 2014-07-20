# pydynamixel

This is a Python version of the ForestMoon Dynamixel library originally written
in C# by Scott Ferguson.

The Python version was created for the Pi Robot Project
(mailto:patrick@pirobot.org) which lives at http://www.pirobot.org.

This github fork of the project is maintained by Ian Danforth.

## Prerequisites

- Python 2.7 (Please file a ticket if you *really* need 2.6 or 3.* support)
- pip
- pyserial
- git
- At least one Dynamixel AX-12A or AX-12+ servo.
- A USB2Dynamixel module.

## Library Installation

You can install just the library from Pypi using pip.

    $ sudo pip install dynamixel

## Source Installation

If you'd like to have access to the getting started examples or contribute to
the library, you can clone this library locally.

    $ git clone https://github.com/iandanforth/pydynamixel.git

### Run the example

- Connect your USB2Dynamixel to a USB port
- Connect at least one dynamixel servo to that
- Connect power to the servo
- Launch the example script

    $ python example.py

If you're on a Mac or on Linux you should be presented with a list of
found USB ports. Select the one to which you have attached the USB2Dynamixel
for example on my machine (a Mac) it shows up as:

    /dev/tty.usbserial-A8005k21

If you are on Windows you will need to enter the name of the correct USB port
manually.

You will then be asked to enter a baud rate, the default should work. Finally 
enter highest ID number of the attached servos.

If servos are found the script will ask if you want to move them to their home 
positions (512).

Type 'y' and they should move! If they were already at their home positions
try editing the script to move them to another position. 

If they still don't move you'll need to trouble shoot.

### Troubleshooting

- When you plug in the USB2Dynamixel to your computer does the red power LED
  light up?
    - If not your module may be defective, or your USB port may not be powered.
- When the script says "Scanning for Dynamixels ..." does the yellow LED on the
  USB2Dynamixel blink ~1/second?
    - The module is not receiving commands or is not transmitting them.
    - Try reconnecting the module, or lowering the baud rate.
- No servos are found even though they are connected.
    - Is the USB2Dynamixel set to the correct communications type? For AX-12
      servos it should be set to TTL.
- Still no servos found!
    - When you plug in the power to the servo network does the power indicator
      LED on the servo briefly light up red?
        - Double check there is really power being supplied.
        - Double check the servo network cables are firmly seated into each
          servo.
        - Otherwise the servo or cables may be defective.


