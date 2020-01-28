from datetime import datetime


def init_tasks(models):
    task_model = models['tasks']

    # clean the storage
    task_model.collection.remove()

    # insert initial data
    init_tasks = [
        {
            'title': u'Buy groceries',
            'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
            'status': u'Done',
            'created_at': datetime.now(),
            'updated_at': datetime.now()
        },
        {
            'title': u'Learn Python',
            'description': u'Need to find a good Python tutorial on the web',
            'status': u'Done',
            'created_at': datetime.now(),
            'updated_at': datetime.now()
        }
    ]
    task_model.collection.insert_many(init_tasks)
    print('finish init tasks')
