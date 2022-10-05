from flask import Blueprint, render_template

from __init__ import create_app

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/')
def index():
    return render_template('index.html')


create_app().run(debug=True, port=9876)
