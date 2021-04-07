from zeep import Client
from zeep.transports import Transport
from requests import Session
from requests.auth import HTTPBasicAuth

from Localizacao import Endereco

'''
Com WSDL,usuário e senha de teste dos Correios para consultar o CEP informado
'''


def find(cep):
    wsdl = 'https://apphom.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl'
    session = Session()
    session.auth = HTTPBasicAuth('sigep', 'n5f9t8')
    client = Client(wsdl, transport=Transport(session=session))
    return client.service.consultaCEP(cep)


def to_string(data):
    if 'cep' in data:
        endereco = Endereco(data['cep'], data['end'],
                            data['bairro'], data['cidade'],
                            data['uf'])
        print(endereco)