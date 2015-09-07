#!/usr/bin/python
# -*- coding: utf8 -*-
"""
Library for generating and translating Morse code
"""


class MorseCode:

    """
    Class that holds everything you need to generate or translate Morse
    """

    def __init__(self):
        self.alphabet = {'0': '-----', '1': '.----', '2': '..---', '3': '...--',
                         '4': '....-', '5': '.....', '6': '-....', '7': '--...',
                         '8': '---..', '9': '----.', 'a': '.-', 'b': '-...',
                         'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.',
                         'h': '....', 'i': '..', 'j': '.---', 'k': '-.-',
                         'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
                         'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-',
                         'v': '..-', 'w': '.--', 'y': '-.--', 'z': '--..'}

        self.punctuation = {
            '!': '−·−·−−',
            '?': '··−−··',
            '/': '−··−·',
            ';': '−·−·−·',
            ',': '−−··−−',
            '(': '−·−−·',
            ')': '−·−−·−',
            ':': '−−−···',
            '=': '−···−',
            '-': '−····−',
            '+': '·−·−·',
            '@': '·−−·−·',
            '"': '·−··−·',
            '$': '···−··−',
            '_': '··−−·−',
            '&': '·−···',
            ' ': ''}

        # Only holds alphanumeric characters
        self.alpha_list = [letter for letter in self.alphabet.keys()]
        # Only holds Morse code
        self.code_list = [code for code in self.alphabet.values()]

        # Punctuation characters
        self.punc_eng = [punc for punc in self.punctuation.keys()]
        # Punctuation Morse code
        self.punc_codes = [code for code in self.punctuation.values()]

    @staticmethod
    def generate(text):
        """
        Generates Morse code from a message in English
        """
        morse_code = MorseCode()
        # Make everything lower case, as case doesn't matter in Morse
        text = text.lower()
        morse = []  # Create the list that will eventually hold the Morse code
        for letter in text:  # Search the message for its match in Morse
            if letter in morse_code.alphabet:
                morse.append(morse_code.alphabet[letter])
            # Attach punctuation or spaces as needed (periods are left out because .
            # is 'e' in Morse)
            if letter == '':
                morse.append('')
            if letter in morse_code.punctuation:
                morse.append(morse_code.punctuation[letter])
        return ' '.join(morse)

    @staticmethod
    def translate(morse):
        """
        Translates a Morse message into English
        """
        morse_code = MorseCode()
        morse = morse.split(' ')
        english = []
        for code in morse:
            if code in morse_code.code_list:
                x = morse_code.code_list.index(code)
                english.append(morse_code.alpha_list[x])
            # Attach punctuation or spaces as needed
            if code == '':
                english.append(' ')
            if code in morse_code.punc_codes:
                index = morse_code.punc_codes.index(code)
                english.append(morse_code.punc_eng[index])
        return ''.join(english)
