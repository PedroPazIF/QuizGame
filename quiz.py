import json

#factory
class Question:
    def __init__(self, question, options, correct_answer, theme):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
        self.theme = theme
    
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.current_question_index = 0
        self.score = 0
        self.observers = []

#strategy
#observer

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.score)

    def start(self):
        while self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            print(f"Pergunta: {question.question}")
            for i, option in enumerate(question.options):
                print(f"{i + 1}. {option}")
            user_answer = int(input("Escolha sua resposta: "))
            if user_answer == question.correct_answer:
                self.score += 1
            self.current_question_index += 1
            self.notify_observers()

    # def calculate_score(self, user_answers):
    #     self.score = sum([1 for i in range(len(user_answers)) if user_answers[i] == self.questions[i].resposta])
    #     print(f"Sua pontuação final: {self.score}/{len(self.questions)}")

class ScoreObserver:
    def __init__(self):
        self.score = 0

    def update(self, score):
        self.score = score
        print(f"\n--------------")
        print(f"|PONTUAÇÃO: {self.score}|")
        print(f"--------------\n")

if __name__ == "__main__":
    with open('jogos.json', 'r') as f:
        data = json.load(f)

    questions = [Question(q['pergunta'], q['opcoes'], int(q['resposta']), q['tema']) for q in data['jogos']]
    quiz = Quiz(questions)
    score_observer = ScoreObserver()
    quiz.add_observer(score_observer)
    quiz.start()
