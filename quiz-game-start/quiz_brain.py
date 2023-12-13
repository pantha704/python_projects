from data import question_data

class QuizBrain:
    def __init__(self, q_list):
        self.q_no = 0
        self.score = 0
        self.ques_list = q_list

    def still_has_questions(self):
        return self.q_no < len(self.ques_list)

    def check_answer(self, userans, correctans):
        if userans == correctans:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
            print(f"Nice try! your score is: {self.score}/{self.q_no}")
        print(f"The correct answer is: {correctans}")
        print()
        print(f"Your current score is: {self.score}/{self.q_no}")
        if self.q_no == len(self.ques_list):
            pass
        else:
            self.next_question()

    def next_question(self):
        current_ques = self.ques_list[self.q_no]
        self.q_no += 1

        userans = input(f"Q.{self.q_no}: {current_ques.text} (True/False) ")
        self.check_answer(userans, current_ques.answer)

