# Projeto Quiz Educacional

## INTEGRANTES:
- JEFFERSON OLIVEIRA -- RESPONSÁVEL PELAS CLASSES | Pergunta | E | PerguntaMultiplaEscolha |
- MARCELO -- RESPONSÁVEL PELAS CLASSES Quiz
- WEBER FERNANDES DA SILVA -- RESPONSÁVEL PELAS CLASSES | Usuario | E | Tentativa |

## PRINCIPAIS CLASSES
Class: Pergunta
- Atributos: enunciado, dificuldade, tema
- Métodos: salvar, atualizar, deletar, mostrar, verificar_resposta, mostrar_resposta, obter_dificuldade

Class: PerguntaMultiplaEscolha(Pergunta)
- Atributos: enunciado, alternativas, resposta_indice, dificuldade, tema
- Métodos: verificar_resposta

Class: Quiz
- Atributos: titulo, perguntas (Lista de Pergunta()), pontos_max, num_tentativas, tempo_limite
- Métodos: adicionar_pergunta, remover_pergunta, salvar, atualizar, deletar, mostrar, calcular_pontuacao, iniciar_execucao

Class: Usuario
- Atributos: nome, email, id, historico_tentativas (Lista de Tentativa())
- Métodos: salvar, mostrar, atualizar, deletar, tentar_quiz

Class: Tentativa
- Atributos: quiz_referencia (Quiz()), usuario_referencia (Usuario()), respostas_dadas, pontuacao_obtida, taxa_acerto, tempo_total
- Métodos: salvar, mostrar, atualizar, deletar, registrar_resposta, finalizar_tentativa, gerar_gabarito

