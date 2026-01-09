# Implementação da classe PerguntaMultiplaEscolha

from src.Pergunta import Pergunta

class PerguntaMultiplaEscolha(Pergunta):
    """
    Representa uma pergunta de múltipla escolha.
    Possui alternativas e um índice que indica a resposta correta.
    
    """
    def __init__(self, cod_pergunta, enunciado, dificuldade, tema, alternativas, resposta_indice):
        
        super().__init__(cod_pergunta, enunciado, dificuldade, tema)
        
        self.alternativas = alternativas
        self.resposta_indice = resposta_indice
        
    def verificar_resposta(self, resposta_usuario):
        """
        Verifica se a resposta do usuário está correta
        
        """
        return resposta_usuario == self.resposta_indice

    
    