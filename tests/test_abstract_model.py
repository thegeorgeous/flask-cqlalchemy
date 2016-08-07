import unittest
from .test_cqlalchemy import BaseTestCase
from uuid import uuid1


def make_abstract_model(db):
    """Taken from
    https://datastax.github.io/python-driver/cqlengine/models.html#model-inheritance

    but where we want the base classes to be in separate tables
    """
    class Pet(db.Model):
        __abstract__ = True
        # __table_name__ = 'pet'
        owner_id = db.columns.UUID(primary_key=True)
        pet_id = db.columns.UUID(primary_key=True)
        pet_type = db.columns.Text(discriminator_column=True)
        name = db.columns.Text()

        def eat(self, food):
            pass

        def sleep(self, time):
            pass

    class Cat(Pet):
        # __discriminator_value__ = 'cat'
        cuteness = db.columns.Float()

        def tear_up_couch(self):
            pass

    class Dog(Pet):
        # __discriminator_value__ = 'dog'
        fierceness = db.columns.Float()

        def bark_all_night(self):
            pass

    return (Pet, Cat, Dog)


class AbstractModelTest(BaseTestCase):

    def test_sync_db(self):
        (Pet, Cat, Dog) = make_abstract_model(self.db)
        self.db.sync_db()
        mycat = Cat.create(owner_id=uuid1(),
                           pet_id=uuid1(),
                           name="Tiddles",
                           cuteness=9001)
        self.assertTrue(isinstance(mycat, Cat))
        self.assertEqual(mycat.cuteness, 9001)

if __name__ == '__main__':
    unittest.main()
