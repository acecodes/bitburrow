import os
from flask import Flask, request, flash, url_for, render_template
from jinja2 import Template
from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired

app = Flask(__name__)

title = "AceCodes Presents: The Code Engine"
desc = 'A web app for encoding and decoding messages using various code systems'
author = 'Ace Eddleman'

app.config.from_object('config')

class MyForm(Form):
    encoderform = TextField('encoderform', validators=[DataRequired()])

""""
Begin Morse Code
"""

"""
THIS CODE IS A WORK IN PROGRESS AND NOT RUNNING YET!
"""
class CodeType:

	ABCs = list('abcdefghijklmnopqrstuvwxyz')
	punctuation = ['!', '?', '\'', ';', ','] # A list of punctuation marks
	numbers = []
	alphabet = []

	def __init__(self, name):
		self.name = name

class Morse(CodeType):

	# Morse Code Generator/Translator
	# Functions for creating or translating Morse code messages.

	numbers = ['-----', '.----', '..---', '...--',
	'....-','.....','-....','--...','---..','----.']

	alphabet = ['.-', '-...', '-.-.', '-..', '.', '..-.','--.','....',
	'..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.',
	'...','-','..-','..-','.--','-.--','--..']

	alpha = dict(zip(CodeType.ABCs, alphabet))
	nums = dict(enumerate(numbers))

	def encode(self, string):
		string = string.lower()

		result = []

		for chars in string:
			if chars in self.alpha:
				result.append(self.alpha[chars])
			elif chars in self.nums:
				result.append(self.nums[chars])
			elif chars == ' ':
				result.append(' ')
			else:
				continue

		return ' '.join(result)

MCode = Morse('Morse Code')

"""
End Morse Code
"""

@app.route('/')
def front_page():
	form = MyForm()
	return render_template('index.html', title=title, desc=desc, author=author, form=form)

@app.route('/encoded_message', methods=['POST'])
def encoded_message():
	encoder_form = request.form['encoderform']
	return render_template('encoded_message.html', title=title, desc=desc, author=author, encoder_form=encoder_form, encode=MCode.encode)


if __name__ == '__main__':
	app.run(debug=True)