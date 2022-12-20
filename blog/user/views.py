from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')
USERS = {
    1: "James",
    2: "Brian",
    3: "Peter",
}


@user.route('/')
def user_list():
    return render_template('users/list.html', users=USERS)


@user.route('/<int:pk>')
def get_user_pk(pk: int):
    user_pk = USERS.get(pk)
    if user_pk:
        return render_template('users/details.html', user_name=user_pk)
    raise NotFound()

@user.route('/name/<int:pk>')
def get_user_name(pk: int):
    user_pk = USERS.get(pk)
    if user_pk:
        return user_pk
    raise NotFound()
