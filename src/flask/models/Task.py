class Task(db.model):

	id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True)
    keywords = db.Column(db.String(120), unique=True)
    lastSearched = db.Column(db.DateTime)

    def __init__(self, email, keywords, lastSearched=None):
    	self.email = email
    	self.keywords = keywords
    	self.lastSearched = datetime.utcnow()
