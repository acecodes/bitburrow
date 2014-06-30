# Runs a functional test on BitBurrow to ensure it is working
from selenium import webdriver
import unittest

class BitBurrowTester(unittest.TestCase):
	# Create browser driver and open the page
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.get('http://www.bitburrow.com')

	# Makes sure that the page is not returning an error or anything
	def test_online(self):
		self.assertIn('BitBurrow', self.browser.title)

	# Close the browser window
	def tearDown(self):
		self.browser.close()

if __name__ == '__main__':
	unittest.main()