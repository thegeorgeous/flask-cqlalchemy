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
