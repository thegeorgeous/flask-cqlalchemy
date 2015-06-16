from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table, create_keyspace_simple
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack


class CQLAlchemy(object):

    def __init__(self, app=None):
        self.columns = columns
        self.Model = Model
        self.app = app
        self.sync_table = sync_table
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self._hosts_ = app.config['CASSANDRA_HOSTS']
        self._default_keyspace_ = app.config['CASSANDRA_KEYSPACE']
        consistency = app.config.get('CASSANDRA_CONSISTENCY', 1)
        lazy_connect = app.config.get('CASSANDRA_LAZY_CONNECT', False)
        retry_connect = app.config.get('CASSANDRA_RETRY_CONNECT', False)
        setup_kwargs = app.config.get('CASSANDRA_SETUP_KWARGS', {})

        # Create a keyspace with a replication factor of 2
        # If the keyspace already exists, it will not be modified
        connection.setup(self._hosts_,
                         self._default_keyspace_,
                         consistency=consistency,
                         lazy_connect=lazy_connect,
                         retry_connect=retry_connect,
                         **setup_kwargs
                         )

    def create_all(self):
        create_keyspace_simple(self._default_keyspace_, 2)
        models = [cls for cls in self.Model.__subclasses__()]
        for model in models:
            sync_table(model)
