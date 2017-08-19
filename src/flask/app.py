# Created by Immanuel Amirtharaj
# app.py

import peewee
import time
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, request
from models import Task, User, Subscriber
from forms import AddTaskForm

app = Flask(__name__)

# export FLASK_APP=app.py
# flask run

def foo():
    print("I am a job")

scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(foo, 'interval', seconds=5)


def create_or_find_user(email):
    try:
        found_user = User.get(User.email == email)
    except User.DoesNotExist:
        User.create(email=email).save()
        found_user = User.get(User.email == email)

    return found_user


def create_or_find_task(keywords):
    try:
        found_task = Task.get(Task.keywords == keywords)
    except Task.DoesNotExist:
        Task.create(keywords=keywords).save()
        found_task = Task.get(Task.keywords == keywords)

    return found_task


def create_or_find_subscriber(user_id, task_id):
    try:
        found_subscriber = Subscriber.get(Subscriber.userId == user_id, Subscriber.taskId == task_id)
    except Subscriber.DoesNotExist:
        Subscriber.create(userId=user_id, taskId = task_id).save()
        found_subscriber = Subscriber.get(Subscriber.userId == user_id, Subscriber.taskId == task_id)

    return found_subscriber


# Handle email
@app.route('/tasks/new', methods=['POST'])
def addTask():

    email = request.form['email']
    keywords = request.form['keywords']

    new_task = create_or_find_task(keywords)
    new_user = create_or_find_user(email)

    create_or_find_subscriber(new_user.id, new_task.id)

    return "Success"


@app.route('/forms/add-task', methods=['GET', 'POST'])
def addTaskThroughForm():

    form = AddTaskForm(request.form)
    if request.method == 'POST':
        new_task = create_or_find_task(form.query.data)
        new_user = create_or_find_user(form.email.data)
        subscriber = create_or_find_subscriber(new_user.id, new_task.id)

        flash('New subscriber created: ' + str(subscriber.id))
        # return redirect(url_for('login'))
    return render_template('templates/add_task.html', form=form)


@app.route('/')
def index():
    print("Entered the index")
    return "megalink scraper index"

# For heroku, when we deploy
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
