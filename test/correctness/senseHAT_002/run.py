from senseHAT.BaseTest import SenseHATBaseTest

class PySysTest(SenseHATBaseTest):

	def execute(self):
		self.start()

		self.correlator.injectMonitorscript(filenames=['TestSenseHAT.mon'])
		self.waitForSignal('correlator.out', expr='Test done')

	def validate(self):
		pass
