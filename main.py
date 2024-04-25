from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from art import true
print(true)

question_bank = []
for question in question_data:
	question_text = question["question"]
	question_answer = question["correct_answer"]
	new_question = Question(question_text, question_answer)
	question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
	quiz.next_question()

print("You have completed the quiz successfully!")
if quiz.your_score >= quiz.out_of / 2:
	print(f"Congratulations!! you passed your final score is {quiz.your_score}/{quiz.out_of}")
else:
	print(f"Ooh!! you  lose your final score is {quiz.your_score}/{quiz.out_of}")


