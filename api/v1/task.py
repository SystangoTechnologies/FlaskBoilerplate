'''
    Module for task CRUD APIs
'''
from __future__ import print_function
from __future__ import unicode_literals

from datetime import datetime

from flask import jsonify, abort, make_response
from flask_restplus import Namespace, Resource, reqparse

from api.v1.base import models

NS = Namespace('tasks')
model = models['tasks']

PARSER = reqparse.RequestParser()
PARSER.add_argument('title', required=True)
PARSER.add_argument('description', required=True)
PARSER.add_argument('status', required=True)


@NS.route('/')
class TaskResource(Resource):
    '''list and create task resource'''

    @NS.response(200, description='List all tasks')
    def get(self):
        '''list tasks API'''
        tasks = model.find()
        return jsonify({'data': list(tasks)})


    @NS.expect(PARSER)
    @NS.response(201, description='Task created successfully')
    def post(self):
        '''create task API'''
        data = PARSER.parse_args()
        task = model.create(data)
        if task is None:
            abort(400)
        return make_response(jsonify({'data': task}), 201)


@NS.route('/<string:task_id>/')
class TaskIDResource(Resource):
    '''get task detail resource'''

    @NS.response(200, description='Get task detail')
    def get(self, task_id):
        '''get task detail by id API'''
        task = model.find_by_id(task_id)
        if task is None:
            abort(404, "Task does not exist")
        return jsonify({'data': task})


    @NS.expect(PARSER)
    @NS.response(200, description='Task updated successfully')
    def put(self, task_id):
        '''update task detail by id API'''
        task = model.find_by_id(task_id)
        if task is None:
            abort(404, "Task does not exist")
        
        data = PARSER.parse_args()
        task = model.update_by_id(task['_id'], data)
        return jsonify({'data': 'Task updated successfully'})


    @NS.response(204, description='Task deleted successfully')
    def delete(self, task_id):
        '''delete task by id API'''
        task = model.find_by_id(task_id)
        if task is None:
            abort(404, "Task does not exist")
        else:
            task = model.remove_by_id(task['_id'])
            return make_response(jsonify({'data': 'Task deleted successfully'}), 204)
