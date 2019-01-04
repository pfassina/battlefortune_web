from flask import Flask, render_template, url_for
app = Flask(__name__)

battle_log = [
    {
        'game': 'Test Game',
        'rounds': 100,
        'nation': 'Atlantis',
        'winratio': '20%',
        'gcost': 2000,
        'return': -800
    },
    {
        'game': 'Test Game',
        'rounds': 100,
        'nation': "R'lyeh",
        'winratio': '80%',
        'gcost': 1200,
        'return': 800
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=battle_log)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
