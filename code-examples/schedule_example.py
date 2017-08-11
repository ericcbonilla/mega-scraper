from apscheduler.schedulers.background import BackgroundScheduler
import time
def foo():
	print("I am a job")


scheduler = BackgroundScheduler()

scheduler.start()



scheduler.add_job(foo, 'interval', seconds=5)

while(1):
	time.sleep(1)
