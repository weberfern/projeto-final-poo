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
    
    @quiz_referencia.setter
    def quiz_referencia(self, quiz_referencia):
        self.__quiz_referencia = quiz_referencia

    @property
    def usuario_referencia(self):
        return self.__usuario_referencia
    
    @usuario_referencia.setter
    def usuario_referencia(self, usuario_referencia):
        self.__usuario_referencia = usuario_referencia

    @property
    def respostas_dadas(self):
        return self.__respostas_dadas
    
    @respostas_dadas.setter
    def respostas_dadas(self, respostas_dadas):
        self.__respostas_dadas = respostas_dadas

    @property
    def pontuacao_obtida(self):
        return self.__pontuacao_obtida
    
    @pontuacao_obtida.setter
    def pontuacao_obtida(self, pontuacao_obtida):
        self.__pontuacao_obtida = pontuacao_obtida

    @property
    def taxa_acerto(self):
        return self.__taxa_acerto
    
    @taxa_acerto.setter
    def taxa_acerto(self, taxa_acerto):
        self.__taxa_acerto = taxa_acerto

    @property
    def tempo_total(self):
        return self.__tempo_total
    
    @tempo_total.setter
    def tempo_total(self, tempo_total):
        self.__tempo_total = tempo_total

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