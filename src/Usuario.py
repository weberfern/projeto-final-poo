class Usuario:
    def __init__ (self, cod_usuario: int, nome: str, email: str, historico_tentativas: list):
        self.cod_usuario = cod_usuario
        self.nome = nome
        self.email = email
        self.historico_tentativas = historico_tentativas

    #####################################################
    ### GETTERS E SETTERS DE CADA ATRIBUTO DA CLASSE ####
    #####################################################

    @property
    def cod_usuario (self):
        return self.__cod_usuario
    
    @cod_usuario.setter
    def cod_usuario(self, value):
        self.__cod_usuario = value

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
    def historico_tentativas (self):
        return self.__historico_tentativas
    
    @historico_tentativas.setter
    def historico_tentativas(self, value):
        self.__historico_tentativas = value
  
    #####################################################
    ###              MÉTODOS DA CLASSE               ####
    #####################################################

    def tentar_quiz (self, quiz):
        quiz.iniciar_quiz()

    def visualizar_historico (self):
        pass