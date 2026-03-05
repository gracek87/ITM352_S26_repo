# Quiz game. Sixth version.
# Name: Grace Kulhanek
# Date: 02/24/2026
# Make a list with the questions and correct answers.
# Make QUESTIONS a dictionary, to include answer options and the correct choice.
# Allow the user to select the correct answer by a label.
# Improve look and usability. Keep track of correct answers.
# Randomize question order and answer choices.


import random
import string

questions = {
    "What is the airspeed of an unladen swallow in miles/hr?": ["12", "10", "15", "8"],
    "What is the capital of Texas?": ["Austin", "Houston", "Dallas", "San Antonio"],
    "The Last Supper was painted by which artist?": ["Da Vinci", "Michelangelo", "Raphael", "Donatello"]
}

numCorrect = 0

# Shuffle question order
questionList = list(questions.items())
random.shuffle(questionList)

for num, (question, options) in enumerate(questionList, start=1):
    print(f"\nQuestion {num}:")
    print(question)

    correctAnswer = options[0]  

    # Shuffle answer order
    shuffledOptions = options.copy()
    random.shuffle(shuffledOptions)

    labels = string.ascii_lowercase[:len(shuffledOptions)]
    labeledAlternatives = dict(zip(labels, shuffledOptions))

    for label in labels:
        print(f" {label}. {labeledAlternatives[label]}")

    # Input validation
    while True:
        answerLabel = input("Choice? ").lower()
        if answerLabel in labeledAlternatives:
            break
        print("Invalid choice. Please enter a valid letter.")

    answer = labeledAlternatives[answerLabel]

    if answer == correctAnswer:
        print("Correct!")
        numCorrect += 1
    else:
        print(f"The answer is '{correctAnswer}' not '{answer}'.")

print(f"\nYou got {numCorrect} out of {len(questions)} correct.")