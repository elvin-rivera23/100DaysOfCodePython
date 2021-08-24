# Elvin Rivera
# 8/20/2021
#
# Reference: https://opentdb.com , https://www.w3schools.com/html/html_entities.asp ,
# https://www.freeformatter.com/html-escape.html ,
# https://stackoverflow.com/questions/2087370/decode-html-entities-in-python-string


from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# mainloop from ui.py will get confused if you have a while loop
# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
