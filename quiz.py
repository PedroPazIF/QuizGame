import json
class Question:
    def __init__(self, pergunta, opcoes, resposta, tema):
        self.pergunta = pergunta
        self.opcoes = opcoes
        self.resposta = resposta
        self.tema = tema

    def __repr__(self):
        return f"<Question> pergunta: {self.pergunta} - opcoes: {self.opcoes} - tema: {self.tema}"

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
    
    def start(self):
      for question in self.questions:
        print("\n" + question.pergunta + " Tema: " + question.tema)
        for i, option in enumerate(question.opcoes, start=1):
                print(f"{i}. {option}")
        respostaCerta = question.resposta[0]

        while True:
            try:
                user_answer = input("Escolha a sua resposta: ")
                if not 1 <= user_answer <= 3:
                    raise ValueError('Valor fora do intervalo permitido')
                break
            except ValueError as error:
                print(error)    
        # if user_answer == len(question.opcoes):
        #         if user_answer == self.resposta:
        #             print("Resposta correta!")
        #         else:
        #             print(f"Resposta incorreta. A resposta correta é: {question.resposta}")

if __name__ == "__main__":
    with open('jogos.json', 'r') as f:
        data = json.load(f)

    questions = [Question(q['pergunta'], q['opcoes'], q['resposta'], q['tema']) for q in data['jogos']]
    quiz = Quiz(questions)
    quiz.start()