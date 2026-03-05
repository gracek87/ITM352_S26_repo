# Build an interactive quiz application that supports asking a user at least five multiple-choice questions.  The quiz should present each question to the user, present at least four options for the answer (a-d), accept an answer from the user. Let them know if their answer is correct or not.  At the end of the quiz, it should report the final score.  The program should not allow a user to enter an invalid response. If the responses are a-d, any other response, such as "q", should be ignored and the user should be re-prompted).  The quiz questions should be kept in a file so that it is easy to add/remove questions or to have sets of questions on different topics.  
# 1. Write the history of scores out to a file. 
# 3. Allow for multiple numbers of answers to a question. 

import random
from string import ascii_lowercase

# Each question stores (correct answers list, all possible options)
QUESTIONS = {
    "Which sport is Duke Kahanamoku most famous for?": (["Surfing"], ["Surfing", "Basketball", "Baseball", "Football"]),
    "Simone Biles is famous for competing in which sport?": (["Gymnastics"], ["Gymnastics", "Swimming", "Tennis", "Track and Field"]),
    "Michael Jordan is best known for playing which sport?": (["Basketball"], ["Basketball", "Baseball", "Football", "Golf"]),
    "Serena Williams is one of the greatest athletes in which sport?": (["Tennis"], ["Tennis", "Soccer", "Volleyball", "Track"]),
    "Which of the following athletes are Olympic gold medalists?": (
        ["Simone Biles", "Usain Bolt", "Serena Williams"],
        ["Simone Biles", "Usain Bolt", "Serena Williams", "Kaori Sakamoto"]
    )
}

# File used to store user high scores
SCORE_FILE = "scores.txt"


# Randomizes answer order and labels them by letter (a, b, c, d)
def makeLabeledAlternatives(options):
    shuffledOptions = options.copy()
    random.shuffle(shuffledOptions)
    labels = ascii_lowercase[:len(shuffledOptions)]
    labeledAlternatives = dict(zip(labels, shuffledOptions))
    return labeledAlternatives


# Ensures the user enters a valid answer choice
def getValidChoice(labeledAlternatives, multiAnswer):
    while True:
        if multiAnswer:
            # Allow multiple letters for questions with multiple answers
            answerLabels = input("Choice(s)? ").lower().replace(" ", "")
            if all(label in labeledAlternatives for label in answerLabels):
                return answerLabels
        else:
            answerLabel = input("Choice? ").lower()
            if answerLabel in labeledAlternatives:
                return answerLabel
        print("Invalid choice. Please enter valid letter(s).")


# Displays a question and checks if the user's answer 
def askQuestion(questionNum, question, correctAnswers, options):
    print(f"\nQuestion {questionNum}:")
    print(question)

    labeledAlternatives = makeLabeledAlternatives(options)
    for label in ascii_lowercase[:len(labeledAlternatives)]:
        print(f" {label}. {labeledAlternatives[label]}")
    multiAnswer = len(correctAnswers) > 1
    if multiAnswer:
        print("Select ALL correct answers.")

    answerLabels = getValidChoice(labeledAlternatives, multiAnswer)

    # Handle questions with multiple correct answers
    if multiAnswer:
        answers = [labeledAlternatives[label] for label in answerLabels]
        if set(answers) == set(correctAnswers):
            print("Correct!")
            return 1
        else:
            print(f"Correct answers were: {', '.join(correctAnswers)}")
            return 0

    # Handle normal single-answer questions
    else:
        answer = labeledAlternatives[answerLabels]
        if answer in correctAnswers:
            print("Correct!")
            return 1
        else:
            print(f"The answer is '{correctAnswers[0]}' not '{answer}'")
            return 0


# Runs the quiz and keeps track of total correct answers
def runQuiz(questions):
    numCorrect = 0
    questionList = list(questions.items())
    random.shuffle(questionList)

    for questionNum, (question, data) in enumerate(questionList, start=1):
        correctAnswers, options = data
        numCorrect += askQuestion(questionNum, question, correctAnswers, options)

    return numCorrect


# Loads previous user scores from the file
def loadScores():
    scores = {}
    try:
        with open(SCORE_FILE, "r") as file:
            for line in file:
                name, score = line.strip().split(",")
                scores[name] = int(score)
    except FileNotFoundError:
        pass
    return scores


# Saves updated scores back to the file
def saveScores(scores):
    with open(SCORE_FILE, "w") as file:
        for name, score in scores.items():
            file.write(f"{name},{score}\n")


# Prompts the user to login with a username
def login():
    username = input("Enter your username: ")
    return username


# Updates the user's personal high score if they beat it
def updateHighScore(username, score, scores):
    if username not in scores or score > scores[username]:
        scores[username] = score
        print("New personal high score!")


# Finds and displays the grand champion (highest score overall)
def showChampion(scores):
    if scores:
        champion = max(scores, key=scores.get)
        print(f"\nGrand Champion: {champion} with {scores[champion]} points!")


# Main function that runs the entire program
def main():
    scores = loadScores()
    username = login()
    numCorrect = runQuiz(QUESTIONS)
    print(f"\n{username}, you got {numCorrect} out of {len(QUESTIONS)} correct.")
    updateHighScore(username, numCorrect, scores)
    saveScores(scores)
    showChampion(scores)

main()