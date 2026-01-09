# Classe Pergunta
# Representa uma pergunta genérica do sistema de quiz
# Serve como classe base para outros tipos de pergunta

class Pergunta:
    """
    Classe base que define os atributos e comportamentos comuns
    a todas as perguntas do quiz.
    """

    def __init__(self, cod_pergunta, enunciado, dificuldade, tema):
        self.cod_pergunta = cod_pergunta
        self.enunciado = enunciado
        self.dificuldade = dificuldade
        self.tema = tema

    @property
    def dificuldade(self):
        return self._dificuldade

    @dificuldade.setter
    def dificuldade(self, valor):
        if valor not in ["Fácil", "Médio", "Difícil"]:
            raise ValueError("Dificuldade inválida.")
        self._dificuldade = valor

    def exibir_pergunta(self):
        print(
            f"[{self.cod_pergunta}] {self.enunciado} "
            f"({self.dificuldade} • {self.tema})"
        )

    def obter_dificuldade(self):
        return self.dificuldade

    def salvar(self):
        print(f"Pergunta {self.cod_pergunta} salva.")

    def atualizar(self, novo_enunciado=None, novo_tema=None, nova_dificuldade=None):
        if novo_enunciado:
            self.enunciado = novo_enunciado
        if novo_tema:
            self.tema = novo_tema
        if nova_dificuldade:
            self.dificuldade = nova_dificuldade
        print(f"Pergunta {self.cod_pergunta} atualizada.")

    def deletar(self):
        print(f"Pergunta {self.cod_pergunta} deletada.")

    def verificar_resposta(self, resposta_usuario):
        """
        Deve ser implementado pelas subclasses para verificar
        se a resposta do usuário está correta
        """
        raise NotImplementedError()

    def mostrar_resposta(self):
        """
        Deve ser implementado pelas subclasses para exibir
        a resposta correta da pergunta
        """
        raise NotImplementedError()
