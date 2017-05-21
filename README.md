mongoengine-objectidmapfield
============================

`mongoengine-objectidmapfield` implements the MongoEngine `ObjectIdMapField` which
is the regular `MapField`, but instead of string as keys has `ObjectId`s as keys.

Installing
----------

Using pip:

    pip install 'git+git@github.com:peergradeio/mongoengine-objectidmapfield.git#egg=mongoengine-objectidmapfield'

Usage
-----
Import `ObjectIdMapField` from this package

    >>> from mongoengine_objectidmapfield import ObjectIdMapField

and then use as you would a normal MongoEngine `MapField`:

    >>> class Student(Document):
    ...     name = StringField()
    >>> class Yearbook(Document):
    ...     student_quote = ObjectIdMapField(field=StringField())
    >>> student = Student(name='lisa').save()
    >>> yearbook = Yearbook()
    >>> yearbook.student_quote[student.id] = 'Thank you everybody for a great time!'
    >>> yearbook.save()
    <Yearbook: Yearbook object>
    >>> yearbook.reload()
    <Yearbook: Yearbook object>
    >>> yearbook.student_quote[student.id]
    'Thank you everybody for a great time!'

Using strings as keys will raise a `ValidationError`:

    >>> student = Student(name='lisa').save()
    >>> yearbook = Yearbook()
    >>> yearbook.student_quote[str(student.id)] = 'Thank you everybody for a great time!'
    >>> yearbook.save()
    Traceback (most recent call last):
    ...
    ValidationError: ValidationError (Yearbook:None) (Invalid key in `ObjectIdMapField` - keys must be `ObjectId`s.: ['student_quote'])

Dependencies
------------
Tested with following versions:

* mongoengine 0.13.0

Tests
-----
To run the tests first install `pytest` (tested with version 3.0.6)

    pip install pytest

And then run the tests with

    py.test

Tests require a MongoDB database running on the standard port.

Authors
-------

### mongoengine-objectidmapfield package

* Malthe Jørgensen (@malthejorgensen <https://github.com/malthejorgensen>)

License
-------

BSD 3-clause
