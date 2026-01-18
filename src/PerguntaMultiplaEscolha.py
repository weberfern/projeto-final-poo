from .Pergunta import Pergunta

class PerguntaMultiplaEscolha(Pergunta):
    def __init__(self, cod_pergunta, enunciado, dificuldade, tema, alternativas, resposta_indice):
        # Aproveita a parte básica da classe Pergunta
        super().__init__(cod_pergunta, enunciado, dificuldade, tema)

        # Quando atribuímos aqui, as regras dos setters abaixo já são aplicadas
        self.alternativas = alternativas 
        self.resposta_indice = resposta_indice

    # Lista de alternativas da pergunta
    @property
    def alternativas(self):
        return self._alternativas

    @alternativas.setter
    def alternativas(self, lista):
        # A pergunta precisa ter entre 3 e 5 opções
        if not (3 <= len(lista) <= 5):
            raise ValueError("A pergunta deve ter entre 3 e 5 alternativas.")
        self._alternativas = lista

    # Índice da alternativa correta
    @property
    def resposta_indice(self):
        return self._resposta_indice

    @resposta_indice.setter
    def resposta_indice(self, valor):
        # O índice precisa estar dentro da quantidade de alternativas
        if not (0 <= valor < len(self.alternativas)):
            raise ValueError("Índice da resposta correta inválido.")
        self._resposta_indice = valor

    def verificar_resposta(self, resposta_usuario):
        # Confere se a resposta do usuário é igual ao índice correto
        return int(resposta_usuario) == self.resposta_indice

    def mostrar_resposta(self):
        # Mostra qual é a alternativa certa
        correta = self.alternativas[self.resposta_indice]
        print(f"Gabarito: Alternativa {self.resposta_indice + 1} {correta}")

    def exibir_pergunta(self):
        # Mostra o enunciado e todas as alternativas numeradas
        super().exibir_pergunta()
        for i, texto in enumerate(self.alternativas):
            print(f"  {i + 1}. {texto}")
    