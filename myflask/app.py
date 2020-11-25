from flask import Flask, render_template, url_for, request
from datetime import date
from model import *
from database import *

today = date.today()

app = Flask(__name__)
all_tasks = []

@app.route('/', methods=['GET', 'POST'])
def home():
    global all_tasks
    if request.method == 'POST':
        content = request.form["content"]
        date = today.strftime("%d/%m/%Y")
        add_task(content, date) 
        all_tasks = return_all_tasks()
    return render_template("home.html", all_tasks = all_tasks)

@app.route('/delete_task/<string:tid>')
def delete_selected_task(tid):
    global all_tasks
    delete_task(tid)
    all_tasks = return_all_tasks()
    return render_template("home.html", all_tasks = all_tasks)

@app.route('/update_task/<string:tid>', methods=['GET', 'POST'])
def update_selected_task(tid):
    global all_tasks
    selected_task = return_task(tid)
    if request.method == 'POST':
        content = request.form["content_update"]
        edit_task(tid, content)
    return render_template("update_task.html", selected_task = selected_task)



if __name__ == "__main__":
    app.run(debug=True)