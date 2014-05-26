import os
from flask import Flask
from flask import render_template
from jinja2 import Template

app = Flask(__name__)
title = "AceCodes Presents: The Code Engine"

""""
Begin Morse Code
"""

"""
THIS CODE IS A WORK IN PROGRESS AND NOT RUNNING YET!
"""

ABCs = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

class CodeType:

	def __init__(self, name):
		self.name = name

class Morse(CodeType):

	# Morse Code Generator/Translator
	# Functions for creating or translating Morse code messages.

	alphabet = {'0':'-----', '1':'.----', '2':'..---', '3':'...--',
	'4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.', 'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.','g':'--.','h':'....',
	'i':'..','j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.',
	's':'...','t':'-','u':'..-','v':'..-','w':'.--','y':'-.--','z':'--..'}

	punctuation = ['!', '?', '\'', ';', ','] # A list of punctuation marks

	alpha_list = [] # Empty list that will hold only the alphanumeric characters from the alphabet dictionary
	code_list = [] # Empty list that will hodl only the Morse code from the alphabet dictionary

	# Looping through the dictionary to separate the alphanumerics and Morse code
	for k, v in sorted(alphabet.items()): 
		alpha_list.append(k)
		code_list.append(v)

	# Generates Morse code list from an English message
	# The 'plain' flag is for messages that will not be turned into lists for use by 'MorseTranslate'
	def MorseGenerate(text, plain=False):
		text = text.lower() # Make everything lower case, as case doesn't matter in Morse
		morse = [] # Create the list that will eventually hold the Morse code
		for letter in text: # Search the message for its match in Morse
			if letter in alphabet:
				morse.append(alphabet[letter])
			if letter == ' ' or letter in punctuation: # Attach punctuation or spaces as needed (periods are left out because . is 'e' in Morse)
				morse.append(letter)
		if plain != False:
			return ' '.join(morse)
		return morse

	# Translates a message in Morse code into English
	def MorseTranslate(morse):
		morse = list(morse) # Create a list out of the entered Morse code
		english = [] # Empty list for translation
		for code in morse: # Search the message for its match in English
			if code in code_list:
				x = code_list.index(code)
				english.append(alpha_list[x])
			if code == ' ' or code in punctuation: # Attach punctuation or spaces as needed
				english.append(code)
		return ''.join(english)


"""
End Morse Code
"""

@app.route('/')
def front_page():
	return render_template('index.html', title=title)

if __name__ == '__main__':
	app.run(debug=True)