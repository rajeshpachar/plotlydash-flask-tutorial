"""Instantiate a Dash app."""
from logging import root
import dash
from flask.helpers import get_root_path
from auth.basic_auth import BasicAuth
from plotlydash.loader import get_modules
import json

VALID_USERNAME_PASSWORD_PAIRS = {
    'hello': 'world'
}

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash('auth', external_stylesheets=external_stylesheets)

def create_dashboard(server):
    """Create a Plotly Dash dashboard."""
    results = get_modules('layouts')

    for path, pkg in results.items():
        register_fun = getattr(pkg.get('callbacks', ''), 'register_callbacks', register_callbacks)
        layout_fun = pkg.get('layout')
        index_html = getattr(pkg.get('index_html', {}), 'get_html', get_html)()
        path_names = path.split('/')
        default_title = path_names[len(path_names) -1]
        layout = layout_fun.get_layout()
        title = getattr(layout_fun, 'title', default_title)
        auth_data = getattr(layout_fun, 'auth_data', {})

        register_dashapp(server, title, path+'_dashboard', layout, register_fun, html_layout=index_html, auth_data= auth_data)
 
def register_dashapp(app, title, base_pathname, layout, register_callbacks_fun, html_layout=None, auth_data={}):
    # Meta tags for viewport responsiveness
    meta_viewport = {"name": "viewport", "content": "width=device-width, initial-scale=1, shrink-to-fit=no"}
    root_path = get_root_path(__name__)
    my_dashapp = dash.Dash(__name__,
                           server=app,
                           url_base_pathname=f'/{base_pathname}/',
                           assets_folder=root_path + f'/{base_pathname}/assets/',
                           meta_tags=[meta_viewport])
    auth_data.update({'basepath': base_pathname})
    BasicAuth(my_dashapp, auth_data, VALID_USERNAME_PASSWORD_PAIRS)

    # with app.app_context():
    my_dashapp.title = title
    my_dashapp.layout = layout
    if html_layout:
        # Custom HTML layout
        my_dashapp.index_string = html_layout
    register_callbacks_fun(my_dashapp)


def get_html():
    return None

def register_callbacks(dashapp):
    pass