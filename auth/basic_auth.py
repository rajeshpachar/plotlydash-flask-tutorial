from .auth import Auth
import base64
import flask
from .constants import *

class BasicAuth(Auth):
    def __init__(self, app, auth_data, username_password_list):
        Auth.__init__(self, app, auth_data)
        # todo: once production, change this to some auth
        self.auth_data = auth_data or {'type': NO_AUTH}
        self._users = username_password_list \
            if isinstance(username_password_list, dict) \
            else {k: v for k, v in username_password_list}

    def is_authorized(self):
        auth_type = self.auth_data.get('type')
        if not auth_type or auth_type == NO_AUTH:
            return True
        elif auth_type == STATIC_KEY:
            token = flask.request.args.get('key')
            path = str(flask.request.path).strip('/')
            if not path.endswith('_dashboard'):
                return True
            return token == self.auth_data.get('key')

        header = flask.request.headers.get('Authorization', None)
        if not header:
            return True
        username_password = base64.b64decode(header.split('Basic ')[1])
        username_password_utf8 = username_password.decode('utf-8')
        username, password = username_password_utf8.split(':', 1)
        print(f"{username_password} is authorized" )
        return self._users.get(username) == password

    def login_request(self):
        return flask.Response(
            'Login Required',
            headers={'WWW-Authenticate': 'Basic realm="User Visible Realm"'},
            status=401)

    def auth_wrapper(self, f):
        def wrap(*args, **kwargs):
            if not self.is_authorized():
                return flask.Response(status=403)

            response = f(*args, **kwargs)
            return response
        return wrap
