from flask import Flask, render_template, request, redirect
import re

app = Flask(__name__)

tasks = []
emails = []
priorities = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks, emails=emails, priorities=priorities)

@app.route('/submit', methods = ['POST'])
def submit():
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']

    if priority != 'Select' and task != '' and re.search('@', email):
        tasks.append(task)
        emails.append(email)
        priorities.append(priority)

    return redirect('/')

@app.route('/clear', methods = ['POST'])
def clear():
    tasks[:] = []
    emails[:] = []
    priorities[:] = []
    return redirect('/')

if __name__ == '__main__':
    app.run()