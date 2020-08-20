"""Routes for parent Flask app."""
from flask import render_template
from flask import current_app as app
from flask import Blueprint

server_bp = Blueprint('main', __name__)

@server_bp.route('/')
def home():
    """Landing page."""
    return render_template(
        'index.jinja2',
        title='Plotly Dash Flask Tutorial',
        description='Embed Plotly Dash into your Flask applications.',
        template='home-template',
        body="This is a homepage served with Flask."
    )

@server_bp.route('/healthcheck')
def mycheckup():
    """Landing page."""
    return "i am good"
