from __future__ import absolute_import
from abc import ABCMeta, abstractmethod
from six import iteritems, add_metaclass


@add_metaclass(ABCMeta)
class Auth(object):
    def __init__(self, app, auth_data, authorization_hook=None, _overwrite_index=True):
        self.app = app
        self.basepath = auth_data.get('basepath')
        self._protect_views()
        self._auth_hooks = [authorization_hook] if authorization_hook else []

    def _protect_views(self):
        # TODO - allow users to white list in case they add their own views
        for view_name, view_method in iteritems(
                self.app.server.view_functions):
            # this is not ensure each path auth data is overridden by next auth data.
            if self.basepath not in view_name:
                continue
            self.app.server.view_functions[view_name] = \
                self.auth_wrapper(view_method)

    def is_authorized_hook(self, func):
        self._auth_hooks.append(func)
        return func

    @abstractmethod
    def is_authorized(self):
        pass

    @abstractmethod
    def auth_wrapper(self, f):
        pass

    @abstractmethod
    def login_request(self):
        pass
