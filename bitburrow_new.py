from flask import Flask, request
from flask_restful import Resource, Api
from acemorse import MorseCode
import time


app = Flask(__name__)
api = Api(app)

title = 'BitBurrow'
desc = 'A web app for encoding and decoding messages using various code systems'
author = 'Ace Eddleman'
year = time.strftime("%Y")


app.config.from_object('config')


class Encode(Resource):
    def post(self):
        response = request.get_json()
        morse = MorseCode()
        encoded = morse.generate(response.get('message', None))
        if encoded:
            return {'message': encoded}
        return {'error': 'This did not work.'}

class Decode(Resource):
    def post(self):
        response = request.get_json()
        morse = MorseCode()
        decoded = morse.translate(response.get('message', None))
        if decoded:
            return {'message': decoded}
        return {'error': 'This did not work.'}

api.add_resource(Encode, '/encode')


if __name__ == '__main__':
    app.run(debug=True)
