"""
Class for working with requests library
"""
import random
import pytest
from dotenv import load_dotenv
from faker import Faker
from pytest_voluptuous import S
from data.data import COUNT_OF_USERS, user_schema, NOT_FOUND, user_data, CREATED, email_data, BAD_REQUEST
from util.session_util import req_session

faker = Faker()


@pytest.fixture(scope='session', autouse=True)
def load_env():
    """
    Load .env
    """
    load_dotenv()


def test_positive_get_list_users():
    """
    Get list users positive test
    """
    response = req_session().get('/users', params='page=2')
    assert len(response.json()['data']) == 6, 'Count of users should be 6'


def test_positive_get_user():
    """
    Get user positive test
    """

    response = req_session().get(f'/users/{random.randint(1, COUNT_OF_USERS)}')
    assert S(user_schema) == response.json(), 'Response should be match scheme'


def test_negative_get_user():
    """
    Get user negative test
    """

    response = req_session().get(f'/users/{random.randint(COUNT_OF_USERS + 1, COUNT_OF_USERS * 2)}')
    assert response.status_code == NOT_FOUND, f'Status code should be {NOT_FOUND}'


def test_positive_create_user():
    """
    Create user positive test
    """

    name = faker.first_name()
    job = faker.job()
    data = user_data(name, job)

    response = req_session().post('/users', data=data)
    assert response.status_code == CREATED, f'Status code should be {CREATED}'
    assert response.json()['name'] == name, f'Name should be equal {name}'
    assert response.json()['job'] == job, f'Job should be equal {job}'


def test_negative_login():
    """
    Login user negative test
    """

    data = email_data(faker.email())

    response = req_session().post('/login', data=data)
    assert response.status_code == BAD_REQUEST, f'Status code should be {BAD_REQUEST}'
