#main file that contains the Flask API.
from app import create_app
from app import db
from app.routes import app
from app.models import Job

if __name__ == '__main__':
    app = create_app('development')  # You can specify the configuration name here
    app.debug=True
    app.run()
