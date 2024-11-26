class QuizBrain:
    def __init__(self, question_list):
        self.question_num = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_num < len(self.question_list)


    def next_question(self):
        q_list = self.question_list
        curr_q = q_list[self.question_num]
        print(curr_q.answer)
        users_answer = input(f'Q.{self.question_num + 1} {curr_q.text}. True or False? ')
        self.question_num += 1
        self.check_ans(users_answer, curr_q.answer)


    def check_ans(self, users_answer, corr_ans):
        if users_answer.lower() == corr_ans.lower():
            self.score += 1
            print('You are right!')
        else:
            print('You are wrong!')
        print(f'The correct answer was {corr_ans}')
        print(f"Your current score is: {self.score}/{self.question_num}")
        print('\n')

