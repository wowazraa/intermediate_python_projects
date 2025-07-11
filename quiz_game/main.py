from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import html

question_bank = []

for q in question_data["results"]:
    question_bank.append(Question(html.unescape(q["question"]), q["correct_answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
