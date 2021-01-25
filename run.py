from app import app, db, deadline_mgmt
from app.models import TinyText


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'TinyText': TinyText}

# add first deadline
deadline_mgmt.init_deadline()