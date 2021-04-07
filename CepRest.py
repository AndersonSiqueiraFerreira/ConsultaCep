import requests

from Localizacao import Endereco


def find(cep):
    url = 'https://viacep.com.br/ws/{cep}/json/'.format(cep=cep)
    return requests.get(url).json()


def to_string(data):
    if 'erro' not in data:
        endereco = Endereco(data['cep'], data['logradouro'],
                            data['bairro'], data['localidade'],
                            data['uf'])
        print(endereco)