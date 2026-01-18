class Tentativa:
    def __init__ (self, quiz_referencia: int, usuario_referencia: int, respostas_dadas: dict, pontuacao_obtida: int, tempo_total: int):
        self.quiz_referencia = quiz_referencia
        self.usuario_referencia = usuario_referencia
        self.respostas_dadas = respostas_dadas
        self.pontuacao_obtida = pontuacao_obtida
        self.tempo_total = tempo_total
        #CALCULA A TAXA DE ACERTO AO INICIAR A TENTATIVA
        self.taxa_acerto = self.calcular_taxa_acerto()

    #####################################################
    ### GETTERS E SETTERS DE CADA ATRIBUTO DA CLASSE ####
    #####################################################
    
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

    #####################################################
    ###              MÉTODOS DA CLASSE               ####
    #####################################################

    def registrar_tentativa(self):
        #SIMULA O REGISTRO DA TENTATIVA (POR ENQUANTO, APENAS IMPRIME UMA MENSAGEM)
        print(f" > Tentativa salva para o usuário {self.usuario_referencia.nome} no quiz {self.quiz_referencia.titulo}.")

    def calcular_pontuacao(self):
        return self.pontuacao_obtida

    def calcular_taxa_acerto(self):
        if self.quiz_referencia.pontos_max == 0:
            return 0
        return (self.pontuacao_obtida / self.quiz_referencia.pontos_max) * 100

    def calcular_tempo_total(self):
        return self.tempo_total

    def mostrar_tentativa(self):
        print(f"--- Detalhes da Tentativa ---")
        print(f"Quiz: {self.quiz_referencia.titulo}")
        print(f"Usuário: {self.usuario_referencia.nome}")
        print(f"Pontuação Obtida: {self.pontuacao_obtida}/{self.quiz_referencia.pontos_max}")
        print(f"Taxa de Acerto: {self.taxa_acerto}%")
        print(f"Tempo Total: {self.tempo_total} minutos")

    def atualizar_tentativa(self):
        print(" > Tentativa atualizada.")
        
    def deletar_tentativa(self):
        print(" > Tentativa deletada.")