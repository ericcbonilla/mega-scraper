import time
from flask import Flask, render_template
from apscheduler.schedulers.background import BackgroundScheduler
from bot import *
from forms import QueryForm

def foo():
	print("I am a job")

app = Flask(__name__)
scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(foo, 'interval', seconds=10)

@app.route('/')
def index():
	print("Entered the index")
	return "megalink scraper"

# For heroku, when we deploy
if __name__ == '__main__':
	# Bind to PORT if defined, otherwise default to 5000.
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
