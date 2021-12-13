# Flask-CQLAlchemy

[![Latest Version](https://img.shields.io/pypi/v/flask-cqlalchemy.svg)](https://pypi.python.org/pypi/Flask-CQLAlchemy)
[![License](https://img.shields.io/pypi/l/Flask-CQLAlchemy.svg)](https://pypi.python.org/pypi/Flask-CQLAlchemy)
[![Python Versions](https://img.shields.io/pypi/pyversions/flask-cqlalchemy.svg)](https://pypi.python.org/pypi/Flask-CQLAlchemy)
[![CI Build and Test](https://github.com/thegeorgeous/flask-cqlalchemy/actions/workflows/ci-build-test.yml/badge.svg?branch=master)](https://github.com/thegeorgeous/flask-cqlalchemy/actions/workflows/ci-build-test.yml)
[![Code Climate](https://codeclimate.com/github/thegeorgeous/flask-cqlalchemy/badges/gpa.svg)](https://codeclimate.com/github/thegeorgeous/flask-cqlalchemy)


Flask-CQLAlchemy handles connections to Cassandra clusters and gives a unified easier way to declare models and
their columns.

## Installation
```shell
$ pip install flask-cqlalchemy
```

## Dependencies
As Flask-CQLAlchemy depends only on the `cassandra-driver`. It is assumed that you already have `Flask` installed.

Flask-CQLAlchemy has been tested with all versions of the `cassandra-driver>=3.22.0` and Cassandra 3.0.25, 3.11.11,
4.x. All previous versions and configurations are deprecated. Used to be reported that plugin worked with
`cassandra-driver>=2.5`, we can not guarantee proper work of older configurations so use on your own. Some versions of
`cassandra-driver` can be incompatible with some versions of Cassandra itself either. 

If you have problems using the plugin, try updating to the latest patch version of the minor version you are using.

## Example

```python
# example_app.py
import uuid
from flask import Flask
from flask_cqlalchemy import CQLAlchemy

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
# example_app_udt.py
from flask import Flask

from flask_cqlalchemy import CQLAlchemy

app = Flask(__name__)
app.config['CASSANDRA_HOSTS'] = ['127.0.0.1']
app.config['CASSANDRA_KEYSPACE'] = "cqlengine"
app.config['CASSANDRA_SETUP_KWARGS'] = {'protocol_version': 3}
db = CQLAlchemy(app)


class Address(db.UserType):
    street = db.columns.Text()
    zipcode = db.columns.Integer()


class Users(db.Model):
    __keyspace__ = 'cqlengine'
    name = db.columns.Text(primary_key=True)
    addr = db.columns.UserDefinedType(Address)
```

## Usage
Enter in Python Interpreter:
```python
>>> from example_app import db, User
>>> db.sync_db()
>>> user1 = User.create(username='John Doe')
>>> user1
User(example_id=UUID('f94b6156-2964-4d46-919c-d6e4abcb9ef1'), username='John Doe')
```

### User Defined Types
```python
>>> from example_app_udt import db, Address, Users
>>> db.sync_db()
>>> user_address = Address(street="Easy Street, 12", zipcode=12345)
>>> user = Users(name='John Appleseed', addr=user_address)
>>> user
Users(name='John Appleseed', addr=<example_app_udt.Address object at 0x10fe56070>)
>>> user.addr
<example_app_udt.Address object at 0x10fe56070>
>>> user.addr.street
'Easy Street, 12'
>>> user.addr.zipcode
12345
```

For a complete list of available methods refer to the
[cassandra.cqlengine.models documentation](https://docs.datastax.com/en/developer/python-driver/latest/api/cassandra/cqlengine/models/).

## Configuration Options
`CQLAlchemy` object provides following the options available for the
[cqlengine `connection.setup()`](https://docs.datastax.com/en/developer/python-driver/latest/api/cassandra/cqlengine/connection/):

* `CASSANDRA_HOSTS` — A `list` of hosts
* `CASSANDRA_KEYSPACE` — The default keyspace name to use
* `CASSANDRA_CONSISTENCY` — The global default `ConsistencyLevel`, default is the driver's
  [`Session.default_consistency_level`](https://docs.datastax.com/en/developer/python-driver/latest/api/cassandra/#cassandra.ConsistencyLevel)
* `CASSANDRA_LAZY_CONNECT` — `True` if should not connect until first use, default is `False`
* `CASSANDRA_RETRY_CONNECT` — `True` if we should retry to connect even if there was a connection failure initially,
  default is `False`
* `CASSANDRA_SETUP_KWARGS` — Pass-through keyword arguments for `Cluster()`

## API
`CQLAlchemy` object provides some helper methods for Cassandra database management:

* `sync_db()` — Creates/Syncs all the tables corresponding to the models declared in the application.
* `set_keyspace()` — Sets the keyspace for a session. Keyspaces once set will remain the default keyspace for the
  duration of the session. If the change is temporary, it must be reverted back to the default keyspace explicitly.

## Contributing
Found a bug? Need a feature? Open it in [issues](https://github.com/thegeorgeous/flask-cqlalchemy/issues), or even
better, open a [PR](https://github.com/thegeorgeous/flask-cqlalchemy/pulls). Please include tests in the PR.
