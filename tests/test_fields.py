# -*- coding: utf-8 -*-

from bson import ObjectId
from mongoengine import Document, EmbeddedDocument
from mongoengine.errors import ValidationError
from mongoengine.fields import EmbeddedDocumentField, IntField, ReferenceField, StringField
import pytest

from mongoengine_objectidmapfield.fields import ObjectIdMapField


def test_objectidmapfield_objectid_required():
    '''Tests that `ObjectIdMapField` allows and requires `ObjectId` as keys.
    '''
    class User(Document):
        name = StringField()

    class Course(Document):
        user_times_visited = ObjectIdMapField(field=IntField())

    user = User(name='John').save()

    first_course = Course()
    first_course.user_times_visited = {
        str(user.id): 2,
    }
    # Saving with a string key -- should fail
    with pytest.raises(ValidationError):
        first_course.save()

    first_course.user_times_visited = {
        user.id: 2,
    }
    # Saving with a ObjectId key -- should pass
    first_course.save()

    first_course = Course()
    first_course.user_times_visited = {
        2: 2,
    }
    # Saving with a integer key -- should fail
    with pytest.raises(ValidationError):
        first_course.save()

    snd_course = Course()
    snd_course.user_times_visited[2] = 2
    # Saving with a integer key -- should fail
    with pytest.raises(ValidationError):
        snd_course.save()

    snd_course = Course()
    snd_course.user_times_visited[str(ObjectId())] = 2
    # Saving with a string key -- should fail
    with pytest.raises(ValidationError):
        snd_course.save()

    snd_course = Course()
    snd_course.user_times_visited[ObjectId()] = 2
    # Saving with a ObjectId key -- should pass
    snd_course.save()


def test_objectidmapfield_value_manipulation():
    '''Tests that values in a dictionary returned from `ObjectIdMapField`
    as expected.
    '''
    class User(Document):
        name = StringField()

    class Course(Document):
        user_times_visited = ObjectIdMapField(field=IntField())

    user = User(name='John').save()

    first_course = Course()
    first_course.user_times_visited = {
        user.id: 2,
    }
    first_course.save()
    first_course.reload()
    assert first_course.user_times_visited[user.id] == 2

    first_course.user_times_visited[user.id] += 1
    assert first_course.user_times_visited[user.id] == 3

    first_course.save()
    assert first_course.user_times_visited[user.id] == 3
    first_course.reload()
    assert first_course.user_times_visited[user.id] == 3

    first_course.user_times_visited[user.id] = 5
    assert first_course.user_times_visited[user.id] == 5
    first_course.save()
    assert first_course.user_times_visited[user.id] == 5
    first_course.reload()
    assert first_course.user_times_visited[user.id] == 5

    first_course.user_times_visited[user.id] = 1
    first_course.reload()
    assert first_course.user_times_visited[user.id] == 5


def test_objectidmapfield_reference_field():
    '''Tests that values in a `ObjectIdMapField`-dictionary can be
    `ReferenceField`s.
    '''
    class Person(Document):
        name = StringField()

    class Dog(Document):
        name = StringField()

    class DogHotel(Document):
        dog2owner = ObjectIdMapField(field=ReferenceField(Person))

    charlie = Person(name='Charlie Brown').save()
    snoopy = Dog(name='Snoopy').save()

    peanuts_doghotel = DogHotel()
    peanuts_doghotel.dog2owner = {
        snoopy.id: charlie,
    }
    peanuts_doghotel.save()
    peanuts_doghotel.reload()
    assert peanuts_doghotel.dog2owner[snoopy.id] == charlie


def test_objectidmapfield_embedded_document():
    '''Tests that values in a `ObjectIdMapField`-dictionary can be
    `EmbeddedDocument`s.
    '''
    class Person(Document):
        name = StringField()

    class Dog(EmbeddedDocument):
        name = StringField()

    class DogHotel(Document):
        current_customers = ObjectIdMapField(field=EmbeddedDocumentField(Dog))

    charlie = Person(name='Charlie Brown').save()

    peanuts_doghotel = DogHotel()
    peanuts_doghotel.dog2owner = {
        charlie.id: Dog(name='snoopy'),
    }
    peanuts_doghotel.save()
    peanuts_doghotel.reload()
    assert peanuts_doghotel.dog2owner[charlie.id] == Dog(name='snoopy')
