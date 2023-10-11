import json
class Question:
    def __init__(self, pergunta, opcoes, resposta):
        self.pergunta = pergunta
        self.opcoes = opcoes
        self.resposta = resposta

    def __repr__(self):
        return f"<Question> pergunta: {self.pergunta} - opcoes: {self.opcoes}"

class Quiz:
    def __init__(self, questions):
        self.questions = questions
    
    def start(self):
      for question in self.questions:
        print("\n" + question.pergunta)
        for i, option in enumerate(question.opcoes, start=1):
                print(f"{i}. {option}")

if __name__ == "__main__":
    with open('jogos.json', 'r') as f:
        data = json.load(f)

    questions = [Question(q['pergunta'], q['opcoes']) for q in data['jogos']]
    quiz = Quiz(questions)
    quiz.start()