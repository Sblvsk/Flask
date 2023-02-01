from flask_combo_jsonapi import ResourceList, ResourceDetail

from Flask.blog.extensions import db
from Flask.blog.models import Tag
from Flask.blog.schemas import TagSchema


class TagList(ResourceList):
    schema = TagSchema
    data_layer = {
        'session': db.session,
        'model': Tag,
    }


class TagDetail(ResourceDetail):
    schema = TagSchema
    data_layer = {
        'session': db.session,
        'model': Tag,
    }