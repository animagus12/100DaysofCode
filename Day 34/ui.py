from tkinter import *

from matplotlib.pyplot import text
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('Arial', 20, 'italic')


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.root = Tk()
        self.root.title('Quizzler')
        self.root.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_lbl = Label(self.root, text="Score: 0", fg='white', bg=THEME_COLOR, font=('Arial', 15, 'bold'))
        self.score_lbl.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.ques_text = self.canvas.create_text(150, 125, text="Filler", fill=THEME_COLOR, font=FONT, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Loading Button Images
        true_img = PhotoImage(file='Python/#100DaysOfCode/Day 34/images/true.png')
        false_img = PhotoImage(file='Python/#100DaysOfCode/Day 34/images/false.png')

        # Buttons
        self.true_btn = Button(image=true_img, bg=THEME_COLOR, highlightthickness=0, bd=0, command=self.correct)
        self.true_btn.grid(column=0, row=2)
        self.false_btn = Button(image=false_img, bg=THEME_COLOR, highlightthickness=0, bd=0, command=self.wrong)
        self.false_btn.grid(column=1, row=2)

        self.get_next_question()

        self.root.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_lbl.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.ques_text, text=q_text)
        else:
            self.canvas.itemconfig(self.ques_text, text="Thank You for completing the quiz.")
            self.true_btn.config(state='disabled')
            self.false_btn.config(state='disabled')

    def correct(self):
        self.feedback(self.quiz.check_answer('True'))

    def wrong(self):
        self.feedback(self.quiz.check_answer('False'))

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.root.after(1000, self.get_next_question)
