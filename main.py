from src.Usuario import Usuario

user1 = Usuario(1, "Ana", "ana@ufca.edu.br", [])

iniciar_quiz = input("Deseja iniciar um quiz? (s/n): ")

if iniciar_quiz.lower() == 's':
    print("Número do quiz: - Título: - ")
    print("1 - Quem descobriu o Brasil?")
    print("2 - Qual a capital da França?")
    print("3 - Qual é a fórmula da água?")
    print("4 - Quem escreveu 'Dom Casmurro'?")
    escolha_quiz = input("Escolha o número do quiz que deseja iniciar: ")
else:
    print("Quiz não iniciado.")
    escolha_quiz = None

if escolha_quiz is not None:
    user1.tentar_quiz(escolha_quiz)