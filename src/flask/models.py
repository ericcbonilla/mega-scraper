from peewee import *
import sqlite3
from sqlite3 import Error
import datetime as dt

# db = SqliteDatabase('microblog.db')

db = SqliteDatabase('megascraper.db', check_same_thread=False)

def setup():
	db.connect()

def teardown():
	if not db.is_closed():
		db.close()


class User(Model):
	email = CharField()

	class Meta:
		database = db

class Task(Model):
	keywords = CharField()
	lastSearched = DateField(default=dt.datetime.now)

	class Meta:
		database = db

class Subscriber(Model):
	taskId = ForeignKeyField(Task, related_name="task_subscribed_to")
	userId = ForeignKeyField(User, related_name="user_owned")

	class Meta:
		database = db





db.create_tables([User, Subscriber, Task], safe=True)
