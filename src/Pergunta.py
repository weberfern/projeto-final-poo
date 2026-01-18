class Pergunta:
    """
    Classe base que representa uma pergunta genérica do sistema de quiz.
    Ela serve como modelo para outros tipos de perguntas (ex.: múltipla escolha).
    Não deve ser usada diretamente, apenas herdada.
    """

    def __init__(self, cod_pergunta, enunciado, dificuldade, tema):
        # Valida se o enunciado não está vazio
        if not enunciado.strip():
            raise ValueError("O enunciado da pergunta não pode ser vazio.")

        self.cod_pergunta = cod_pergunta
        self.enunciado = enunciado
        self.dificuldade = dificuldade  # será validada pelo setter
        self.tema = tema

    # ------------------- ENCAPSULAMENTO -------------------
    @property
    def dificuldade(self):
        return self._dificuldade

    @dificuldade.setter
    def dificuldade(self, valor):
        # Valida se a dificuldade está dentro das opções permitidas
        if valor not in ["Fácil", "Médio", "Difícil"]:
            raise ValueError("Dificuldade inválida. Use: Fácil, Médio ou Difícil.")
        self._dificuldade = valor

    # ------------------- MÉTODOS ESPECIAIS -------------------
    def __str__(self):
        """
        Retorna uma representação textual amigável da pergunta.
        Exemplo: [1] Qual a capital da França? (Fácil • Geografia)
        """
        return f"[{self.cod_pergunta}] {self.enunciado} ({self.dificuldade} • {self.tema})"

    def __eq__(self, other):
        """
        Compara duas perguntas pelo enunciado e tema.
        Isso evita duplicidade de perguntas iguais dentro do mesmo tema.
        """
        return isinstance(other, Pergunta) and self.enunciado == other.enunciado and self.tema == other.tema

    # ------------------- MÉTODOS A SEREM SOBRESCRITOS -------------------
    def verificar_resposta(self, resposta_usuario):
        """
        Deve ser implementado pelas subclasses.
        Aqui apenas levantamos um erro para lembrar que não deve ser usado diretamente.
        """
        raise NotImplementedError("Este método deve ser implementado pela subclasse.")

    def mostrar_resposta(self):
        """
        Deve ser implementado pelas subclasses.
        Aqui apenas levantamos um erro para lembrar que não deve ser usado diretamente.
        """
        raise NotImplementedError("Este método deve ser implementado pela subclasse.")

    # ------------------- MÉTODOS DE APOIO -------------------
    def exibir_pergunta(self):
        """
        Exibe a pergunta no formato padrão.
        """
        print(self.__str__())

    def obter_dificuldade(self):
        """
        Retorna a dificuldade da pergunta.
        """
        return self.dificuldade

    # ------------------- MÉTODOS DE PERSISTÊNCIA (simulados) -------------------
    def salvar(self):
        print(f"Pergunta {self.cod_pergunta} salva.")

    def atualizar(self, novo_enunciado=None, novo_tema=None, nova_dificuldade=None):
        """
        Atualiza os atributos da pergunta, caso novos valores sejam fornecidos.
        """
        if novo_enunciado:
            self.enunciado = novo_enunciado
        if novo_tema:
            self.tema = novo_tema
        if nova_dificuldade:
            self.dificuldade = nova_dificuldade
        print(f"Pergunta {self.cod_pergunta} atualizada.")

    def deletar(self):
        print(f"Pergunta {self.cod_pergunta} deletada.")