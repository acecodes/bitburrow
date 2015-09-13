from flask import Flask, request
from flask_restful import Resource, Api
from acemorse import MorseCode

app = Flask(__name__)
api = Api(app)

app.config.from_object('config')


class Encode(Resource):

    def post(self):
        response = request.get_json()
        encoded = MorseCode.generate(response.get('message', None))
        if encoded:
            return {'message': encoded}
        return {'error': 'This did not work.'}


class Decode(Resource):

    def post(self):
        response = request.get_json()
        decoded = MorseCode.translate(response.get('message', None))
        if decoded:
            return {'message': decoded}
        return {'error': 'This did not work.'}

api.add_resource(Encode, '/encode')
api.add_resource(Decode, '/decode')

if __name__ == '__main__':
    app.run(debug=True)
