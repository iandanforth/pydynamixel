# pydynamixel

This is a Python version of the ForestMoon Dynamixel library originally written
in C# by Scott Ferguson.

The Python version was created for the Pi Robot Project
(mailto:patrick@pirobot.org) which lives at http://www.pirobot.org.

This github fork of the project is maintained by Ian Danforth.

## Installation

    $ sudo pip install dynamixel

## Run the examples

1. Connect your USB2Dynamixel to a USB port
2. Connect at least one dynamixel servo to that
3. Connect power to the servo
4. Download the example.py from above and run it:

    $ python example.py

If you're on a Mac or on Linux you should be presented with a list of
found USB ports. You should then pick the one the USB2Dynamixel is attached to
and edit example.py so that the variable portName is set correctly.
