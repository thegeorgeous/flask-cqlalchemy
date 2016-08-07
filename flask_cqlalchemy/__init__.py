# -*- coding: utf-8 -*-
"""
flask_cqlalchemy

:copyright: (c) 2015-2016 by George Thomas
:license: BSD, see LICENSE for more details

"""
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import (
    sync_table, create_keyspace_simple, sync_type
)
from cassandra.cqlengine import columns
from cassandra.cqlengine import models
from cassandra.cqlengine import usertype

try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack


class CQLAlchemy(object):
    """The CQLAlchemy class. All CQLEngine methods are available as methods of
    Model or columns attribute in this class.
    No teardown method is available as connections are costly and once made are
    ideally not disconnected.
    """

    def __init__(self, app=None):
        """Constructor for the class"""
        self.columns = columns
        self.Model = models.Model
        self.UserType = usertype.UserType
        self.app = app
        self.sync_table = sync_table
        self.sync_type = sync_type
        self.create_keyspace_simple = create_keyspace_simple
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """Bind the CQLAlchemy object to the app.

        This method set all the config options for the connection to
        the Cassandra cluster and creates a connection at startup.
        """
        self._hosts_ = app.config['CASSANDRA_HOSTS']
        self._keyspace_ = app.config['CASSANDRA_KEYSPACE']
        consistency = app.config.get('CASSANDRA_CONSISTENCY', 1)
        lazy_connect = app.config.get('CASSANDRA_LAZY_CONNECT', False)
        retry_connect = app.config.get('CASSANDRA_RETRY_CONNECT', False)
        setup_kwargs = app.config.get('CASSANDRA_SETUP_KWARGS', {})

        if not self._hosts_ and self._keyspace_:
            raise NoConfig("""No Configuration options defined.
            At least CASSANDRA_HOSTS and CASSANDRA_CONSISTENCY
            must be supplied""")
        connection.setup(self._hosts_,
                         self._keyspace_,
                         consistency=consistency,
                         lazy_connect=lazy_connect,
                         retry_connect=retry_connect,
                         **setup_kwargs)

    def sync_db(self):
        """Sync all defined tables. All defined models must be imported before
        this method is called
        """
        models = get_subclasses(self.Model)
        for model in models:
            sync_table(model)

    def set_keyspace(self, keyspace_name=None):
        """ Changes keyspace for the current session if keyspace_name is
        supplied. Ideally sessions exist for the entire duration of the
        application. So if the change in keyspace is meant to be temporary,
        this method must be called again without any arguments
        """
        if not keyspace_name:
            keyspace_name = self.app.config['CASSANDRA_KEYSPACE']
        models.DEFAULT_KEYSPACE = keyspace_name
        self._keyspace_ = keyspace_name


class NoConfig(Exception):
    """ Raised when CASSANDRA_HOSTS or CASSANDRA_KEYSPACE is not defined"""
    pass


# some helper functions for mashing the class list
def flatten(lists):
    """flatten a list of lists into a single list"""
    return [item for sublist in lists for item in sublist]


def get_subclasses(cls):
    """get all the non abstract subclasses of cls"""
    if cls.__abstract__:
        return flatten([get_subclasses(scls) for scls in cls.__subclasses__()])
    else:
        return [cls]
