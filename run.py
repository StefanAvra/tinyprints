from app import app, db
from app.models import TinyText
from app.deadline_mgmt import renew_deadline

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'TinyText': TinyText}

# add first deadline
renew_deadline()