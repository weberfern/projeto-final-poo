class Usuario:
    def __init__ (self, nome, email, id, historico_tentativas):
        self.nome = nome
        self.email = email
        self.id = id
        self.historico_tentativas = historico_tentativas

    #####################################################
    ### GETTERS E SETTERS DE CADA ATRIBUTO DA CLASSE ####
    #####################################################
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def historico_tentativas(self):
        return self.__historico_tentativas
    
    @historico_tentativas.setter
    def historico_tentativas(self, historico_tentativas):
        self.__historico_tentativas = historico_tentativas

    ######################################################
    ###            MÉTODOS DA CLASSE USUARIO           ###
    ######################################################

    def tentar_quiz (self):
        pass

    def salvar (self):
        pass

    def mostrar (self):
        pass
    
    def atualizar (self):
        pass
    
    def deletar (self):
        pass
    