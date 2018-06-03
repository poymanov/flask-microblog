from app import app, db
from app.models import User, Post

@app.shell_context_proccesor
def make_shell_context():
	return {'db': db, 'User': User, 'Post': Post}
