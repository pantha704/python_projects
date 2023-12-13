from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for i in question_data:
    q_text = i["text"]
    q_ans = i["answer"]
    new_ques = Question(q_text,q_ans)
    question_bank.append(new_ques)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print()
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.q_no}")