# Runs a functional test on BitBurrow to ensure it is working
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest

test_english = 'Hello world!'
test_morse = ".... . .-.. .-.. --- .-- --- .-. .-.. -.. -.-.--"

local_test = True

if local_test == True:
	url = 'http://localhost:5000'
else:
	url = 'http://www.bitburrow.com'


class BitBurrowTester(unittest.TestCase):
	# Create browser driver and open the page
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.get(url)
		self.assertIn('BitBurrow', self.browser.title)
		
	# Run a test of the encoding function
	def test_encoder(self):
		encoder_input = self.browser.find_element_by_name('encoder_message')
		encoder_input.send_keys(test_english)
		encoder_input.send_keys(Keys.RETURN)
		sleep(5)

	def test_decoder(self):
		decoder_input = self.browser.find_element_by_name('decoder_message')
		decoder_input.send_keys(test_morse)
		decoder_input.send_keys(Keys.RETURN)
		sleep(5)

	# Close the browser window
	def tearDown(self):
		self.browser.close()

if __name__ == '__main__':
	unittest.main()