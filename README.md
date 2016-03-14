# Flask-CQLAlchemy

[![Latest Version](https://img.shields.io/pypi/v/flask-cqlalchemy.svg)](https://pypi.python.org/pypi/Flask-CQLAlchemy)
[![Build Status](https://travis-ci.org/thegeorgeous/flask-cqlalchemy.svg?branch=master)](https://travis-ci.org/thegeorgeous/flask-cqlalchemy)
[![Python Versions](https://img.shields.io/pypi/pyversions/flask-cqlalchemy.svg)](https://pypi.python.org/pypi/Flask-CQLAlchemy)
[![License](https://img.shields.io/pypi/l/Flask-CQLAlchemy.svg)](https://pypi.python.org/pypi/Flask-CQLAlchemy)
[![Code Climate](https://codeclimate.com/github/thegeorgeous/flask-cqlalchemy/badges/gpa.svg)](https://codeclimate.com/github/thegeorgeous/flask-cqlalchemy)
[![Downloads](https://img.shields.io/pypi/dm/flask-cqlalchemy.svg)](https://pypi.python.org/pypi/Flask-CQLAlchemy)


Flask-CQLAlchemy handles connections to Cassandra clusters
and gives a unified easier way to declare models and their
columns

**Now with Python 3 support**

## Installation
```shell
pip install flask-cqlalchemy
```

## Dependencies
As such Flask-CQLAlchemy depends only on the cassandra-driver. It is assumed
that you already have flask installed.

Flask-CQLAlchemy has been tested with versions 2.6.0, 2.7.2, 3.0.0 and 3.1.0 of
cassandra-driver. It is known to work with all versions >=2.5, but use it at
your own risk. All previous versions of Flask-CQLAlchemy are deprecated.

## Example
```python
#example_app.py
import uuid
from flask import Flask
from flask.ext.cqlalchemy import CQLAlchemy

app = Flask(__name__)
app.config['CASSANDRA_HOSTS'] = ['127.0.0.1']
app.config['CASSANDRA_KEYSPACE'] = "cqlengine"
db = CQLAlchemy(app)


class User(db.Model):
    uid = db.columns.UUID(primary_key=True, default=uuid.uuid4)
    username = db.columns.Text(required=False)
```

## Usage
Start a python shell
```python
>>from example_app import db, User
>>db.sync_db()
>>user1 = User.create(username='John Doe')
```
For a complete list of available method refer to the cqlengine
[Model documentation](http://datastax.github.io/python-driver/api/cassandra/cqlengine/models.html)

## Configuration Options
CQLAlchemy provides all the option available in the cqlengine connection.setup()
method

* `CASSANDRA_HOSTS` - A list of hosts
* `CASSANDRA_KEYSPACE` - The default keyspace to use
* `CASSANDRA_CONSISTENCY` - The global default ConsistencyLevel
* `CASSANDRA_LAZY_CONNECT` - True if should not connect until first use
* `CASSANDRA_RETRY_CONNECT` - True if we should retry to connect even if there was
  a connection failure initially
* `CASSANDRA_SETUP_KWARGS` - Pass-through keyword arguments for Cluster()

## Contributing
Found a bug? Need a feature? Open it in issues, or even better, open a PR.
Please include tests in the PR.
