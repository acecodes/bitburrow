import os

if os.path.exists('localtesting.py') == True:
	SECRET_KEY = "NotARealKey!"

else:
	SECRET_KEY = os.environ['SECRET_KEY']

CSRF_ENABLED = True