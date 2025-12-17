# Projeto Quiz Educacional

## INTEGRANTES:
- JEFFERSON RODRIGUES DE OLIVEIRA -- Responsável pelas classes **Pergunta** e **PerguntaMultiplaEscolha**
- MARCELO DOS SANTOS ALVES -- Responsável pela classe **Quiz**
- WEBER FERNANDES DA SILVA -- Responsável pelas classes **Usuario** e **Tentativa**

## PRINCIPAIS CLASSES
**Class: Pergunta**
- Atributos: cod_pergunta, enunciado, dificuldade, tema
- Métodos: salvar, atualizar, deletar, mostrar, verificar_resposta, mostrar_resposta, obter_dificuldade

**Class: PerguntaMultiplaEscolha(Pergunta)**
- Atributos: enunciado, alternativas, resposta_indice, dificuldade, tema
- Métodos: verificar_resposta

**Class: Quiz**
- Atributos: titulo, perguntas, pontos_max, num_tentativas, tempo_limite
- Métodos: adicionar_pergunta, remover_pergunta, salvar, atualizar, deletar, mostrar, calcular_pontuacao, iniciar_execucao

**Class: Usuario**
- Atributos: nome, email, id, historico_tentativas
- Métodos: salvar, mostrar, atualizar, deletar, tentar_quiz

**Class: Tentativa**
- Atributos: quiz_referencia, usuario_referencia, respostas_dadas, pontuacao_obtida, taxa_acerto, tempo_total
- Métodos: salvar, mostrar, atualizar, deletar, registrar_resposta, finalizar_tentativa, gerar_gabarito

