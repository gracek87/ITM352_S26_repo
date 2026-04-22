from flask import Flask, redirect, render_template, request, session, url_for
import random
from string import ascii_lowercase

app = Flask(__name__)
app.secret_key = "quizSecretKey"

# YOUR ORIGINAL QUESTIONS (UNCHANGED)
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

scoreFile = "scores.txt"


# Convert dict → shuffled list for Flask use
def getQuestionList():
    questionList = []
    for question, data in QUESTIONS.items():
        correctAnswers, options = data
        shuffledOptions = options.copy()
        random.shuffle(shuffledOptions)

        questionList.append({
            "question": question,
            "correctAnswers": correctAnswers,
            "options": shuffledOptions
        })

    random.shuffle(questionList)
    return questionList


def loadScores():
    scores = {}
    try:
        with open(scoreFile, "r") as file:
            for line in file:
                name, score = line.strip().split(",")
                scores[name] = int(score)
    except FileNotFoundError:
        pass
    return scores


def saveScores(scores):
    with open(scoreFile, "w") as file:
        for name, score in scores.items():
            file.write(f"{name},{score}\n")


def updateHighScore(username, score, scores):
    if username not in scores or score > scores[username]:
        scores[username] = score
        return True
    return False


def getChampion(scores):
    if scores:
        champion = max(scores, key=scores.get)
        return champion, scores[champion]
    return None, None


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        username = request.form.get("username", "").strip()

        if username == "":
            return render_template("index.html", error="Enter a username.")

        session["username"] = username
        session["questions"] = getQuestionList()
        session["questionNumber"] = 0
        session["score"] = 0

        return redirect(url_for("quiz"))

    return render_template("index.html")


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if "questions" not in session:
        return redirect(url_for("home"))

    questions = session["questions"]
    questionNumber = session["questionNumber"]

    if questionNumber >= len(questions):
        return redirect(url_for("result"))

    currentQuestion = questions[questionNumber]
    options = currentQuestion["options"]

    labeledOptions = dict(zip(ascii_lowercase[:len(options)], options))
    multiAnswer = len(currentQuestion["correctAnswers"]) > 1

    if request.method == "POST":
        selectedAnswers = request.form.getlist("answer")

        # VALIDATION (no invalid input allowed)
        if len(selectedAnswers) == 0:
            return render_template(
                "quiz.html",
                question=currentQuestion["question"],
                labeledOptions=labeledOptions,
                questionNumber=questionNumber + 1,
                totalQuestions=len(questions),
                multiAnswer=multiAnswer,
                error="Select at least one answer."
            )

        if not all(ans in labeledOptions for ans in selectedAnswers):
            return render_template(
                "quiz.html",
                question=currentQuestion["question"],
                labeledOptions=labeledOptions,
                questionNumber=questionNumber + 1,
                totalQuestions=len(questions),
                multiAnswer=multiAnswer,
                error="Invalid choice."
            )

        chosenOptions = [labeledOptions[a] for a in selectedAnswers]
        correctAnswers = currentQuestion["correctAnswers"]

        if set(chosenOptions) == set(correctAnswers):
            session["score"] += 1

        session["questionNumber"] += 1
        return redirect(url_for("quiz"))

    return render_template(
        "quiz.html",
        question=currentQuestion["question"],
        labeledOptions=labeledOptions,
        questionNumber=questionNumber + 1,
        totalQuestions=len(questions),
        multiAnswer=multiAnswer
    )


@app.route("/result")
def result():
    if "username" not in session:
        return redirect(url_for("home"))

    username = session["username"]
    score = session["score"]
    totalQuestions = len(session["questions"])

    scores = loadScores()
    newHighScore = updateHighScore(username, score, scores)
    saveScores(scores)

    champion, championScore = getChampion(scores)

    session.clear()

    return render_template(
        "result.html",
        username=username,
        score=score,
        totalQuestions=totalQuestions,
        newHighScore=newHighScore,
        champion=champion,
        championScore=championScore
    )


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()