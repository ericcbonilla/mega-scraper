# Created by Immanuel Amirtharaj
# app.py

import peewee
import time
import datetime
import logging
import email_manager
import reddit_manager
import praw
from constants import *

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, request, render_template, flash, session
from models import Task, User, Subscriber
from email_manager import EmailObject

app = Flask(__name__)
app.secret_key = 'super secret key'

logging.basicConfig()

last_searched_time = time.time()


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


def foo():
    print("I am a job")


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


def retrieve_posts(subreddits, search_query='', limit=5):
    reddit = praw.Reddit(SITE_NAME, user_agent=USER_AGENT)
    results = {}

    # TODO: implement retrieval by search term
    if not search_query:
        for sub in subreddits:
            results[sub] =  {}
            for post in reddit.subreddit(sub).hot(limit=limit):
                results[sub][post.title] = post.url
    return results


# Handle email
@app.route('/tasks/new', methods=['POST'])
def add_task():

    email = request.form['email']
    keywords = request.form['keywords']

    new_task = create_or_find_task(keywords)
    new_user = create_or_find_user(email)

    create_or_find_subscriber(new_user.id, new_task.id)

    return "Success"


@app.route('/add-task', methods=['GET', 'POST'])
def search():
    error = None
    if request.method == 'POST':
        search_terms = request.form['search']
        subreddits = request.form['subreddits']
        # TODO: getting error: database is locked
        # new_task = create_or_find_task(search_terms)
        # new_user = create_or_find_task(request.form['email'])
        # subscriber = create_or_find_subscriber(new_user.id, new_task.id)

        # TODO: Validation
        # if request.form['username'] != current_app.config['USERNAME']:
        #     error = 'Invalid username'
        # elif request.form['password'] != current_app.config['PASSWORD']:
        #     error = 'Invalid password'
        # else:
        # flash('New subscriber created: ' + str(subscriber.id)
        #  + 'under ' + new_user.email)
        session['logged_in'] = True
        flash(str(retrieve_posts([subreddits])))

        # return redirect(url_for('flaskr.show_entries'))
    return render_template('add_task.html', error=error)


@app.route('/')
def index():
    print("Entered the index")
    return "megalink scraper index"


# For heroku, when we deploy
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, threaded=True)
