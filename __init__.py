from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dsfhx1634'

    from main import main_blueprint
    app.register_blueprint(main_blueprint)

    from comments import comments_blueprint
    app.register_blueprint(comments_blueprint)

    return app
