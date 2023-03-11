from flask import Flask
from flask_restful import Api
from resource.enigma_rotas import Enigma
from resource.de_enigma_rotas import DeEnigma

app = Flask(__name__)
api = Api(app)

@app.route("/")
def hello_world():
    return f"<p>Hello, World!</p>"


api.add_resource(Enigma, '/enigma')
api.add_resource(DeEnigma,'/de-enigma')


if __name__ == '__main__':
    app.run(debug=True)