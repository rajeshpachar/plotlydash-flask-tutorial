"""Instantiate a Dash app."""
from logging import root
import dash
from flask.helpers import get_root_path
from auth.basic_auth import BasicAuth

VALID_USERNAME_PASSWORD_PAIRS = {
    'hello': 'world'
}

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash('auth', external_stylesheets=external_stylesheets)

def create_dashboard(server):
    """Create a Plotly Dash dashboard."""
    from layouts.sample.dashapp1.layout import layout as layout1
    from layouts.sample.dashapp1.callbacks import register_callbacks as register_callbacks1
    register_dashapp(server, 'Dashapp 1', 'dashboard1', layout1, register_callbacks1)

    from layouts.sample.dashapp2.layout import layout as layout2
    from layouts.sample.dashapp2.callbacks import register_callbacks as register_callbacks2
    register_dashapp(server, 'Dashapp 2', 'dashboard2', layout2, register_callbacks2)

    from layouts.sample.stockticker.layout import create_layout as create_layout3
    from layouts.sample.stockticker.callbacks import register_callbacks as register_callbacks2
    from layouts.sample.stockticker.index_html import html_layout as html_layout3
    register_dashapp(server, 'Dashapp 2', 'dashboard3', create_layout3(), register_callbacks2, html_layout=html_layout3)


def register_dashapp(app, title, base_pathname, layout, register_callbacks_fun, html_layout=None):
    # Meta tags for viewport responsiveness
    meta_viewport = {"name": "viewport", "content": "width=device-width, initial-scale=1, shrink-to-fit=no"}
    root_path = get_root_path(__name__)
    print(f"{root_path} is root path ")
    my_dashapp = dash.Dash(__name__,
                           server=app,
                           url_base_pathname=f'/{base_pathname}/',
                           assets_folder=root_path + f'/{base_pathname}/assets/',
                           meta_tags=[meta_viewport])

    BasicAuth(my_dashapp, VALID_USERNAME_PASSWORD_PAIRS)

    # with app.app_context():
    my_dashapp.title = title
    my_dashapp.layout = layout
    if html_layout:
        # Custom HTML layout
        my_dashapp.index_string = html_layout
    register_callbacks_fun(my_dashapp)

