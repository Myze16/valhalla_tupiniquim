class Heroi:
    def __init__(self, nome, classe, forca, destreza, constituicao, inteligencia, carisma):
        self._nome = nome
        self._classe = classe
        self._forca = forca
        self._destreza = destreza
        self._constituicao = constituicao
        self._inteligencia = inteligencia
        self._carisma = carisma
        self._vida = 100

    # nome
    @property
    def nome(self):
        return self._name

    @nome.setter
    def nome(self, value):
        self._name = value
    
    # classe
    @property
    def classe(self):
        return self._classe

    @classe.setter
    def classe(self, value):
        self._classe = value

    #forca
    @property
    def forca(self):
        return self._forca

    @forca.setter
    def forca(self, value):
        if self.verifyValueAttr(value):
            self._forca = value
        else:
            return 'São válidos somente valores entre 1 e 18'

    # destreza
    @property
    def destreza(self):
        return self._destreza

    @destreza.setter
    def destreza(self, value):
        if self.verifyValueAttr(value):
            self._destreza = value
        else:
            return 'São válidos somente valores entre 1 e 18'

    # constituicao
    @property
    def constituicao(self):
        return self._constituicao

    @constituicao.setter
    def constituicao(self, value):
        if self.verifyValueAttr(value):
            self._constituicao = value
        else:
            return 'São válidos somente valores entre 1 e 18'

    # inteligencia
    @property
    def inteligencia(self):
        return self._inteligencia

    @inteligencia.setter
    def inteligencia(self, value):
        if self.verifyValueAttr(value):
            self._inteligencia = value
        else:
            return 'São válidos somente valores entre 1 e 18'

    # carisma
    @property
    def carisma(self):
        return self._carisma

    @carisma.setter
    def carisma(self, value):
        if self.verifyValueAttr(value):
            self._carisma = value
        else:
            return 'São válidos somente valores entre 1 e 18'

    # vida
    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, value):
        self._vida = value
    
    def verifyValueAttr(self, value):
        return True if value < 1 or value > 18 else False

    def __str__(self):
        return [self.nome, self.classe, self.forca, self.destreza, self.contituicao, self.inteligencia, self.carisma, self.vida]
