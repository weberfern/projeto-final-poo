class Tentativa:
    def __init__ (self, quiz_referencia: int, usuario_referencia: int, respostas_dadas: int, pontuacao_obtida: int, taxa_acerto: int, tempo_total: int):
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
    def quiz_referencia(self, value):
        self.__quiz_referencia = value

    @property
    def usuario_referencia(self):
        return self.__usuario_referencia

    @usuario_referencia.setter
    def usuario_referencia(self, value):
        self.__usuario_referencia = value

    @property
    def respostas_dadas(self):
        return self.__respostas_dadas
    
    @respostas_dadas.setter
    def respostas_dadas(self, value):
        self.__respostas_dadas = value

    @property
    def pontuacao_obtida(self):
        return self.__pontuacao_obtida

    @pontuacao_obtida.setter
    def pontuacao_obtida(self, value):
        self.__pontuacao_obtida = value

    @property
    def taxa_acerto(self):
        return self.__taxa_acerto

    @taxa_acerto.setter
    def taxa_acerto(self, value):
        self.__taxa_acerto = value

    @property
    def tempo_total(self):
        return self.__tempo_total

    @tempo_total.setter
    def tempo_total(self, value):
        self.__tempo_total = value
    
    def registrar_resposta(self):
        pass
    
    def finalizar_tentativa(self):
        pass

    def gerar_gabarito(self):
        pass