class Tentativa:
    def __init__ (self, quiz_referencia, usuario_referencia, respostas_dadas, pontuacao_obtida, taxa_acerto, tempo_total):
        self.quiz_referencia = quiz_referencia
        self.usuario_referencia = usuario_referencia
        self.respostas_dadas = {}

    #####################################################
    ### GETTERS E SETTERS DE CADA ATRIBUTO DA CLASSE ####
    #####################################################
    
    @property
    def quiz_referencia(self):
        return self.__quiz_referencia

    def salvar(self):
        pass
    
    def mostrar(self):
        pass
    
    def atualizar(self):
        pass
    
    def deletar(self):
        pass
    