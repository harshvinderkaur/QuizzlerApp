from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="#fff")
        self.score_label.grid(row=1, column=2)

        self.canvas = Canvas(width=300, height=250, bg="#fff")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="hellow world",
            font=("Arial", 20, "italic"),
            width=280,
            fill=THEME_COLOR)
        self.canvas.grid(row=2, column=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.true_btn = Button(image=true_img, relief=FLAT, command=self.true_answer)
        self.true_btn.grid(row=3, column=1)
        self.false_btn = Button(image=false_img, relief=FLAT, command=self.false_answer)
        self.false_btn.grid(row=3, column=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_answer(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def false_answer(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)



