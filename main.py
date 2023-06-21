from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    user = {
        "name": "Ходящий Ч-п",
        "age": 61
    }
    return render_template('index.html', user=user)


@app.route('/login')
def about():
    user = {
        "name": "Ходящий Ч-п",
        "age": 61
    }
    return render_template('index.html', user=user)

@app.route('/contact')
def contact():
    user = {
        "name": "Ходящий Ч-п",
        "age": 61
    }
    return render_template('profile.html', user=user)

@app.route('/404')
def app404():
    return '''
     404 ТЫ НЕ ПРАВИЛЬНО ЗАШЁЛ НА СТРАНИЦУ
     '''

@app.route('/about')
def pronas():
    team_name = 'team-9'
    age = 10
    return '<h1>ABOUT<h1> <p>TeamName = ' + team_name + '</p> <h3>Возраст = ' + str(age) + '</h3>'

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/profile')
def prfl():
    user = {
        "name": "Ходящий Ч-п",
        "age": 61
    }
    return render_template('profile.html', user=user)

if __name__ == "__main__":
    app.run(debug=True)