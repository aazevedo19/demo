

class Estado:

    def __init__(self, sigla, nome):
        self.sigla = sigla
        self.nome = nome
        self.descricao = nome + '(' + sigla + ')'
