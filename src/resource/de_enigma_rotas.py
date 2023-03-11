from flask_restful import Resource
from flask import request
from criptografia.funcoes import *

class DeEnigma(Resource):

    def post(self):
        try:
            corpo = request.get_json(force = True)
        except:
            return {'mensagem': 'Problema ao parsear o JSON'}, 400
        
        P = cria_matriz(corpo['chave'])
        E = cria_matriz(corpo['chave'] + 17)

        msg_criptografada = de_enigma(corpo['msg'], P, E )
        return {'mensagem': msg_criptografada}, 200