
from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        topic = request.form['search']
        url = 'https://newsapi.org/v2/everything'

        params = {
            'q': topic,
            'apiKey': '749337dc9a3347108a188b3abf404acb',
        }

        response = requests.get(url, params=params)
        data = response.json()

        articles = data['articles']
        return render_template("index.html", articles=articles)

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, port=5132)





