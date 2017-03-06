"""
Flask-CQLAlchemy
----------------

Flask-CQLAlchemy handles connections to Cassandra clusters and provides a
Flask-SQLAlchemy like interface to declare models and their columns in a Flask
app
Links
`````

* `documentation <http://flask-cqlalchemy.readthedocs.org>`_


"""

from setuptools import setup

setup(
    name='Flask-CQLAlchemy',
    version='1.3.0',
    url='http://thegeorgeous.com/flask-cqlalchemy',
    license='BSD',
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
        'cassandra-driver>=2.6',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Framework :: Flask',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]

)
