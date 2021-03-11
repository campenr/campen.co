import sys
import os

from flask_script import Manager

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app import flask_app

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = flask_app

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
