# Created by Immanuel Amirtharaj
# app.py

import peewee
import time
<<<<<<< HEAD
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

=======
import datetime

import email_manager
from email_manager import EmailObject
import reddit_manager

import logging
logging.basicConfig()

app = Flask(__name__)

last_searched_time = time.time()


# export FLASK_APP=app.py
# flask run

>>>>>>> flask-db

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

<<<<<<< HEAD
    return found_subscriber
=======
def handle_job():
	print("I am a job")
	task_list = Task.select()
	global last_searched_time
	print("The last searched time is ", last_searched_time)
	for task in task_list:
		print(task.keywords)
		post_list = reddit_manager.get_posts(task.keywords, int(last_searched_time))
		print("length of post list for ", task.keywords, " is ", len(post_list))

		if len(post_list) > 0:
			print("We will send the email!")
			email_list = Subscriber.select().join(User).where(Subscriber.taskId == task.id)
			send_list = []
			for email in email_list:
				print(email.email)
				send_list.append(email.email)
				#def __init__(self, destination, subject, description):

			email_manager.send_message(send_list, "found", task)

	last_searched_time = time.time()


scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(handle_job, 'interval', seconds=10)
>>>>>>> flask-db


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
<<<<<<< HEAD
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
=======
	# Bind to PORT if defined, otherwise default to 5000.
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port, threaded=True)
>>>>>>> flask-db
