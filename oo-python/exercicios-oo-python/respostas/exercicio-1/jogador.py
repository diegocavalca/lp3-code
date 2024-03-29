import datetime

class JogadorFutebol:
    def __init__(self, nome, posicao, nascimento, nacionalidade, altura, peso):
        self.__nome = nome
        self.__posicao = posicao
        self.__nascimento = nascimento
        self.__nacionalidade = nacionalidade
        self.__altura = altura
        self.__peso = peso

    def calcular_idade(self):
        hoje = datetime.datetime.now()
        idade = hoje.year - self.__nascimento.year - ((hoje.month, hoje.day) < (self.__nascimento.month, self.__nascimento.day))
        return idade

    def falta_para_aposentar(self):
        anos_para_aposentar = 0
        if (self.__posicao == "defesa"):
            anos_para_aposentar = 40 - self.calcular_idade()
        elif(self.__posicao == "meio-campo"):
            anos_para_aposentar = 38 - self.calcular_idade()
        elif(self.__posicao == "atacante"):
            anos_para_aposentar = 35 - self.calcular_idade()
        return anos_para_aposentar

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def posicao(self):
        return self.__posicao

    @posicao.setter
    def posicao(self, posicao):
        self.__posicao = posicao

    @property
    def nascimento(self):
        return self.__nascimento

    @nascimento.setter
    def nascimento(self, nascimento):
        self.__nascimento = nascimento

    @property
    def nacionalidade(self):
        return self.__nacionalidade

    @nacionalidade.setter
    def nacionalidade(self, nacionalidade):
        self.__nacionalidade = nacionalidade

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura):
        self.__altura = altura

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, peso):
        self.__peso = peso

    def __str__(self):
        return "Nome: %s, Posição: %s, Nascimento: %s, Nacionalidade: %s, Altura: %f, Peso: %d" % \
               (self.__nome, self.__posicao, self.__nascimento, self.__nacionalidade, self.__altura, self.__peso)