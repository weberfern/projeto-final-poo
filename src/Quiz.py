class Quiz:
    
    def __init__(self, titulo: str, perguntas: list, pontos_max: int, num_tentativas: int, tempo_limite: int):
        self.titulo = titulo 
        self.perguntas = perguntas
        self.pontos_max = pontos_max
        self.num_tentativas = num_tentativas
        self.tempo_limite = tempo_limite

    ########################## GETTERS E SETTERS DE CADA ATRIBUTO DA CLASSE ##########################
    

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
    def pontos_max(self):
        return self.__pontos_max

    @pontos_max.setter
    def pontos_max(self, value):
        self.__pontos_max = value
    
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

    ################################# MÉTODOS DA CLASSE ##################################
    

    def iniciar_quiz(self):
        print(f"--- Iniciando Quiz: {self.titulo} ---")
        pontuacao_atual = 0


        for pergunta in self.perguntas:
            print("\n--------------------------------")

            pergunta.exibir_pergunta()

            try:
                resposta_usuario = input("Digite o número da sua resposta: ")
                indice_ajustado = int(resposta_usuario) - 1 #Removendo o 0 do índice de numeração ficando 1, 2, 3, 4


                if pergunta.verificar_resposta(int(indice_ajustado)):
                    print("Resposta registrada com sucesso!")
                    pontuacao_atual += 1
                else:
                    print("Resposta registrada com sucesso!")
                
            except ValueError:
                print("Entrada inválida. Por favor, insira um número correspondente à sua resposta.")


        print("=================================")
        print(f"Quiz finalizado!")
        print(f"Sua pontuação final: {pontuacao_atual} de {len(self.perguntas)}")
        print("=================================")

        return pontuacao_atual

    def exibir_perguntas(self):
        pass 

    def calcular_pontuacao_max(self):
        pass 

    def verificar_tentativas(self):
        pass 

    def verificar_tempo_limite(self):
        pass