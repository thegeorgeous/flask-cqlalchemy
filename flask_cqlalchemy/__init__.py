from cassandra.cqlengine import connection
from cassandra.cqlengine.management import create_keyspace_simple, sync_table
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
        self.db = app.config['CASSANDRA_DB']
        self.keyspace = app.config['CASSANDRA_KEYSPACE']

        # Create a keyspace with a replication factor of 2
        # If the keyspace already exists, it will not be modified
        self.connection = connection.setup(
            self.db, self.keyspace, protocol_version=3)

    def create_all(self):
        create_keyspace_simple(self.keyspace, 2)
