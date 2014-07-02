import os
from flask import Flask, request, flash, url_for, render_template, redirect
from jinja2 import Template
from flask_wtf import Form
from flask_mail import Mail, Message
from wtforms import TextField
from wtforms.validators import Required, Email
import re
import time




app = Flask(__name__)
mail = Mail(app)

title = "BitBurrow"
desc = 'A web app for encoding and decoding messages using various code systems'
author = 'Ace Eddleman'
year = time.strftime("%Y")


app.config.from_object('config')

class EncoderForm(Form):
    encoder_message = TextField('encoder_message', [Required()])
    
class DecoderForm(Form):
    decoder_message = TextField('decoder_message', [Required()])

class SendtoFriend(Form):
	friend = TextField('friend', [Email('Enter a valid e-mail address')])
	you = TextField('you', validators=[Required('Please enter a name')])

""""
Begin Morse Code
"""

class CodeType:

	ABCs = list('abcdefghijklmnopqrstuvwxyz')
	Numbers = list('012345679')
	Punctuation = '.,?\'!/)(&:;=+-_"$@ ' # A list of punctuation marks
	acceptable_encoding_inputs = ABCs + Numbers + list(Punctuation)
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

	acceptable_decoding_inputs = numbers + alphabet + punctuation

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
			if chars not in CodeType.acceptable_encoding_inputs:
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
			if chars not in self.acceptable_decoding_inputs:
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
	print(encoderform.errors)
	print(decoderform.errors)
	return render_template('index.html', title=title, desc=desc, author=author, encoderform=encoderform, decoderform=decoderform, year=year)

@app.route('/encoded_message', methods=['POST'])
def encoded_message():
	page_title = 'Your encoded message'
	send = SendtoFriend()
	encoder_form = request.form['encoder_message']
	print(send.errors)
	if send.validate_on_submit():
		return redirect(url_for('sent_message'))
	return render_template('encoded_message.html', title=title, desc=desc, page_title=page_title, author=author, encoder_form=encoder_form, encode=MCode.encode, year=year, send=send)

@app.route('/decoded_message', methods=['POST'])
def decoded_message():
	page_title = 'Your decoded message'
	decoder_form = request.form['decoder_message']
	return render_template('decoded_message.html', title=title, desc=desc, page_title=page_title, author=author, decoder_form=decoder_form, decode=MCode.decode, year=year)

@app.route('/sent', methods=['POST'])
def sent_message():
	page_title = 'Your sent message'
	friend = request.form['friend']
	you = request.form['you']
	msg = Message('Your Friend {you} Sent You A Coded Message!'.format(you=you), sender='donotreply@bitburrow.com', recipients=friend)

	return render_template('sent.html', title=title, desc=desc, page_title=page_title, author=author, year=year, friend=friend)

if __name__ == '__main__':
	app.run(debug=True)