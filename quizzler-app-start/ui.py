from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
from tkinter import *


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.source_label = Label(text="Score: 0 ", fg="white", bg=THEME_COLOR, highlightthickness=0,
                                  font=("Arial", 20, "italic"))
        self.source_label.grid(row=0, column=1)
        self.q_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some question", font=("Arial", 20, "italic"))
        right_image = PhotoImage(file="images/true.png")
        wrong_image = PhotoImage(file="images/false.png")
        self.r_button = Button(image=right_image, highlightthickness=0, command=self.true_pressed)
        self.r_button.grid(row=2, column=1)
        self.w_button = Button(image=wrong_image, highlightthickness=0, command=self.false_pressed)
        self.w_button.grid(row=2, column=0)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.source_label.config(text=f"Score: {self.quiz.score}")
            # q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.q_text, text="You have reached the end of the quiz.")
            self.r_button.config(state="disabled")
            self.w_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
        self.source_label.config(text=f"Score: {self.quiz.score}")

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, ans: bool):
        if ans:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
