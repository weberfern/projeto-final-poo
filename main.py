from src import Usuario, Quiz, PerguntaMultiplaEscolha

# Criação de perguntas para inserir no Quiz
p1 = PerguntaMultiplaEscolha(1, "Quem descobriu o Brasil?", "Fácil", "História",
                             ["Pedro Álvares Cabral", "Cristóvão Colombo", "Vasco da Gama", "Fernão de Magalhães"], 0)
p2 = PerguntaMultiplaEscolha(2, "Qual a capital da França?", "Fácil", "Geografia",
                             ["Berlim", "Madrid", "Paris", "Lisboa"], 2)
p3 = PerguntaMultiplaEscolha(3, "Qual é a fórmula da água?", "Fácil", "Ciência",
                             ["CO2", "H2O", "O2", "NaCl"], 1)
p4 = PerguntaMultiplaEscolha(4, "Quem escreveu 'Dom Casmurro'?", "Médio", "Literatura",
                             ["Machado de Assis", "José de Alencar", "Clarice Lispector", "Graciliano Ramos"], 0)

lista_perguntas = [p1, p2, p3, p4]  # p1, p2, p3, p4 são instâncias de PerguntaMultiplaEscolha

# Criação de um quiz
quiz1 = Quiz("Quiz de Conhecimentos Gerais", lista_perguntas, 4, 3, 60)

# Criação de um usuário
user1 = Usuario(1, "Ana", "ana@ufca.edu.br", [])

# Iniciar o quiz
iniciar_quiz = input("Deseja iniciar um quiz? (s/n): ")

if iniciar_quiz.lower() == 's':
    user1.tentar_quiz(quiz1)
    escolha_quiz = quiz1
else:
    print("Quiz não iniciado.")
    escolha_quiz = None