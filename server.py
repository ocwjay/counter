from ctypes import cast
from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "Not enough beer left to learn this."

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 1
    if 'visits' not in session:
        session['visits'] = 1
    else:
        session['visits'] += 1
    return render_template('index.html')

@app.route('/count2')
def add_2():
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 2
    return redirect('/')

@app.route('/count_user', methods=['POST'])
def add_user_count():
    session['user_num'] = request.form['user_input']
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += int(session['user_num']) - 1
    return redirect('/')

@app.route('/destroy_session')
def reset_counter():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)