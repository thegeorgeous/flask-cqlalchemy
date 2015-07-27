.. Flask-CQLAlchemy documentation master file, created by
   sphinx-quickstart on Fri Jun 12 13:22:44 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Flask-CQLAlchemy
================

.. toctree::
   :maxdepth: 2


Flask-CQLAlchemy handles connections to Cassandra clusters
and gives a unified easier way to declare models and their
columns

Installation
------------
.. code-block:: guess

   $ pip install flask-cqlalchemy


Example
-------
.. code-block:: python

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


Usage
-----
Start a python shell

.. code-block:: guess

   >>from example_app import db, User
   >>db.sync_db()
   >>user1 = User(username='John Doe')
   >>user1.save()

For a complete list of available method refer to the cqlengine `Model documentation <http://datastax.github.io/python-driver/api/cassandra/cqlengine/models.html>`_

Configuration Options
---------------------
CQLAlchemy provides all the option available in the cqlengine connection.setup() method

* CASSANDRA_HOSTS - A list of hosts
* CASSANDRA_KEYSPACE - The default keyspace to use
* CASSANDRA_CONSISTENCY - The global default ConsistencyLevel
* CASSANDRA_LAZY_CONNECT - True if should not connect until first use
* CASSANDRA_RETRY_CONNECT - True if we should retry to connect even if there was
  a connection failure initially
* CASSANDRA_SETUP_KWARGS - Pass-through keyword arguments for Cluster()

API
---
CQLAlchemy provides some helper methods for Cassandra database management

**sync_db()** - Creates/Syncs all the tables corresponding to the models declared in the application

**set_keyspace()** - Sets the keyspace for a session. Keyspaces once set will remain the default keyspace for the duration of the session. If the change is temporary, it must be reverted back to the default keyspace explicitly.
