"""
Flask-CQLAlchemy
----------------

Flask-CQLAlchemy handles connections to Cassandra clusters and provides a
Flask-SQLAlchemy like interface to declare models and their columns in a Flask
app.

Links
`````

* `Documentation <https://flask-cqlalchemy.readthedocs.org/>`_
"""
from setuptools import setup

setup(
    name='Flask-CQLAlchemy',
    version='2.0.0',
    url='http://thegeorgeous.com/flask-cqlalchemy',
    license='ISC',
    author='George Thomas',
    author_email='iamgeorgethomas@gmail.com',
    description='Flask-CQLAlchemy handles connections to Cassandra clusters and provides an interface through cqlengine',
    long_description=__doc__,
    keywords='cassandra cqlengine flask',
    packages=['flask_cqlalchemy'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'cassandra-driver>=3.22.0',
    ],
    options={"bdist_wheel": {"universal": True}},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Framework :: Flask',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
