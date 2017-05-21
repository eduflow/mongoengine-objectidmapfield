from mongoengine import connect, Document
import pytest


DB_NAME = 'test_mongonengine_objectidmapfield'


@pytest.fixture(autouse=True)
def doctests_fixture(doctest_namespace):
    doctest_namespace['Document'] = Document


@pytest.fixture(scope='session', autouse=True)
def conn(request):
    conn = connect(DB_NAME)

    def teardown():
        conn.drop_database(DB_NAME)

    request.addfinalizer(teardown)
    return conn
