"""Initialize Flask app."""
import dash
from flask import Flask
from flask_assets import Environment


def create_app():
    """Construct core Flask application with embedded Dash app."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    assets = Environment()
    assets.init_app(app)

    with app.app_context():
        # Import parts of our core Flask app
        # from . import routes
        from .assets import compile_static_assets

        from plotlydash.dashboards import create_dashboard
        create_dashboard(app)

        # Compile static assets
        compile_static_assets(assets)

    register_blueprints(app)

    return app



def register_blueprints(server):
    from application.routes import server_bp

    server.register_blueprint(server_bp)

