import os
from flask import Flask, request, flash, url_for, render_template, redirect
from jinja2 import Template
from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import Required
import re
import time

app = Flask(__name__)

title = "BitBurrow"
desc = 'A web app for encoding and decoding messages using various code systems'
author = 'Ace Eddleman'
year = time.strftime("%Y")


app.config.from_object('config')

class EncoderForm(Form):
    encoder_message = TextField('encoder_message', validators=[Required()])
    
class DecoderForm(Form):
    decoder_message = TextField('decoder_message', validators=[Required()])

""""
Begin Morse Code
"""

class CodeType:

	ABCs = list('abcdefghijklmnopqrstuvwxyz')
	Numbers = list('012345679')
	Punctuation = '.,?\'!/)(&:;=+-_"$@' # A list of punctuation marks
	numbers = []
	alphabet = []

	def __init__(self, name):
		self.name = name

class CodeType:

	ABCs = list('abcdefghijklmnopqrstuvwxyz')
	Numbers = list('012345679')
	Punctuation = '.,?\'!/)(&:;=+-_"$@ ' # A list of punctuation marks
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
	'...','-','..-','...-','.--','-.--','-..-', '--..']

	punctuation = ['.-.-.-', '--..--', '..--..', '.----.', '-.-.--', '-..-.', '-..-.', '-.--.', 
					'-.--.-', '.-...', '---...', '-.-.-.', '-...-', '.-.-.', '-....-', '..--.-', '.-..-.', 
					'...-..-', '.--.-.', ' ']


	encode_alpha = dict(zip(CodeType.ABCs, alphabet))
	encode_nums = dict(enumerate(numbers))
	encode_punct = dict(zip(CodeType.Punctuation, punctuation))

	decode_alpha = dict(zip(alphabet, CodeType.ABCs))
	decode_nums = dict(zip(numbers, CodeType.Numbers))
	decode_punct = dict(zip(punctuation, CodeType.Punctuation))

	def encode(self, string):
		if string == '':
			return False

		string = string.lower()

		for chars in string:
			if chars not in (self.encode_alpha, self.encode_nums, self.encode_punct):
				return False

		result = []

		for chars in string:
			if chars in self.encode_alpha:
				result.append(self.encode_alpha[chars])
			elif chars in self.encode_nums:
				result.append(self.encode_nums[chars])
			elif chars in self.encode_punct:
				result.append(self.encode_punct[chars])
			else:
				continue

		return ' '.join(result)

	def decode(self, string):
		if string == '':
			return False

		for chars in string:
			if chars not in (self.decode_alpha, self.decode_nums, self.decode_punct):
				return False

		string = re.split(r'(\s)', string)
		result = []

		for chars in string:
			if chars in self.decode_alpha:
				result.append(self.decode_alpha[chars])
			elif chars in self.decode_nums:
				result.append(self.decode_nums[chars])
			elif chars in self.decode_punct:
				result.append(self.decode_punct[chars])
			elif chars == '':
				result.append(' ')
			else:
				continue

		return ''.join(result)

MCode = Morse('Morse Code')

"""
End Morse Code
"""

@app.route('/')
def front_page():
	encoderform = EncoderForm()
	decoderform = DecoderForm()
	return render_template('index.html', title=title, desc=desc, author=author, encoderform=encoderform, decoderform=decoderform, year=year)

@app.route('/encoded_message', methods=['GET','POST'])
def encoded_message():
	page_title = 'Your encoded message'
	encoder_form = request.form['encoder_message']
	return render_template('encoded_message.html', title=title, desc=desc, page_title=page_title, author=author, encoder_form=encoder_form, encode=MCode.encode, year=year)

@app.route('/decoded_message', methods=['GET','POST'])
def decoded_message():
	page_title = 'Your decoded message'
	decoder_form = request.form['decoder_message']
	return render_template('decoded_message.html', title=title, desc=desc, page_title=page_title, author=author, decoder_form=decoder_form, decode=MCode.decode, year=year)


if __name__ == '__main__':
	app.run(debug=True)