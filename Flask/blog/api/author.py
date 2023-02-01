from flask_combo_jsonapi import ResourceList, ResourceDetail

from Flask.blog.extensions import db
from Flask.blog.models import Author
from Flask.blog.schemas import AuthorSchema


class AuthorList(ResourceList):
    schema = AuthorSchema
    data_layer = {
        'session': db.session,
        'model': Author,
    }

a
class AuthorDetail(ResourceDetail):
    schema = AuthorSchema
    data_layer = {
        'session': db.session,
        'model': Author,
    }