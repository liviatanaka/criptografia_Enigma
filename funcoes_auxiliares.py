"""Funções auxiliares para a biblioteca de criptografia enigma."""
import re
from unidecode import unidecode

def limpa_mensagem(msg):
    # Transforma a string para minúsculo
    msg = msg.lower()
    # Remove acentos
    msg = unidecode(msg)
    # Substitui caracteres especiais por "_"
    msg = re.sub(r'[^a-z0-9\s]', '_', msg)
    # Remove os números
    msg = re.sub(r'[0-9]', '_', msg)
    return msg