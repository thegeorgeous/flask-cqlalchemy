import unittest
import uuid
from flask import Flask
from flask.ext.cqlalchemy import CQLAlchemy
from cassandra.cqlengine.management import drop_keyspace, create_keyspace_simple
from cassandra.cqlengine import models
from cassandra.cqlengine.usertype import UserType


def make_user_model(db):
    class User(db.Model):
        uuid = db.columns.UUID(primary_key=True, default=uuid.uuid4)
        username = db.columns.Text(index=True, required=False)

    return User

def make_user_defined_model(db):
    class address(db.UserType):
        street = db.columns.Text()
        zipcode = db.columns.Integer()

    class users(db.Model):
        __keyspace__ = 'test1'
        name = db.columns.Text(primary_key=True)
        addr = db.columns.UserDefinedType(address)

    return (users, address)

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        app.config['CASSANDRA_HOSTS'] = ['127.0.0.1']
        app.config['CASSANDRA_KEYSPACE'] = "test1"
        app.config['CASSANDRA_SETUP_KWARGS'] = {'protocol_version': 3}
        db = CQLAlchemy(app)
        self.User = make_user_model(db)
        create_keyspace_simple("test1", 1)

        self.app = app
        self.db = db

    def tearDown(self):
        drop_keyspace("test1")


class BasicTestCase(BaseTestCase):

    def test_sync_db(self):
        self.db.sync_db()
        user = self.User.create(username="JohnDoe")
        self.assertTrue(isinstance(user, self.User))
        self.assertEqual(user.username, "JohnDoe")

    def test_set_keyspace(self):
        create_keyspace_simple("test2", 1)
        self.db.set_keyspace('test2')
        self.assertEqual(models.DEFAULT_KEYSPACE, "test2")
        self.assertEqual(self.db._keyspace_, "test2")

    def test_set_keyspace_no_args(self):
        create_keyspace_simple("test2", 1)
        self.db.set_keyspace('test2')
        self.db.set_keyspace()
        self.assertEqual(models.DEFAULT_KEYSPACE,
                         self.app.config['CASSANDRA_KEYSPACE'])
        self.assertEqual(self.db._keyspace_,
                         self.app.config['CASSANDRA_KEYSPACE'])


class UserDefinedTypeTestCase(BaseTestCase):
    def test_udt(self):
        (users, address) = make_user_defined_model(self.db)
        self.db.sync_db()
        user_address = address(street="Easy St.", zipcode=99999)
        users.create(name="Joe", addr=user_address)
        user = users.objects(name="Joe")[0]
        self.assertEqual(user.name, "Joe")
        self.assertEqual(user.addr, user_address)

if __name__ == '__main__':
    unittest.main()
