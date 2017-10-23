# mega-scraper

Megascraper is a web application where users can type in keywords for movies they want downloaded.  Once the movie gets onto r/megalinks, the user requesting it gets an email

## Technologies Used
Currently runs on Flask, using Peewee as ORM and sqlite.  Uses APscheduler to schedule tasks

## Todo
- Switch to Celery as task manager
- Make a cleaner web frontend
- Store entries in an actual databse instead of sqlite file
