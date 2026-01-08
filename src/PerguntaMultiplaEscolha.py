# Implementação da classe PerguntaMultiplaEscolha

from src.Pergunta import Pergunta

class PerguntaMultiplaEscolha(Pergunta):
    
    def __init__(self, cod_pergunta, enunciado, dificuldade, tema, alternativas, resposta_indice):
        
        super().__init__(cod_pergunta, enunciado, dificuldade, tema)
        
        self.alternativas = alternativas
        self.resposta_indice = resposta_indice
        
    def verificar_resposta(self, resposta_usuario):
        if resposta_usuario == self.resposta_indice:
            return True
        else:
            return False
        
    def exibir_pergunta(self):
        super().exibir_pergunta()
        for i, alternativa in enumerate(self.alternativas):
            print(f"{i}. {alternativa}")