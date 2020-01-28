'''
    Module to test all APIs related to task
'''
import pytest


class MockRequest():
    '''Dummy class to mock request'''
    @staticmethod
    def find():
        return 'string data'

    @staticmethod
    def create(obj):
        return obj

    @staticmethod
    def find_by_id(task_id):
        data = {
            '_id': task_id
        }
        return data

    @staticmethod
    def update_by_id(task_id, data):
        data = {
            '_id': task_id,
            'data': data
        }
        return data

    @staticmethod
    def remove_by_id(task_id):
        return task_id


class MockGetRequest():
    '''Dummy class to mock get request'''
    @staticmethod
    def find_by_id(task_id):
        return None


@pytest.mark.usefixtures("testapp")
class TestTakss:
    '''class to test all tasks APIs'''

    def test_list_task(self, testapp, monkeypatch):
        '''test list tasks API'''
        monkeypatch.setattr('api.v1.task.model', MockRequest)

        # test list tasks
        response = testapp.get('/api/v1/tasks/') 
        assert response.status_code == 200


    def test_create_task(self, testapp, monkeypatch):
        '''test create task API'''
        monkeypatch.setattr('api.v1.task.model', MockRequest)

        # test task create API with valid data
        data = {
            "title": "Test",
            "description": "test 1234",
            "status": 'to do'
        }
        response = testapp.post('/api/v1/tasks/', data=data)
        assert response.status_code == 201

        # test task create API without data
        response = testapp.post('/api/v1/tasks/')
        assert response.status_code == 400


    def test_get_task(self, testapp, monkeypatch):
        '''test get task detail API'''
        monkeypatch.setattr('api.v1.task.model', MockRequest)

        # test task detail API with valid task id
        response = testapp.get('/api/v1/tasks/123456/')
        assert response.status_code == 200


    def test_delete_task(self, testapp, monkeypatch):
        '''test delete task detail API'''
        monkeypatch.setattr('api.v1.task.model', MockRequest)

        # test delete task API with valid task id
        response = testapp.delete('/api/v1/tasks/123456/')
        assert response.status_code == 204


    def test_update_task(self, testapp, monkeypatch):
        '''test update task detail API'''
        monkeypatch.setattr('api.v1.task.model', MockRequest)

        # test update task API
        data = {
            "title": "Test",
            "description": "test 1234",
            "status": 'to do'
        }
        response = testapp.put('/api/v1/tasks/123456/', data=data)
        assert response.status_code == 200


    def test_task_with_invalid_id(self, testapp, monkeypatch):
        '''test task with invalid id APIs'''
        monkeypatch.setattr('api.v1.task.model', MockGetRequest)

        # test delete task API with invalid task id
        response = testapp.delete('/api/v1/tasks/12345/')
        assert response.status_code == 404

        # test task detail API with invalid task id
        response = testapp.get('/api/v1/tasks/12345/')
        assert response.status_code == 404

        # test update task API with invalid task id
        data = {
            "title": "Test",
            "description": "test 1234",
            "status": 'to do'
        }
        response = testapp.put('/api/v1/tasks/12345/', data=data)
        assert response.status_code == 404
