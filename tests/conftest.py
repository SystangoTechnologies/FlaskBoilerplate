'''
    Module for conftest file to initialize test app
'''
import pytest

from app import app, config_app


@pytest.fixture(scope='session')
def testapp(request):
    '''
        function to create test app
    '''
    client = app.test_client()
    app_context = app.app_context()
    app_context.push()

    def teardown():
        app_context.pop()

    request.addfinalizer(teardown)

    return client
