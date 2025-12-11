# Projeto Quiz Educacional

## INTEGRANTES:
- JEFFERSON OLIVEIRA -- RESPONSÁVEL PELAS CLASSES
- MARCELO -- RESPONSÁVEL PELA INTERFACE
- WEBER FERNANDES DA SILVA --

## PRINCIPAIS CLASSES
Classe: Pergunta
Atributos: enunciado, alternativas, resposta, dificuldade, tema
Métodos: salvar, atualizar, deletar, mostrar, verificar_resposta, mostrar_resposta

Classe: Quiz
- Atributos: titulo, perguntas, pontos_max, num_tentativas, tempo_limite
- Métodos: salvar, atualizar, deletar, mostrar, calcular_pontuacao

Classe: Usuario
- Atributos: nome, email, id, tentativas
- Métodos: salvar, mostrar, atualizar, deletar, tentar_quiz

Classe: Tentativa
- Atributos: quiz, respostas
- Métodos: salvar, mostrar, atualizar, deletar

Classe: Estatisticas
- Atributos: acertos, erros
- Métodos: 
