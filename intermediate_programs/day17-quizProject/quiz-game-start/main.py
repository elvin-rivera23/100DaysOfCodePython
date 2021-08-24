from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []  # start by creating an empty list
for question in question_data:
    # loop through dictionary and get text and answer (data.py)
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)  # construct a new object for each one
    question_bank.append(new_question)  # append to empty list question_bank

quiz = QuizBrain(question_bank)  # construct new quiz and pass in q_list parameter (question_bank)

while quiz.still_has_questions():
    quiz.next_question()  # calls the method from QuizBrain

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")  # quiz is an object, can tap into its attributes
