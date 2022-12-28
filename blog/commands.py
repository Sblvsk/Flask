import click
from werkzeug.security import generate_password_hash

from Flask.blog.extensions import db


@click.command('init-db')
def init_db():
    # import models for creating tables
    #from Flask.wsgi import app

    # db.create_all(app=app)
    db.create_all()
    print("done!")


@click.command('create-init-user')
def create_init_user():
    from Flask.blog.models import User
    from wsgi import app

    with app.app_context():
        db.session.add(
            User(email='name@example.com', password=generate_password_hash('test123'))
        )
        db.session.commit()
        print("done! created users:")

