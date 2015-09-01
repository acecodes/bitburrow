from flask import Flask, request, render_template
from flask_wtf import Form
from flask_mail import Mail, Message
from flask_restful import Resource, Api
from wtforms import TextField
from wtforms.validators import Required, Email
from acemorse import MorseCode
import re
import time


app = Flask(__name__)
api = Api(app)

title = "BitBurrow"
desc = 'A web app for encoding and decoding messages using various code systems'
author = 'Ace Eddleman'
year = time.strftime("%Y")


app.config.from_object('config')


class Encode(Resource):
    def post(self):
        response = request.get_json()
        morse = MorseCode()
        encoded = morse.generate(response.get('message', None))
        print(encoded)
        if encoded:
            return {'message': encoded}
        return {'error': 'This did not work.'}

api.add_resource(Encode, '/encode')


if __name__ == '__main__':
    app.run(debug=True)
