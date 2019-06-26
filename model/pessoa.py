class Pessoa:
    def __init__(self):
        self._id = ""
        self._cpf = ""
        self._nome = ""
        self._endereco = ""
        self._complemento = ""
        self._cidade = ""
        self._bairro = ""
        self._estado = ""
        self._cep = ""
        self._dtainc = ""

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if len(value) < 0:
            raise ValueError("ID inválido!")
        self._id = value

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, value):
        if len(value) < 14:
            raise ValueError("CPF inválido!")
        self._cpf = value

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        if len(value) > 30:
            raise ValueError("Nome inválido!")
        self._nome = value

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, value):
        if len(value) > 50:
            raise ValueError("Endereço inválido!")
        self._endereco = value

    @property
    def complemento(self):
        return self._complemento

    @complemento.setter
    def complemento(self, value):
        if len(value) > 50:
            raise ValueError("Complemento inválido!")
        self._complemento = value

    @property
    def cidade(self):
        return self._cidade

    @cidade.setter
    def cidade(self, value):
        if len(value) > 50:
            raise ValueError("Cidade inválido!")
        self._cidade = value

    @property
    def bairro(self):
        return self._bairro

    @bairro.setter
    def bairro(self, value):
        if len(value) > 50:
            raise ValueError("Bairro inválido!")
        self._bairro = value

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, value):
        if len(value) > 50:
            raise ValueError("Estado inválido!")
        self._estado = value

    @property
    def cep(self):
        return self._cep

    @cep.setter
    def cep(self, value):
        if len(value) > 10:
            raise ValueError("CEP inválido!")
        self._cep = value

    @property
    def dtainc(self):
        return self._dtainc

    @dtainc.setter
    def dtainc(self, value):
        if len(value) > 20:
            raise ValueError("Data inválida!")
        self._dtainc = value
