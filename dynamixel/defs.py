#!/usr/bin/env python2.6

"""
This is a Python version of the ForestMoon Dynamixel library originally
written in C# by Scott Ferguson.

The Python version was created by Patrick Goebel (mailto:patrick@pirobot.org)
for the Pi Robot Project which lives at http://www.pirobot.org.

The original license for the C# version is as follows:

This software was written and developed by Scott Ferguson.
The current version can be found at http://www.forestmoon.com/Software/.
This free software is distributed under the GNU General Public License.
See http://www.gnu.org/licenses/gpl.html for details.
This license restricts your usage of the software in derivative works.

* * * * * 

Module wide definitions

"""

import enumeration

ERROR_STATUS = enumeration.Enumeration( [
    ('None',0x0,"None"),
    ('InputVoltage', 0x1, "Input Voltage Error"),
    ('AngleLimit', 0x2, "Angle Limit Error"),
    ('Overheating', 0x4, "Overheating Error"),
    ('Range', 0x8,"Range Error"),
    ('Checksum', 0x10,"Checksum Error"),
    ('Overload', 0x20,"Overload Error"),
    ('Instruction', 0x40,"Instruction Error" ) ] )

BAUD_RATE = enumeration.Enumeration( [
    ('Baud_1000000', 1),
    ('Baud_500000', 3),
    ('Baud_400000', 4),
    ('Baud_250000', 7),
    ('Baud_200000', 9),
    ('Baud_115200', 0x10),
    ('Baud_57600', 0x22),
    ('Baud_19200', 0x67),
    ('Baud_9600', 0xcf) ] )

REGISTER_AX12 = enumeration.Enumeration( [
    ('ModelNumber',  0, "Model Number"),
    ('FirmwareVersion',  2, "Firmware Version"),
    ('Id', 3, "Id"),
    ('BaudRate',  4, "Baud Rate"),
    ('ReturnDelay',  5, "Return Delay"),
    ('CWAngleLimit',  6, "CW Angle Limit"),
    ('CCWAngleLimit',  8, "CCW Angle Limit"),
    ('TemperatureLimit',  11, "Temperature Limit"),
    ('LowVoltageLimit',  12, "Low Voltage Limit"),
    ('HighVoltageLimit',  13, "High Voltage Limit"),
    ('MaxTorque',  14, "Max Torque"),
    ('StatusReturnLevel',  16, "Status Return Level"),
    ('AlarmLED',  17, "Alarm Led"),
    ('AlarmShutdown',  18, "Alarm Shutdown"),
    ('DownCalibration',  20, "Down Calibration"),
    ('UpCalibration',  22, "Up Calibration"),
    ('TorqueEnable',  24, "Torque Enable"),
    ('LED',  25, "LED"),
    ('CWComplianceMargin',  26, "CW Compliance Margin"),
    ('CCWComplianceMargin',  27, "CCW Compliance Margin"),
    ('CWComplianceSlope',  28, "CW Compliance Slope"),
    ('CCWComplianceSlope',  29, "CCW Compliance Slope"),
    ('GoalPosition', 30, "Goal Position"),
    ('MovingSpeed', 32, "Moving Speed"),
    ('TorqueLimit',  34, "Torque Limit"),
    ('CurrentPosition',  36, "Current Position"),
    ('CurrentSpeed',  38, "Current Speed"),
    ('CurrentLoad',  40, "Current Load"),
    ('CurrentVoltage',  42, "Current Voltage"),
    ('CurrentTemperature',  43, "Current Temperature"),
    ('RegisteredInstruction',  44, "Registered Instruction"),
    ('Moving',  46, "Moving"),
    ('Lock',  47, "Lock"),
    ('Punch',  48, "Punch" ) ] )

REGISTER_AXS1 = enumeration.Enumeration( [
    ('ModelNumber',  0, "Model Number"),
    ('FirmwareVersion',  2, "Firmware Version"),
    ('Id', 3, "Id"),
    ('BaudRate',  4, "Baud Rate"),
    ('ReturnDelay',  5, "Return Delay"),
    ('TemperatureLimit',  11, "Temperature Limit"),
    ('LowVoltageLimit',  12, "Low Voltage Limit"),
    ('HighVoltageLimit',  13, "High Voltage Limit"),
    ('StatusReturnLevel',  16, "Status Return Level"),
    ('ObstacleDetectedCompVal',  20, "Obstacle Detected Comparison Value"),
    ('LightDetectedCompVal',  21, "Light Detected Comparison Value"),
    ('LeftIrSensorValue',  26, "Left IR Sensor Value"),
    ('CenterIrSensorValue',  27, "Center IR Sensor Value"),
    ('RightIrSensorValue',  28, "Right IR Sensor Value"),
    ('LeftLumin',  29, "Left Luminosity"),
    ('CenterLumin', 30, "Center Luminosity"),
    ('RightLumin', 31, "Right Luminosity"),
    ('ObstacleDetectedFlag',  32, "Obstacle Detected Flag"),
    ('LuminDetectedFlag',  33, "Luminosity Detected Flag"),
    ('SoundValue',  35, "Sound Value"),
    ('SoundValueMax',  36, "Stored Max Sound Value"),
    ('SoundDetectedCount',  37, "Sound Detected Count"),
    ('SoundDetectedTime',  38, "Sound Detected Time"),
    ('BuzzerIndex',  40, "Note to play (0-51)"),
    ('BuzzerTime',  41, "How long to play note, plus special values. See Manual"),
    ('CurrentVoltage',  42, "Current Voltage" ),
    ('CurrentTemperature',  43, "Current Temperature" ),
    ('RegisteredInstruction',  44, "Registered Instruction" ),
    ('IrRemoconArrived',  46, "2 byte IR Instruction Recieved" ),
    ('Lock',  47, "Lock" ),
    ('IrRemoconRxData0',  48, "Recieved IR Data, first byte" ),
    ('IrRemoconRxData1',  49, "Recieved IR Data, second byte" ),
    ('IrRemoconTxData0',  50, "IR Data to Send, first byte" ),
    ('IrRemoconTxData1',  51, "IR Data to Send, second byte" ),
    ('ObstacleDetectedComp',  52, "Obstacle Detected Compare Value" ),
    ('LightDetectedComp',  53, "Light Detected Compare Value" ) ] )

DEVICE = enumeration.Enumeration( [
    ('AX12', REGISTER_AX12, 'AX-12 Servo'),
    ('AXS1', REGISTER_AXS1, 'AX-S1 Sensor Module') ] )

STATUS_RETURN_LEVEL = enumeration.Enumeration( [
    ('NoResponse', 0),
    ('RespondToReadData', 1),
    ('RespondToAll', 2 )] )

INSTRUCTION = enumeration.Enumeration( [
    ('Ping', 1, "Respond only with a status packet."),
    ('ReadData', 2, "Read register data."),
    ('WriteData', 3, "Write register data."),
    ('RegWrite', 4, "Delay writing register data until an Action \
    instruction is received."),
    ('Action', 5, "Perform pending RegWrite instructions."),
    ('Reset', 6, "Reset all registers (including ID) to default values."),
    ('SyncWrite',  0x83, "Write register data to multiple \
    Dynamixels at once. ") ] )
