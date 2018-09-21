from pysys.basetest import BaseTest
from apama.correlator import CorrelatorHelper
import RPi.GPIO as GPIO
import os

class SenseHATBaseTest(BaseTest):

	def __init__(self, descriptor, outsubdir, runner):
		BaseTest.__init__(self, descriptor, outsubdir, runner)
		
		self.BASE_DIR = os.path.join(self.project.root, '..')
		self.config = os.path.join(self.BASE_DIR, 'config','CorrelatorConfig.yaml')
		os.environ["LD_LIBRARY_PATH"] = self.BASE_DIR + os.pathsep + "/usr/local/lib" + os.pathsep + os.environ["LD_LIBRARY_PATH"]
		os.environ["AP_PYTHONHOME"] = '/usr/local'
		
	def start(self):
		self.correlator = CorrelatorHelper(self)
		self.correlator.start(config=self.config)
		self.correlator.injectMonitorscript(filenames=[os.path.join(self.BASE_DIR, 'monitors','utils','SenseHATHelper.mon')])
		self.correlator.injectMonitorscript(filenames=[os.path.join(self.BASE_DIR, 'monitors','api','SenseHATAPI.mon')])
		
