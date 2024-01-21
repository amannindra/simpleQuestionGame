from answer import quiz_data
import random


class Question_format():
    def __init__(self, question_text, answer_text, A_text, B_text, C_text, D_text):
        self.question_text = question_text
        self.answer_text = answer_text
        self.A_text = A_text
        self.B_text = B_text
        self.C_text = C_text
        self.D_text = D_text


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.question_number = 0

    def load_next_question(self):
        if self.question_number < len(self.questions):
            current_question = self.questions[self.question_number]
            prepared_question = "Q{0}: {1}\nA: {2}\nB: {3}\nC: {4}\nD: {5}".format(
                self.question_number + 1,
                current_question.question_text,
                current_question.A_text,
                current_question.B_text,
                current_question.C_text,
                current_question.D_text
            )
        user_answer = self.ask_question(prepared_question)
        self.check_for_correctness(
            user_answer, current_question.question_text, current_question.answer_text)
        self.question_number += 1

    def ask_question(self, question):
        return input(f"{question}\nYour answer: ")

    def check_for_correctness(self, user_answer, current_question, answer_text):
        if user_answer.strip().upper() == answer_text.strip().upper():
            self.score += 1
            print("Correct Answer")
        else:
            print("Incorrect Answer")


def extractQuestion():
    questions = []
    for question in quiz_data:
        question_text = question["question"]
        answer_text = question["correct_answer"]
        A_text = question["A"]
        B_text = question["B"]
        C_text = question["C"]
        D_text = question["D"]
        answer_text = question["correct_answer"]
        prepared_question = Question_format(
            question_text, answer_text, A_text, B_text, C_text, D_text)
        questions.append(prepared_question)
    quiz = Quiz(questions)
    while True:
        quiz.question_number = random.randint(0, len(questions)-1)
        quiz.load_next_question()


extractQuestion()
