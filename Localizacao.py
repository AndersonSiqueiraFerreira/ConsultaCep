class Endereco:

    def __init__(self, cep, rua, bairro, cidade, uf):
        self.cep = cep
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf

    def __str__(self):
        return f'Rua: {self.rua} Bairro: {self.bairro} CEP: {self.cep} Cidade: {self.cidade} UF: {self.uf}'
