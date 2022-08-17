from flask import Flask, render_template

# name чтобы понять откуда стартует проект
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html', title='Главная')


if __name__ == '__main__':
    app.run(debug=True, port=5656)