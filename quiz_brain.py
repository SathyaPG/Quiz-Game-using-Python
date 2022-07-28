class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_question(self):
        if self.question_number == len(self.question_list):
            return False
        return True

    def next_question(self):
         current_question = self.question_list[self.question_number]
         self.question_number += 1
         user_Answer = input(f"Q.{self.question_number} : {current_question.text} (True/False) : ")
         self.check_answer(user_Answer, current_question.answer)

    def check_answer(self, user_a, correct_a):
        if user_a.lower() == correct_a.lower():
            print("You have got it right")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer is {correct_a}")
        print(f"your score is {self.score}/{self.question_number}\n")