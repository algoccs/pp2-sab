from flask import Flask, redirect, url_for, session
from database import get_next_question


app = Flask(__name__)
app.config['SECRET_KEY'] = 'LaClaveMasSecretaDelMundo' 

def index():
    session['quiz'] = 1
    session['prev_question'] = 0
    return '<a href="/test">Click para iniciar el questionario!</a>'

def test():

    result = get_next_question(session['prev_question'], session['quiz'])
    if result is None or result == 0:
        return redirect(url_for('result'))
    else:
        session['prev_question'] = result[0]
    
    return f'{result}'

def result():
    return 'Aqui se muestra el resultado!'

app.add_url_rule('/', 'index', index)
app.add_url_rule('/test', 'test', test)
app.add_url_rule('/result', 'result', result)

if __name__ == "__main__":
    app.run()
