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
    ('None', 0x0, {'textDesc': "None"}),
    ('InputVoltage', 0x1, {'textDesc': "Input Voltage Error"}),
    ('AngleLimit', 0x2, {'textDesc': "Angle Limit Error"}),
    ('Overheating', 0x4, {'textDesc': "Overheating Error"}),
    ('Range', 0x8, {'textDesc': "Range Error"}),
    ('Checksum', 0x10, {'textDesc': "Checksum Error"}),
    ('Overload', 0x20, {'textDesc': "Overload Error"}),
    ('Instruction', 0x40, {'textDesc': "Instruction Error"}) ] )

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
    ('ModelNumber',  0, {'registerLen': 2, 'textDesc': "Model Number"}),
    ('FirmwareVersion',  2, {'registerLen': 1, 'textDesc': "Firmware Version"}),
    ('Id', 3, {'registerLen': 1, 'textDesc': "Id"}),
    ('BaudRate',  4, {'registerLen': 1, 'textDesc': "Baud Rate"}),
    ('ReturnDelay',  5, {'registerLen': 1, 'textDesc': "Return Delay"}),
    ('CWAngleLimit',  6, {'registerLen': 2, 'textDesc': "CW Angle Limit"}),
    ('CCWAngleLimit',  8, {'registerLen': 2, 'textDesc': "CCW Angle Limit"}),
    ('TemperatureLimit',  11, {'registerLen': 1, 'textDesc': "Temperature Limit"}),
    ('LowVoltageLimit',  12, {'registerLen': 1, 'textDesc': "Low Voltage Limit"}),
    ('HighVoltageLimit',  13, {'registerLen': 1, 'textDesc': "High Voltage Limit"}),
    ('MaxTorque',  14, {'registerLen': 2, 'textDesc': "Max Torque"}),
    ('StatusReturnLevel',  16, {'registerLen': 1, 'textDesc': "Status Return Level"}),
    ('AlarmLED',  17, {'registerLen': 1, 'textDesc': "Alarm Led"}),
    ('AlarmShutdown',  18, {'registerLen': 1, 'textDesc': "Alarm Shutdown"}),
    ('DownCalibration',  20, {'registerLen': 2, 'textDesc': "Down Calibration"}),
    ('UpCalibration',  22, {'registerLen': 2, 'textDesc': "Up Calibration"}),
    ('TorqueEnable',  24, {'registerLen': 1, 'textDesc': "Torque Enable"}),
    ('LED',  25, {'registerLen': 1, 'textDesc': "LED"}),
    ('CWComplianceMargin',  26, {'registerLen': 1, 'textDesc': "CW Compliance Margin"}),
    ('CCWComplianceMargin',  27, {'registerLen': 1, 'textDesc': "CCW Compliance Margin"}),
    ('CWComplianceSlope',  28, {'registerLen': 1, 'textDesc': "CW Compliance Slope"}),
    ('CCWComplianceSlope',  29, {'registerLen': 1, 'textDesc': "CCW Compliance Slope"}),
    ('GoalPosition', 30, {'registerLen': 2, 'textDesc': "Goal Position"}),
    ('MovingSpeed', 32, {'registerLen': 2, 'textDesc': "Moving Speed"}),
    ('TorqueLimit',  34, {'registerLen': 2, 'textDesc': "Torque Limit"}),
    ('CurrentPosition',  36, {'registerLen': 2, 'textDesc': "Current Position"}),
    ('CurrentSpeed',  38, {'registerLen': 2, 'textDesc': "Current Speed"}),
    ('CurrentLoad',  40, {'registerLen': 2, 'textDesc': "Current Load"}),
    ('CurrentVoltage',  42, {'registerLen': 1, 'textDesc': "Current Voltage"}),
    ('CurrentTemperature',  43, {'registerLen': 1, 'textDesc': "Current Temperature"}),
    ('RegisteredInstruction',  44, {'registerLen': 1, 'textDesc': "Registered Instruction"}),
    ('Moving',  46, {'registerLen': 1, 'textDesc': "Moving"}),
    ('Lock',  47, {'registerLen': 1, 'textDesc': "Lock"}),
    ('Punch',  48, {'registerLen': 2, 'textDesc': "Punch"} ) ] )

REGISTER_AXS1 = enumeration.Enumeration( [
    ('ModelNumber',  0, {'registerLen': 2, 'textDesc': "Model Number"}),
    ('FirmwareVersion',  2, {'registerLen': 1, 'textDesc': "Firmware Version"}),
    ('Id', 3, {'registerLen': 1, 'textDesc': "Id"}),
    ('BaudRate',  4, {'registerLen': 1, 'textDesc': "Baud Rate"}),
    ('ReturnDelay',  5, {'registerLen': 1, 'textDesc': "Return Delay"}),
    ('TemperatureLimit',  11, {'registerLen': 1, 'textDesc': "Temperature Limit"}),
    ('LowVoltageLimit',  12, {'registerLen': 1, 'textDesc': "Low Voltage Limit"}),
    ('HighVoltageLimit',  13, {'registerLen': 1, 'textDesc': "High Voltage Limit"}),
    ('StatusReturnLevel',  16, {'registerLen': 1, 'textDesc': "Status Return Level"}),
    ('ObstacleDetectedCompVal',  20, {'registerLen': 1, 'textDesc': "Obstacle Detected Comparison Value"}),
    ('LightDetectedCompVal',  21, {'registerLen': 1, 'textDesc': "Light Detected Comparison Value"}),
    ('LeftIrSensorValue',  26, {'registerLen': 1, 'textDesc': "Left IR Sensor Value"}),
    ('CenterIrSensorValue',  27, {'registerLen': 1, 'textDesc': "Center IR Sensor Value"}),
    ('RightIrSensorValue',  28, {'registerLen': 1, 'textDesc': "Right IR Sensor Value"}),
    ('LeftLumin',  29, {'registerLen': 1, 'textDesc': "Left Luminosity"}),
    ('CenterLumin', 30, {'registerLen': 1, 'textDesc': "Center Luminosity"}),
    ('RightLumin', 31, {'registerLen': 1, 'textDesc': "Right Luminosity"}),
    ('ObstacleDetectedFlag',  32, {'registerLen': 1, 'textDesc': "Obstacle Detected Flag"}),
    ('LuminDetectedFlag',  33, {'registerLen': 1, 'textDesc': "Luminosity Detected Flag"}),
    ('SoundValue',  35, {'registerLen': 1, 'textDesc': "Sound Value"}),
    ('SoundValueMax',  36, {'registerLen': 1, 'textDesc': "Stored Max Sound Value"}),
    ('SoundDetectedCount',  37, {'registerLen': 1, 'textDesc': "Sound Detected Count"}),
    ('SoundDetectedTime',  38, {'registerLen': 2, 'textDesc': "Sound Detected Time"}),
    ('BuzzerIndex',  40, {'registerLen': 1, 'textDesc': "Note to play (0-51)"}),
    ('BuzzerTime',  41, {'registerLen': 1, 'textDesc': "How long to play note, plus special values. See Manual"}),
    ('CurrentVoltage',  42, {'registerLen': 1, 'textDesc': "Current Voltage"}),
    ('CurrentTemperature',  43, {'registerLen': 1, 'textDesc': "Current Temperature"}),
    ('RegisteredInstruction',  44, {'registerLen': 1, 'textDesc': "Registered Instruction"}),
    ('IrRemoconArrived',  46, {'registerLen': 1, 'textDesc': "2 byte IR Instruction Recieved"}),
    ('Lock',  47, {'registerLen': 1, 'textDesc': "Lock"}),
    ('IrRemoconRxData0',  48, {'registerLen': 1, 'textDesc': "Recieved IR Data, first byte"}),
    ('IrRemoconRxData1',  49, {'registerLen': 1, 'textDesc': "Recieved IR Data, second byte"}),
    ('IrRemoconTxData0',  50, {'registerLen': 1, 'textDesc': "IR Data to Send, first byte"}),
    ('IrRemoconTxData1',  51, {'registerLen': 1, 'textDesc': "IR Data to Send, second byte"}),
    ('ObstacleDetectedComp',  52, {'registerLen': 1, 'textDesc': "Obstacle Detected Compare Value"}),
    ('LightDetectedComp',  53, {'registerLen': 1, 'textDesc': "Light Detected Compare Value"}) ] )

DEVICE = enumeration.Enumeration( [
    ('AX12', REGISTER_AX12, 'AX-12 Servo'),
    ('AXS1', REGISTER_AXS1, 'AX-S1 Sensor Module') ] )

STATUS_RETURN_LEVEL = enumeration.Enumeration( [
    ('NoResponse', 0),
    ('RespondToReadData', 1),
    ('RespondToAll', 2 )] )

INSTRUCTION = enumeration.Enumeration( [
    ('Ping', 1, {'textDesc': "Respond only with a status packet."}),
    ('ReadData', 2, {'textDesc': "Read register data."}),
    ('WriteData', 3, {'textDesc': "Write register data."}),
    ('RegWrite', 4, {'textDesc': "Delay writing register data until an Action \
    instruction is received."}),
    ('Action', 5, {'textDesc': "Perform pending RegWrite instructions."}),
    ('Reset', 6, {'textDesc': "Reset all registers (including ID) to default values."}),
    ('SyncWrite',  0x83, {'textDesc': "Write register data to multiple \
    Dynamixels at once. "}) ] )
