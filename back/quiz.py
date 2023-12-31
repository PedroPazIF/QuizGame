import json
import random

class Question:
    def __init__(self, question, options, correct_answer, theme):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
        self.theme = theme

#factory 
class factoryQuestion:
    def createQuestion(data):
        question = [Question(q['pergunta'], q['opcoes'], int(q['resposta']), q['tema']) for q in data['jogos']]
        return question
    
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.current_question_index = 0
        self.score = 0
        self.observers = []

#observer
    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.score)

    def start(self):
        while self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            print(f"\n--------------------------------------------------------------------")
            print(f" Pergunta: {question.question} \n Tema: {question.theme}")
            print(f"--------------------------------------------------------------------\n")

            for i, option in enumerate(question.options):
                print(f"{i + 1}. {option}")
                
            user_answer = int(input("\nEscolha sua resposta: "))
            if user_answer == question.correct_answer:
                self.score += 1
            self.current_question_index += 1
            self.notify_observers()

class ScoreObserver:
    def __init__(self):
        self.score = 0

    def update(self, score):
        self.score = score
        print(f"\n--------------")
        print(f"|PONTUAÇÃO: {self.score}|")
        print(f"--------------\n")

class QuizFacade:
    def __init__(self, total=0):
        self.quiz = None
        self.score_observer = None
        self.total = total

    def load_questions_from_json(self, file_path, total):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            questions = factoryQuestion.createQuestion(data)
            print(questions)
            total_int = int(total)
            selecao = random.sample(questions, min(total_int, len(questions)))
            self.quiz = Quiz(selecao)
            self.score_observer = ScoreObserver()
            self.quiz.add_observer(self.score_observer)
            return selecao 
            
    def start_quiz(self):
        if self.quiz:
            self.quiz.start()
        else:
            print("Por favor, carregue as perguntas antes de iniciar o quiz.")

if __name__ == "__main__":
    facade = QuizFacade()
    facade.load_questions_from_json('jogos.json')
    facade.start_quiz()
