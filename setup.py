"""
Flask-CQLAlchemy
----------------

Flask-CQLAlchemy handles connections to Cassandra clusters
and gives a unified easier way to declare models and their
columns

Links
`````

* `documentation <http://flask-cqlalchemy.readthedocs.org>`_


"""

from setuptools import setup

setup(
    name='Flask-CQLAlchemy',
    version='0.2.0',
    url='http://thegeorgeous.com/flask-cqlalchemy',
    license='BSD',
    author='George',
    author_email='iamgeorgethomas@gmail.com',
    description='Flask-CQLAlchemy handles connections to Cassandra clusters through the cqlengine',
    long_description=__doc__,
    keywords='cassandra cqlengine flask',
    packages=['flask_cqlalchemy'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'cassandra-driver>=2.5',
        'blist'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Framework :: Flask',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]

)
