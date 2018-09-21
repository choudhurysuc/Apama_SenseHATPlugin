
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

### Hardware
   * Raspberry Pi version 3, Model B. (Untested but should also work with a v2, or v3+, but will NOT work with a v1 
   or a Zero or ZeroW. Apama needs at least ARMv7hf)
   * SenseHAT
   * Usual misc power, networking, cables   

### Software
  * Apama Core Community Edition v10.3.0 (Oct 2018 release), or later, for Linux on ARM
  * Linux installation on the RaspberryPi. Tested on Raspbian
  * Python 3.6 (to install and setup python 3.6 source : <https://github.com/kpalf/ApamaSenseHat> ) .
 
  
##  Test framework  : (Using the SenseHAT, via Plugin, from Apama EPL )
  Using PySys framework , can test the senseHAT EPL API functionality.
  Following are examples to play a Raspberry Pi SenseHAT device using senseHAT EPL API's from 
  Apama EPL running in a Correlator process.
  
  - senseHAT_001 : verify senseHAT plugin basic functionality
  - senseHAT_002 : RandomSparkles example
  - senseHAT_003 : Temperature Bar Graph example
  
  ## Sample EPL Code
  ```
  package com.apmax.test;
using com.apamax.sensehat.SenseHat;
using com.apamax.sensehat.Color;
 
/** Sample to access SenseHAT information using EPL API's .......  */
 
monitor SenseHATSample {
 
    action onload() {
 
        log "Loaded monitor SenseHATSample" at INFO;
 
        SenseHat senseHat := SenseHat.create();
 
        //clear LED Matrx
        senseHat.ledMatrix.clear();
 
        //display message
        senseHat.ledMatrix.showMessage("APAMA TEST");
 
        //Set pixel
        Color c := Color.Of(255, 0, 0);
        senseHat.ledMatrix.setPixel(0, 0, c);
 
        //Get measurements
        float t := senseHat.envSensor.getTemperature();
        float p := senseHat.envSensor.getPressure();
        float h := senseHat.envSensor.getHumidity();
 
        string msg := "Temperature = " + t.toString() +" Pressure= " + p.toString() + " Humidity= " + h.toString();
 
        senseHat.ledMatrix.showMessageWithParam(msg, 0.05, Color.Of(255, 255, 255) ,Color.Of(0, 100, 0));
 
        senseHat.ledMatrix.clear();
    }
}
  ```
  
