'''
	A python helpers to get Sense HAT API
	Copyright (c) 2018 Suresh C
'''

from sense_hat import SenseHat , ACTION_RELEASED
from apama.eplplugin import EPLAction, EPLPluginBase, Correlator, Event


class SenseHATPlugin(EPLPluginBase):
	
	def __init__(self,init):
		super(SenseHATPlugin,self).__init__(init)
		self.getLogger().info("SenseHATPlugin initialised with config: %s" % self.getConfig())
		self.sense = SenseHat()
			
	@EPLAction("action<integer >")
	def setRotation(self,angle=None):
		"""
		Orientation of the message/image 
		
		@param message:	Orientation of the message, The supported values of orientation are 0, 90, 180, and 270..
		"""
		if angle == None : angle = 90
		
		self.sense.set_rotation(angle)
	
	@EPLAction("action<integer, integer, integer, integer, integer >")	
	def setPixel(self, x, y, r, g, b):
		self.sense.set_pixel(x, y, r, g, b)
		
		
		
	@EPLAction("action< sequence <sequence <integer> > >")	
	def setPixels(self, pixels):
		if not isinstance(pixels, list) : return;
		self.sense.set_pixels(pixels)
		
	@EPLAction("action< >")	
	def clear(self):
		self.sense.clear()
	
	@EPLAction("action< integer, integer, integer >")
	def Clear(self,  r, g, b):
		self.sense.clear(r, g, b)
	
	
	@EPLAction("action<string >")
	def showMessage(self,message):
		self.sense.show_message(message)
	
			
	@EPLAction("action<string, float, sequence<integer>, sequence<integer> >")
	def displayMessage(self,message,scrollingSpeed=None, textColor=None, backgroundColor=None):
		"""
		This method will scrolls a text message across the LED Matrix.
				
		@param message:	The Scrolling message to be displayed.
		@param scrollingSpeed:	Scrolling message speed.
		@param textColor:	 The text color of the scrolling message i.e [R G B] .
		@param backgroundColor:	 The background color of the scrolling message [R G B].
		
		"""
		if scrollingSpeed == None : scrollingSpeed = 0.1
		if (textColor == None) or (not isinstance(textColor, list)) : textColor = [255, 255, 255]
		if (backgroundColor == None) or (not isinstance(backgroundColor, list)) : backgroundColor = [0, 0, 0] 
		
		self.sense.show_message(message, scroll_speed=scrollingSpeed, text_colour=textColor, back_colour=backgroundColor)
		
	@EPLAction("action<string >")
	def showLetter(self, letter):
		if not isinstance(letter, basestring) : return;
		self.sense.show_letter(letter)
	
	@EPLAction("action<boolean >")
	def lowLight(self, islowLight):
		self.sense.low_light = islowLight
	
	@EPLAction("action<string >")
	def loadImage(self, imagePath):
		self.sense.load_image(imagePath)
	
	
	
	##########################################################################################################
	
	#				Environmental sensors 
	
	##########################################################################################################
	
	
	@EPLAction("action<> returns float")
	def getHumidity(self):
		humidity = self.sense.get_humidity()
		return round(humidity,2);
	
	
	@EPLAction("action<> returns float")
	def getTemperature(self):
		temp  = self.sense.get_temperature()
		return round(temp,2) ;
	
	
	@EPLAction("action<> returns float")
	def getTemperatureFromHumidity(self):
		temp = self.sense.get_temperature_from_humidity()
		return round(temp,2) ;
	
	@EPLAction("action<> returns float")
	def getTemperatureFromPressure(self):
		temp  = self.sense.get_temperature_from_pressure()
		return round(temp,2) ;
	
	@EPLAction("action<> returns float")
	def getPressure(self):
		pressure = self.sense.get_pressure()
		return round(pressure,2)  ;
	
	##########################################################################################################
	
	#				Joystick 
	
	##########################################################################################################
	
	@EPLAction("action<boolean > returns com.apamax.sensehat.InputEvent")
	def waitForEvent(self, emptyBuffer=False):
		jevent = self.sense.stick.wait_for_event(emptybuffer=emptyBuffer)		
		evtInstance = Event('com.apamax.sensehat.InputEvent', {"actionValue": jevent.action , "directionValue": jevent.direction , "timestamp": jevent.timestamp })
		return evtInstance;
	
	@EPLAction("action<> returns sequence<com.apamax.sensehat.InputEvent >")
	def getEvents(self):
		
		events = list()
		for event in self.sense.stick.get_events():
			evtInstance = Event('com.apamax.sensehat.InputEvent', {"actionValue": jevent.action , "directionValue": jevent.direction , "timestamp": jevent.timestamp })
			events.append(evtInstance)
			
		return events;
	
	def pushed_up(event):
	    if event.action == ACTION_RELEASED:
	        joyevt = Event('com.apamax.sensehat.JoystickControl', {"controlType": 1})
	        Correlator.sendTo("sensedhat_data", joyevt)

	def pushed_down(event):
	    if event.action == ACTION_RELEASED:
	        joyevt = Event('com.apamax.sensehat.JoystickControl', {"controlType": 2})
	        Correlator.sendTo("sensedhat_data", joyevt)
	
	def pushed_left(event):
	    if event.action == ACTION_RELEASED:
	        joyevt = Event('com.apamax.sensehat.JoystickControl', {"controlType": 3})
	        Correlator.sendTo("sensedhat_data", joyevt)
	
	def pushed_right(event):
	    if event.action == ACTION_RELEASED:
	        joyevt = Event('com.apamax.sensehat.JoystickControl', {"controlType": 4})
	        Correlator.sendTo("sensedhat_data", joyevt)
	
	def pushed_in(event):
	    if event.action == ACTION_RELEASED:
	    	self.sense.show_message(str(round(sense.temp,1)),0.05,b)		 


	##########################################################################################################
	
	#				IMU Sensor 
	
	##########################################################################################################
	
	@EPLAction("action<boolean, boolean, boolean >")
	def setIMUConfig(self, compassEnabled, gyroscopeEnabled, accelerometerEnabled):
		
		'''
     	Enables and disables the gyroscope, accelerometer and/or magnetometer contribution to the get orientation functions
     
     	@param compassEnabled :        enable compass
     	@param gyroscopeEnabled :      enable gyroscope
      	@param accelerometerEnabled :  enable accelerometer
      	
     	'''
		self.sense.set_imu_config(compassEnabled, gyroscopeEnabled, accelerometerEnabled)
		
	
	@EPLAction("action< > returns com.apamax.sensehat.IMUData")
	def getOrientationRadians(self):
		
		'''		
     	Gets the current orientation in radians using the aircraft principal axes of pitch, roll and yaw
     
     	@return event with pitch, roll and yaw values. Values are floats representing the angle of the axis in radians
     
		'''
		
		pitch, roll, yaw = self.sense.get_orientation_radians().values()		
		evtInstance = Event('com.apamax.sensehat.IMUData', {"pitch": pitch , "roll": roll , "yaw": yaw })
		return evtInstance;
	
	
	@EPLAction("action< > returns com.apamax.sensehat.IMUData")
	def getOrientationDegrees(self):
		
		'''		
     	Gets the current orientation in degrees using the aircraft principal axes of pitch, roll and yaw
     
     	@return event with pitch, roll and yaw values. Values are Floats representing the angle of the axis in degrees
     
		'''
		
		pitch, roll, yaw = self.sense.get_orientation_degrees().values()		
		evtInstance = Event('com.apamax.sensehat.IMUData', {"pitch": pitch , "roll": roll , "yaw": yaw })
		return evtInstance;
		
	
		
	@EPLAction("action< > returns com.apamax.sensehat.IMUData")
	def getOrientation(self):
		
		'''
     	@return event with pitch, roll and yaw representing the angle of the axis in degrees
     
		'''
		
		pitch, roll, yaw = self.sense.get_orientation().values()		
		evtInstance = Event('com.apamax.sensehat.IMUData', {"pitch": pitch , "roll": roll , "yaw": yaw })
		return evtInstance;	
	
	
	@EPLAction("action< > returns float")
	def getCompass(self):
		
		'''
		Calls set_imu_config internally in Python core to disable the gyroscope and accelerometer
     	then gets the direction of North from the magnetometer in degrees
     
     	@return The direction of North
     	
		'''
		return self.sense.get_compass()
		
	
	@EPLAction("action< > returns com.apamax.sensehat.IMUDataRaw")
	def getCompassRaw(self):
		
		'''
		
     	Gets the raw x, y and z axis magnetometer data     
     	@return event representing the magnetic intensity of the axis in microteslas (uT)
     
     	'''
		x, y, z = self.sense.get_compass_raw().values()
		evtInstance = Event('com.apamax.sensehat.IMUDataRaw', {"x": x , "y": y , "z": z })
		return evtInstance;	
	 
		
	@EPLAction("action< > returns com.apamax.sensehat.IMUData")
	def getGyroscope(self):
		
		'''
		Calls set_imu_config internally in Python core to disable the magnetometer and accelerometer
     	then gets the current orientation from the gyroscope only
     	
     	@return event with pitch, roll and yaw representing the angle of the axis in degrees
     
		'''
		
		pitch, roll, yaw = self.sense.get_gyroscope().values()		
		evtInstance = Event('com.apamax.sensehat.IMUData', {"pitch": pitch , "roll": roll , "yaw": yaw })
		return evtInstance;	
	
		
	@EPLAction("action< > returns com.apamax.sensehat.IMUDataRaw")
	def getGyroscopeRaw(self):
		
		'''		
     	Gets the raw x, y and z axis gyroscope data     
     	@return event representing the rotational intensity of the axis in radians per second
     
     	'''
		x, y, z = sense.get_gyroscope_raw().values()
		evtInstance = Event('com.apamax.sensehat.IMUDataRaw', {"x": x , "y": y , "z": z })
		return evtInstance;
	
	@EPLAction("action< > returns com.apamax.sensehat.IMUData")
	def getAccelerometer(self):
		
		'''
		Calls set_imu_config in Python core to disable the magnetometer and gyroscope
        then gets the current orientation from the accelerometer only
     
        @return Object representing the angle of the axis in degrees
             
		'''
		
		pitch, roll, yaw = self.sense.get_accelerometer().values()		
		evtInstance = Event('com.apamax.sensehat.IMUData', {"pitch": pitch , "roll": roll , "yaw": yaw })
		return evtInstance;	
	
		
	@EPLAction("action< > returns com.apamax.sensehat.IMUDataRaw")
	def getAccelerometerRaw(self):
		
		'''		
     	Gets the raw x, y and z axis accelerometer data    
     	@return event representing the acceleration intensity of the axis in Gs
     
     	'''
		x, y, z = sense.get_accelerometer_raw().values()
		evtInstance = Event('com.apamax.sensehat.IMUDataRaw', {"x": x , "y": y , "z": z })
		return evtInstance;
	
	
	 
	
		
		
		
		