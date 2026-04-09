# Create a simple Flask application that retrieves a meme from an API and displays the meme with its source subreddit

from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    memeUrl = "https://meme-api.com/gimme/wholesomememes"

    response = requests.request("GET", memeUrl)
    memeData = response.json()

    memeImage = memeData["url"]
    memeSource = memeData["subreddit"]
    memeTitle = memeData["title"]

    return render_template('meme.html',
                           memeImage=memeImage,
                           memeSource=memeSource,
                           memeTitle=memeTitle)

if __name__ == '__main__':
    app.run(debug=True)