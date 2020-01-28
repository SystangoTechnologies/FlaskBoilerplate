'''
    file is used to initialize the flask app
'''
from __future__ import print_function
from __future__ import unicode_literals

import os
from flask import Flask, jsonify, make_response, redirect

from api.conf import configure_app
from api.v1 import api_blueprint

# flask app
app = Flask(__name__)
app.config['SWAGGER_BASEPATH'] = '/api/v1/'

def create_app():
    '''Function to initialize flask app'''
    config_app = configure_app(app)

    @app.errorhandler(404)
    def not_found(error="Not Found"):
        '''Function to handle 404 error'''
        print(error)
        return make_response(jsonify({'error': error}), 404)

    @app.route('/')
    def base_index():
        '''function to handle the default path'''
        return redirect('/api/v1/')

    app.register_blueprint(api_blueprint)

    return app, config_app


app, config_app = create_app()

if __name__ == '__main__':
    HOST = os.environ.get('HOST', '0.0.0.0')
    PORT = os.environ.get('PORT', '5000')
    DEBUG = os.environ.get('DEBUG', False)

    app.run(debug=DEBUG, host=HOST, port=PORT, threaded=True)
