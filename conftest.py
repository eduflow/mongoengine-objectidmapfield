
from mongoengine import connect, Document, StringField
import pytest

from mongoengine_objectidmapfield.fields import ObjectIdMapField

DB_NAME = 'test_mongonengine_objectidmapfield'


collect_ignore = ['setup.py']


@pytest.fixture(autouse=True)
def doctests_fixture(request, doctest_namespace):
    doctest_namespace['Document'] = Document
    doctest_namespace['StringField'] = StringField
    doctest_namespace['ObjectIdMapField'] = ObjectIdMapField

    conn = connect(DB_NAME)

    def teardown():
        conn.drop_database(DB_NAME)

    request.addfinalizer(teardown)
    return conn


@pytest.fixture(scope='session')
def conn(request):
    conn = connect(DB_NAME)

    def teardown():
        conn.drop_database(DB_NAME)

    request.addfinalizer(teardown)
    return conn
