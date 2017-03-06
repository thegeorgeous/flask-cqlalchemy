# Flask-CQLAlchemy

[![Latest Version](https://img.shields.io/pypi/v/flask-cqlalchemy.svg)](https://pypi.python.org/pypi/Flask-CQLAlchemy)
[![License](https://img.shields.io/pypi/l/Flask-CQLAlchemy.svg)](https://pypi.python.org/pypi/Flask-CQLAlchemy)
[![Python Versions](https://img.shields.io/pypi/pyversions/flask-cqlalchemy.svg)](https://pypi.python.org/pypi/Flask-CQLAlchemy)
[![Build Status](https://travis-ci.org/thegeorgeous/flask-cqlalchemy.svg?branch=master)](https://travis-ci.org/thegeorgeous/flask-cqlalchemy)
[![Code Climate](https://codeclimate.com/github/thegeorgeous/flask-cqlalchemy/badges/gpa.svg)](https://codeclimate.com/github/thegeorgeous/flask-cqlalchemy)


Flask-CQLAlchemy handles connections to Cassandra clusters
and gives a unified easier way to declare models and their
columns

**Now with support for PyPy**

## Installation
```shell
pip install flask-cqlalchemy
```

## Dependencies
As such Flask-CQLAlchemy depends only on the cassandra-driver. It is assumed
that you already have flask installed.

Flask-CQLAlchemy has been tested with all minor versions greater than 2.6 of
cassandra-driver. All previous versions of Flask-CQLAlchemy are deprecated.
All tests are run against the latest patch version. If you have problems using
the plugin, try updating to the latest patch version of the minor version you
are using.

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

### User Defined Types

```python
#example_app_udt.py
import uuid
from flask import Flask
from flask_cqlalchemy import CQLAlchemy

app = Flask(__name__)
app.config['CASSANDRA_HOSTS'] = ['127.0.0.1']
app.config['CASSANDRA_KEYSPACE'] = "cqlengine"
app.config['CASSANDRA_SETUP_KWARGS'] = {'protocol_version': 3}
db = CQLAlchemy(app)


class address(db.UserType):
    street = db.columns.Text()
    zipcode = db.columns.Integer()

class users(db.Model):
    __keyspace__ = 'cqlengine'
    name = db.columns.Text(primary_key=True)
    addr = db.columns.UserDefinedType(address)

```

## Usage
Start a python shell
```python
>>>from example_app import db, User
>>>db.sync_db()
>>>user1 = User.create(username='John Doe')
```
### User Defined Types

```python
>>>from example_app_udt import db, address, users
>>>db.sync_db()
>>>user_address = address(street="Easy St.", zipcode=99999
>>> user
users(name=u'Joe', addr=<example_app_udt.address object at 0x7f4498063310>)
>>> user.addr
<example_app_udt.address object at 0x7f4498063310>
>>> user.addr.street
u'Easy St.'
>>> user.addr.zipcode
99999
```

For a complete list of available methods refer to the cqlengine
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

## Beta Features
Flask CQLAlchemy supports User Defined Types, provided you are using Cassandra
versions 2.1 or above. However Travis only provides 2.0.9 for testing and so this
feature has not undergone rigorous testing.

## Contributing
Found a bug? Need a feature? Open it in issues, or even better, open a PR.
Please include tests in the PR.
