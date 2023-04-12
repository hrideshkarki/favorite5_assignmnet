from flask import Flask, render_template
from app import app

app = Flask(__name__)

# Define our top 5 favorite sports figures
favorite_figures = [
    'Cristiano Ronaldo',
    'Mesut Ozil',
    'Erling Haaland',
    'Daniil Medvedev',
    'Stephen Curry'
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/favorite5')
def favorite5():
    return render_template('favorite.html', figures=favorite_figures)

if __name__ == '__main__':
    app.run(debug=True)
