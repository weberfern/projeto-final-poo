class Tentativa:
    def __init__ (self, quiz_referencia, usuario_referencia, respostas_dadas, pontuacao_obtida, taxa_acerto, tempo_total):
        self.quiz_referencia = quiz_referencia
        self.usuario_referencia = usuario_referencia
        self.respostas_dadas = respostas_dadas
        self.pontuacao_obtida = pontuacao_obtida
        self.taxa_acerto = taxa_acerto
        self.tempo_total = tempo_total

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
    
    def registrar_resposta(self):
        pass
    
    def finalizar_tentativa(self):
        pass

    def gerar_gabarito(self):
        pass