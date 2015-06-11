# Flask-CQLAlchemy

Flask-CQLAlchemy handles connections to Cassandra clusters
and gives a unified easier way to declare models and their
columns

## Usage
```
import uuid
from flask import Flask
from flask.ext.cqlalchemy import CQLAlchemy

app = Flask(__name__)
app.config['CASSANDRA_DB'] = ['127.0.0.1']
app.config['CASSANDRA_KEYSPACE'] = "cqlengine"
db = CQLAlchemy(app)


class User(db.Model):
    example_id = db.columns.UUID(primary_key=True, default=uuid.uuid4)
    username = db.columns.Text(required=False)
```
