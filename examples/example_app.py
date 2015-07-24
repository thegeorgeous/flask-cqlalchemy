import uuid
from flask import Flask
from flask.ext.cqlalchemy import CQLAlchemy

app = Flask(__name__)
app.config['CASSANDRA_HOSTS'] = ['127.0.0.1']
app.config['CASSANDRA_KEYSPACE'] = "cqlengine"
app.config['CASSANDRA_SETUP_KWARGS'] = {'protocol_version': 3}
db = CQLAlchemy(app)


class User(db.Model):
    example_id = db.columns.UUID(primary_key=True, default=uuid.uuid4)
    username = db.columns.Text(index=True, required=False)
