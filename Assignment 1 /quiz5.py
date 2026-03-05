# Quiz game.  Fifth version.
# Name: Grace Kulhanek
# Date: 02/24/2026
# Make a list with the questions and correct answers.
# Make QUESTIONS a dictionary, to include answer options and the correct choice.
# Allow the user to select the correct answer by a label.
# Improve look and usability. Keep track of correct answers.

# Quiz game.  Fifth version.
# Name: Grace Kulhanek
# Date: 02/24/2026
# Make a list with the questions and correct answers.
# Make QUESTIONS a dictionary, to include answer options and the correct choice.
# Allow the user to select the correct answer by a label.
# Improve look and usability. Keep track of correct answers.

import random
from string import ascii_lowercase

QUESTIONS = {
    "What is the airspeed of an unladen swallow in miles/hr?": ["12", "10", "15", "8"],
    "What is the capital of Texas?": ["Austin", "Houston", "Dallas", "San Antonio"],
    "The Last Supper was painted by which artist?": ["Da Vinci", "Michelangelo", "Raphael", "Donatello"]
}

numCorrect = 0

questionList = list(QUESTIONS.items())
random.shuffle(questionList)

for num, (question, options) in enumerate(questionList, start=1):
    print(f"Question {num}:")
    print(question)

    correctAnswer = options[0]  # The first option is the correct answer

    shuffledOptions = options.copy()
    random.shuffle(shuffledOptions)

    labels = ascii_lowercase[:len(shuffledOptions)]
    labeledAlternatives = dict(zip(labels, shuffledOptions))

    for label in labels:
        print(f" {label}. {labeledAlternatives[label]}")

    answerLabel = input("Choice? ").lower()
    answer = labeledAlternatives.get(answerLabel)

    if answer == correctAnswer:
        print("Correct!")
        numCorrect += 1
    else:
        print(f"The answer is '{correctAnswer}' not {answer!r}")

print(f"You got {numCorrect} out of {len(QUESTIONS)} correct.")