from flask import Flask, render_template
from simpledu.config import configs
from simpledu.models import db, Course

def register_blueprints(app):
    from .handlers import front, course, admin, user
    app.register_blueprint(front)
    app.register_blueprint(course)
    app.register_blueprint(admin)
    app.register_blueprint(user)

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    db.init_app(app)
    register_blueprints(app)
    return app
"""Put below code into front.py and course.py and admin.py etc"""
#    @app.route('/')
#    def index():
#        courses = Course.query.all()
#        return render_template('index.html', courses=courses)

#    @app.route('/admin')
#    def admin_index():
#        return 'admin'
#    return app


