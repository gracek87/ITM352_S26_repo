# Quiz game.  Seventh version.
# Name: Grace Kulhanek
# Date: 02/24/2026
# Make a list with the questions and correct answers.
# Make QUESTIONS a dictionary, to include answer options and the correct choice.
# Allow the user to select the correct answer by a label.
# Improve look and usability. Keep track of correct answers.
# Randomize question order and answer choices.
# Refactor the code to use functions. Randomize question order and answer order.

import random
from string import ascii_lowercase

QUESTIONS = {
    "What is the airspeed of an unladen swallow in miles/hr?": ["12", "10", "15", "8"],
    "What is the capital of Texas?": ["Austin", "Houston", "Dallas", "San Antonio"],
    "The Last Supper was painted by which artist?": ["Da Vinci", "Michelangelo", "Raphael", "Donatello"]
}

def makeLabeledAlternatives(options):
    correctAnswer = options[0]
    shuffledOptions = options.copy()
    random.shuffle(shuffledOptions)
    labels = ascii_lowercase[:len(shuffledOptions)]
    labeledAlternatives = dict(zip(labels, shuffledOptions))
    return labeledAlternatives, correctAnswer

def getValidChoice(labeledAlternatives):
    while True:
        answerLabel = input("Choice? ").lower()
        if answerLabel in labeledAlternatives:
            return answerLabel
        print("Invalid choice. Please enter a valid letter.")

def askQuestion(questionNum, question, options):
    print(f"\nQuestion {questionNum}:")
    print(question)

    labeledAlternatives, correctAnswer = makeLabeledAlternatives(options)

    for label in ascii_lowercase[:len(labeledAlternatives)]:
        print(f" {label}. {labeledAlternatives[label]}")

    answerLabel = getValidChoice(labeledAlternatives)
    answer = labeledAlternatives[answerLabel]

    if answer == correctAnswer:
        print("Correct!")
        return 1
    else:
        print(f"The answer is '{correctAnswer}' not {answer!r}")
        return 0

def runQuiz(questions):
    numCorrect = 0
    questionList = list(questions.items())
    random.shuffle(questionList)

    for questionNum, (question, options) in enumerate(questionList, start=1):
        numCorrect += askQuestion(questionNum, question, options)

    return numCorrect

def main():
    numCorrect = runQuiz(QUESTIONS)
    print(f"\nYou got {numCorrect} out of {len(QUESTIONS)} correct.")

main()