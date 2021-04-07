import CepRest
import CepSoap

if __name__ == '__main__':
    print('### Web Service dos Correios ###')
    d1 = CepSoap.find('13420835')
    CepSoap.to_string(d1)

    print('### Web Service ViaCep ###')
    d2 = CepRest.find('19470000')
    CepRest.to_string(d2)

