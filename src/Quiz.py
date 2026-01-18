class Quiz:
    def __init__(self, titulo: str, perguntas: list, num_tentativas: int, tempo_limite: int):
        self.titulo = titulo 
        self.perguntas = perguntas
        self.num_tentativas = num_tentativas
        self.tempo_limite = tempo_limite

    ########################## GETTERS E SETTERS ##########################
    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, value):
        self.__titulo = value
    
    @property
    def perguntas(self):
        return self.__perguntas

    @perguntas.setter
    def perguntas(self, value):
        self.__perguntas = value
    
    @property
    def num_tentativas(self):
        return self.__num_tentativas

    @num_tentativas.setter
    def num_tentativas(self, value):
        self.__num_tentativas = value
    
    @property
    def tempo_limite(self):
        return self.__tempo_limite

    @tempo_limite.setter
    def tempo_limite(self, value):
        self.__tempo_limite = value

    ################################# MÉTODOS PRINCIPAIS ##################################
    def iniciar_quiz(self):
        print(f"--- Iniciando Quiz: {self.titulo} ---")
        pontuacao_total_obtida = 0
        
        # Dicionário de pesos conforme regra de negócio
        pesos = {"Fácil": 1, "Médio": 2, "Difícil": 3}

        for pergunta in self:  # Usa o __iter__ implementado
            pergunta.exibir_pergunta()
            try:
                resposta = int(input("Digite o número da sua resposta: ")) - 1
                if pergunta.verificar_resposta(resposta):
                    print("Você acertou!")
                    pontuacao_total_obtida += pesos.get(pergunta.dificuldade, 1)
                else:
                    print("Você errou!")
            except ValueError:
                print("Entrada inválida.")

        print("=================================")
        print(f"Quiz finalizado!")
        print(f"Sua pontuação final: {pontuacao_total_obtida} de {self.pontos_max}")
        print("=================================")

        return pontuacao_total_obtida

    def exibir_perguntas(self):
        print(f"--- Perguntas do Quiz: {self.titulo} ---")
        for pergunta in self.perguntas:
            pergunta.exibir_pergunta()

    @property
    def pontos_max(self):
        # Calcula automaticamente a pontuação máxima com base nas dificuldades
        pesos = {"Fácil": 1, "Médio": 2, "Difícil": 3}
        return sum(pesos.get(p.dificuldade, 1) for p in self.perguntas)

    def verificar_tentativas(self):
        if self.num_tentativas <= 0:
            print("Número de tentativas esgotado.")
            return False
        return True

    def verificar_tempo_limite(self):
        if self.tempo_limite <= 0:
            print("Tempo limite expirado.")
            return False
        return True

    ################################# MÉTODOS ESPECIAIS ##################################
    def __len__(self):
        return len(self.perguntas)

    def __iter__(self):
        return iter(self.perguntas)

    def __str__(self):
        return f"Quiz: {self.titulo} | Perguntas: {len(self)} | Pontos Máx: {self.pontos_max}"