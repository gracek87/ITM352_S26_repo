from flask import Flask, redirect, render_template, request, session, url_for
import random
import time

app = Flask(__name__)
app.secret_key = "quizSecretKey"

timeLimitSeconds = 15

allQuestions = [
    {
        "category": "Sports",
        "question": "Which sport is Duke Kahanamoku most famous for?",
        "correctAnswers": ["Surfing"],
        "options": ["Surfing", "Basketball", "Baseball", "Football"]
    },
    {
        "category": "Sports",
        "question": "Simone Biles is famous for competing in which sport?",
        "correctAnswers": ["Gymnastics"],
        "options": ["Gymnastics", "Swimming", "Tennis", "Track and Field"]
    },
    {
        "category": "Sports",
        "question": "Michael Jordan is best known for playing which sport?",
        "correctAnswers": ["Basketball"],
        "options": ["Basketball", "Baseball", "Football", "Golf"]
    },
    {
        "category": "Sports",
        "question": "Serena Williams is one of the greatest athletes in which sport?",
        "correctAnswers": ["Tennis"],
        "options": ["Tennis", "Soccer", "Volleyball", "Track"]
    },
    {
        "category": "Sports",
        "question": "Which of the following athletes are Olympic gold medalists?",
        "correctAnswers": ["Simone Biles", "Usain Bolt", "Serena Williams"],
        "options": ["Simone Biles", "Usain Bolt", "Serena Williams", "Kaori Sakamoto"]
    },

    {
        "category": "Food",
        "question": "Which country is most closely associated with the dish paella?",
        "correctAnswers": ["Spain"],
        "options": ["Spain", "Italy", "Mexico", "Greece"]
    },
    {
        "category": "Food",
        "question": "What type of pastry is traditionally used to make baklava?",
        "correctAnswers": ["Phyllo"],
        "options": ["Phyllo", "Puff pastry", "Shortcrust", "Sourdough"]
    },
    {
        "category": "Food",
        "question": "Which cheese is traditionally used in a Greek salad?",
        "correctAnswers": ["Feta"],
        "options": ["Feta", "Mozzarella", "Brie", "Cheddar"]
    },
    {
        "category": "Food",
        "question": "What is the main ingredient in miso soup that gives it its signature flavor?",
        "correctAnswers": ["Fermented soybean paste"],
        "options": ["Fermented soybean paste", "Fish sauce", "Coconut milk", "Sesame oil"]
    },
    {
        "category": "Food",
        "question": "Which of the following are classic French mother sauces?",
        "correctAnswers": ["Béchamel", "Velouté", "Hollandaise"],
        "options": ["Béchamel", "Velouté", "Hollandaise", "Pesto"]
    },

    {
        "category": "Movies",
        "question": "Which film won the Academy Award for Best Picture in 1994, beating Pulp Fiction and The Shawshank Redemption?",
        "correctAnswers": ["Forrest Gump"],
        "options": ["Forrest Gump", "Pulp Fiction", "The Shawshank Redemption", "Four Weddings and a Funeral"]
    },
    {
        "category": "Movies",
        "question": "Who directed the 2010 film Inception?",
        "correctAnswers": ["Christopher Nolan"],
        "options": ["Christopher Nolan", "Steven Spielberg", "James Cameron", "Denis Villeneuve"]
    },
    {
        "category": "Movies",
        "question": "In The Godfather, what is the Corleone family’s main organized crime business at the beginning of the film?",
        "correctAnswers": ["Olive oil importing"],
        "options": ["Olive oil importing", "Casino ownership", "Movie production", "Construction"]
    },
    {
        "category": "Movies",
        "question": "Which actress played the lead role of Evelyn Wang in Everything Everywhere All at Once?",
        "correctAnswers": ["Michelle Yeoh"],
        "options": ["Michelle Yeoh", "Cate Blanchett", "Sandra Oh", "Lucy Liu"]
    },
    {
        "category": "Movies",
        "question": "Which of the following films were directed by Quentin Tarantino?",
        "correctAnswers": ["Pulp Fiction", "Kill Bill", "Inglourious Basterds"],
        "options": ["Pulp Fiction", "Kill Bill", "Inglourious Basterds", "Goodfellas"]
    }
]


def getQuestionsByCategory(category):
    questionList = []

    for question in allQuestions:
        if question["category"] == category:
            newQuestion = question.copy()
            shuffledOptions = question["options"].copy()
            random.shuffle(shuffledOptions)
            newQuestion["shuffledOptions"] = shuffledOptions
            questionList.append(newQuestion)

    random.shuffle(questionList)
    return questionList


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        username = request.form.get("username", "").strip()

        # VALIDATION
        if username == "":
            return render_template(
                "index.html",
                error="Please enter your name.",
                username=session.get("username"),
                history=session.get("history", [])
            )

        # SAVE USER
        session["username"] = username

        # CREATE HISTORY
        if "history" not in session:
            session["history"] = []

        return redirect(url_for("setup"))

    return render_template(
        "index.html",
        username=session.get("username"),
        history=session.get("history", [])
    )


@app.route("/setup", methods=["GET", "POST"])
def setup():
    categories = ["Sports", "Food", "Movies"]

    # REQUIRE USER
    if "username" not in session:
        return redirect(url_for("home"))

    if request.method == "POST":
        category = request.form.get("category", "").strip()

        # VALIDATION
        if category not in categories:
            return render_template(
                "setup.html",
                categories=categories,
                error="Please choose a valid category."
            )

        questionList = getQuestionsByCategory(category)

        # VALIDATION
        if len(questionList) == 0:
            return render_template(
                "setup.html",
                categories=categories,
                error="No questions were found for that category."
            )

        # START QUIZ
        session["category"] = category
        session["questions"] = questionList
        session["questionIndex"] = 0
        session["score"] = 0
        session["questionStartTime"] = time.time()

        return redirect(url_for("quiz"))

    return render_template(
        "setup.html",
        categories=categories
    )


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    # REQUIRE USER
    if "username" not in session:
        return redirect(url_for("home"))

    # REQUIRE QUIZ SESSION
    if "questions" not in session:
        return redirect(url_for("setup"))

    if "questionIndex" not in session:
        return redirect(url_for("setup"))

    questions = session.get("questions", [])
    questionIndex = session.get("questionIndex", 0)

    # END QUIZ
    if questionIndex >= len(questions):
        return redirect(url_for("result"))

    currentQuestion = questions[questionIndex]
    multiAnswer = len(currentQuestion["correctAnswers"]) > 1

    if request.method == "POST":
        selectedAnswers = request.form.getlist("answer")
        startTime = session.get("questionStartTime", time.time())
        timeUsed = time.time() - startTime

        # TIMER CHECK
        if timeUsed > timeLimitSeconds:
            session["questionIndex"] = questionIndex + 1
            session["questionStartTime"] = time.time()
            return redirect(url_for("quiz"))

        # VALIDATION (no invalid input allowed)
        if len(selectedAnswers) == 0:
            return render_template(
                "quiz.html",
                question=currentQuestion,
                questionNumber=questionIndex + 1,
                totalQuestions=len(questions),
                category=session.get("category", ""),
                multiAnswer=multiAnswer,
                timeLimit=timeLimitSeconds,
                error="Please select at least one answer."
            )

        # SCORE CHECK
        if set(selectedAnswers) == set(currentQuestion["correctAnswers"]):
            session["score"] = session.get("score", 0) + 1

        # NEXT QUESTION
        session["questionIndex"] = questionIndex + 1
        session["questionStartTime"] = time.time()

        return redirect(url_for("quiz"))

    # RESET TIMER FOR FIRST LOAD OF CURRENT QUESTION
    if "questionStartTime" not in session:
        session["questionStartTime"] = time.time()

    return render_template(
        "quiz.html",
        question=currentQuestion,
        questionNumber=questionIndex + 1,
        totalQuestions=len(questions),
        category=session.get("category", ""),
        multiAnswer=multiAnswer,
        timeLimit=timeLimitSeconds
    )


@app.route("/result")
def result():
    # REQUIRE USER
    if "username" not in session:
        return redirect(url_for("home"))

    # REQUIRE COMPLETED QUIZ
    if "questions" not in session:
        return redirect(url_for("setup"))

    username = session.get("username", "")
    category = session.get("category", "")
    score = session.get("score", 0)
    totalQuestions = len(session.get("questions", []))

    # SAVE HISTORY
    history = session.get("history", [])
    history.append(f"{category}: {score}/{totalQuestions}")
    session["history"] = history

    # CLEAR QUIZ DATA
    session.pop("questions", None)
    session.pop("questionIndex", None)
    session.pop("score", None)
    session.pop("questionStartTime", None)
    session.pop("category", None)

    return render_template(
        "result.html",
        username=username,
        score=score,
        totalQuestions=totalQuestions,
        history=history
    )


def main():
    app.run(debug=True, host="0.0.0.0", port=5002)


if __name__ == "__main__":
    main()