from data import question_bank
from quiz_brain import QuizBrain

brain = QuizBrain(question_bank)
while brain.still_has_questions():
    brain.next_question()

print('You have completed the quiz')
print(f'Your final score is {brain.score}/{brain.question_num}')