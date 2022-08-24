"""
Class contains some datas
"""
from voluptuous import Schema, ALLOW_EXTRA

COUNT_OF_USERS = 12
NOT_FOUND = 404
CREATED = 201
BAD_REQUEST = 400

data_schema = Schema({
    'id': int,
    'email': str,
    'first_name': str,
    'last_name': str,
    'avatar': str
})

support_schema = Schema({
    'url': str,
    'text': str
})

user_schema = Schema(
    {
        "data": data_schema,
        "support": support_schema
    },
    extra=ALLOW_EXTRA,
    required=True
)


def user_data(name, job):
    """
    Generate user data
    """
    return {
        "name": name,
        "job": job
    }


def email_data(email):
    """
    Generate email
    """
    return {
        "email": email
    }
