# Copyright 2017 Richard Campen
# All rights reserved
# This software is released under the Modified BSD license
# See LICENSE.txt for the full license documentation

from flask import Flask
from celery import Celery
from flask_sqlalchemy import SQLAlchemy
import os

from config import config

flask_app = Flask(__name__)

# load correct config settings based on environment variable, or default to 'development' environment
environment = os.environ.get('ENVIRONMENT')
if environment is None:
    print('-Loading configuration: No environment specified, defaulting to development environment')
    environment = 'development'
else:
    print('-Loading configuration: ', environment)
flask_app.config.from_object(config[environment])

# enable wekzeug debug traceback when running behind uWSGI
if environment == 'development':
    from werkzeug.debug import DebuggedApplication
    flask_app.wsgi_app = DebuggedApplication(flask_app.wsgi_app, True)

# db setup
db = SQLAlchemy(flask_app)

print('-Configuring celery')
def make_celery(app):
    celery_ = Celery(app.import_name, backend=app.config['CELERY_RESULT_BACKEND'],
                     broker=app.config['CELERY_BROKER_URL'])
    celery_.conf.update(app.config)
    TaskBase = celery_.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery_.Task = ContextTask

    return celery_

celery_app = make_celery(flask_app)

print('-Importing views, models, and tasks')
from app import views, models, tasks

print('-Configuring trackers')
from app import trackers
flask_app.software_trackers = {
    'pypi': trackers.PYPITracker
}

print('-Init complete')
