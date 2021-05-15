from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from accounts_service.database import db
from accounts_service.models.user import User

blueprint = Blueprint('users', __name__)


@blueprint.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.from_id(user_id)
    if user is None:
        abort(404)
    return user.to_dict()


@blueprint.route('/users', methods=['POST'])
def create_user():
    response = User.create(request.json)
    if response['status'] == 'error':
        return response, 400
    return response

@blueprint.route('/sessions', methods=['POST'])
def login_user():
    response = User.login(request.json.get('username'), request.json.get('password'))
    if response['status'] == 'error':
        return response, 400
    return response
