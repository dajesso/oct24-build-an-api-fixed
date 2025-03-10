from flask import Flask
from init import db, ma
import os
from blueprints.db_bp import db_bp
from blueprints.students_bp import students_bp
from blueprints.teachers_bp import teachers_bp
from blueprints.courses_bp import courses_bp
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)
    load_dotenv(override=True)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URI')

    db.init_app(app)
    ma.init_app(app)

    app.register_blueprint(db_bp)
    app.register_blueprint(students_bp)
    app.register_blueprint(teachers_bp)
    app.register_blueprint(courses_bp)

    return app


