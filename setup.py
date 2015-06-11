"""
Flask-CQLAlchemy
---------------

Flask-CQLAlchemy handles connections to Cassandra clusters
and gives a unified easier way to declare models and their
columns
"""

from setuptools import setup

setup(
    name='Flask-CQLAlchemy',
    version='0.1',
    url='http://thegeorgeous.github.io/Flask-CQLAlchemy',
    license='BSD',
    author='George',
    author_email='iamgeorgethomas@gmail.com',
    description='Flask-CQLAlchemy handles connections to Cassandra clusters through the cqlengine',
    long_description=__doc__,
    packages=['flask_cqlalchemy'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask>=0.10',
        'cassandra-driver>=2.5',
        'blist'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
