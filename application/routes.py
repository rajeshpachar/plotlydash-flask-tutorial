"""Core Flask app routes."""
from flask import Blueprint, render_template
from flask import current_app as app


main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates',
                    static_folder='static')


@main_bp.route('/')
def home():
    """Landing page."""
    return render_template('index.jinja2',
                           title='Plotly Dash & Flask Tutorial',
                           template='home-template',
                           body="This is an example homepage served with Flask.")
