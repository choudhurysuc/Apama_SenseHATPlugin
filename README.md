
# Apama SenseHat Python Plugin

The ApamaSenseHAT plugin is python based plugin and provides an EPL wrapper for Sense Hat API's.

From APAMA application, user can  drive a Raspberry Pi SenseHAT device with this plugin and EPL API's. 
user can access information(i.e measurements of temperature,humidity, pressure and orientation) and 
publish the output (using its built-in LED matrix) from/to  SenseHAT using thease EPL API's .

Supported EPL API (i.e components) :

    Environmental sensors
    IMU (inertial measurement unit)
    LED Matrix
    Joystick 

# Hardware

    Raspberry Pi version 3, Model B. (Untested but should also work with a v2, or v3+, but will NOT work with a v1 or a Zero or ZeroW. Apama needs at least ARMv7hf)
    SenseHAT
    Usual misc power, networking, cables
    For the Sense Hat install 'I2C' should be enabled in the 'interfaces' section of raspi-config. ( sudo raspi-config - option 5 then P5 )

# Software

    Apama Core Community Edition v10.3.0 (Oct 2018 release), or later, for Linux on ARM
    Linux installation on the RaspberryPi. Tested on Raspbian
    Python 3.6 (to install and setup python 3.6 source : https://github.com/kpalf/ApamaSenseHat)
  
#  Test framework  : (Using the SenseHAT, via Plugin, from Apama EPL )
  using PySys framework , can test the senseHAT EPL API functionality.
  Following are examples to play a Raspberry Pi SenseHAT device using senseHAT EPL API's from 
  Apama EPL running in a Correlator process.
  
  - senseHAT_001 : verify senseHAT plugin basic functionality
  - senseHAT_002 : RandomSparkles example
  - senseHAT_003 : Temperature Bar Graph example
