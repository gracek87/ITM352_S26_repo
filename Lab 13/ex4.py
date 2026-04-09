# Create a skeleton Flask application for a quiz game

from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "graceSecretKey"


QUESTIONS = [
    {
        "question": "Which sport is Duke Kahanamoku most famous for?",
        "options": ["Surfing", "Basketball", "Baseball", "Football"],
        "answer": "Surfing"
    },
    {
        "question": "Simone Biles is famous for competing in which sport?",
        "options": ["Gymnastics", "Swimming", "Tennis", "Track and Field"],
        "answer": "Gymnastics"
    },
    {
        "question": "Michael Jordan is best known for playing which sport?",
        "options": ["Basketball", "Baseball", "Football", "Golf"],
        "answer": "Basketball"
    },
    {
        "question": "Serena Williams is one of the greatest athletes in which sport?",
        "options": ["Tennis", "Soccer", "Volleyball", "Track"],
        "answer": "Tennis"
    },
    {
        "question": "Which athlete is an Olympic gold medalist?",
        "options": ["Usain Bolt", "Kaori Sakamoto", "Tom Brady", "Lionel Messi"],
        "answer": "Usain Bolt"
    }
]

@app.route('/')
def home():
    return render_template('quiz_home.html')


@app.route('/start')
def startQuiz():
    session['questionIndex'] = 0
    session['numCorrect'] = 0
    return redirect(url_for('quiz'))


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    questionIndex = session.get('questionIndex', 0)
    numCorrect = session.get('numCorrect', 0)

    if request.method == 'POST':
        userAnswer = request.form['answer']
        correctAnswer = QUESTIONS[questionIndex]['answer']

        if userAnswer == correctAnswer:
            numCorrect += 1
            session['numCorrect'] = numCorrect

        questionIndex += 1
        session['questionIndex'] = questionIndex

        if questionIndex >= len(QUESTIONS):
            return redirect(url_for('result'))

    if questionIndex < len(QUESTIONS):
        currentQuestion = QUESTIONS[questionIndex]
        return render_template('quiz.html',
                               question=currentQuestion,
                               questionNumber=questionIndex + 1,
                               totalQuestions=len(QUESTIONS))
    return redirect(url_for('result'))

@app.route('/result')
def result():
    finalScore = session.get('numCorrect', 0)
    return render_template('result.html',
                           finalScore=finalScore,
                           totalQuestions=len(QUESTIONS))


if __name__ == '__main__':
    app.run(debug=True)