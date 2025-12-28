from Tentativa import Tentativa

class Usuario:
    def __init__ (self, nome, email, id, historico_tentativas):
        self.nome = nome
        self.email = email
        self.id = id
        self.historico_tentativas = historico_tentativas

    @property
    def nome (self):
        return self.__nome
    
    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def email (self):
        return self.__email
    
    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def cod_usuario (self):
        return self.__cod_usuario
    
    @cod_usuario.setter
    def cod_usuario(self, value):
        self.__cod_usuario = value

    @property
    def historico_tentativas (self):
        return self.__historico_tentativas
    
    @historico_tentativas.setter
    def historico_tentativas(self, value):
        self.__historico_tentativas = value

    def mostrar (self):
        pass
    
    def atualizar (self):
        pass
    
    def deletar (self):
        pass
    
    def tentar_quiz (self):
        pass