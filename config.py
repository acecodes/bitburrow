import os

if os.path.exists('localtesting.py') == True:
	SECRET_KEY = "tK7tX64BINg5r178&i**"

else:
	os.environ['SECRET_KEY']

CSRF_ENABLED = True