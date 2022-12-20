from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

article = Blueprint('article', __name__, url_prefix='/articles', static_folder='../static')
ARTICLES = {
    1: {'text': 'Bootstrap', "author": 1},
    2: {'text': 'Jinja', "author": 2},
    3: {'text': 'Django', "author": 3},
}


@article.route('/')
def article_list():
    return render_template('articles/list.html', articles=ARTICLES)


@article.route('/<int:pk>')
def get_article_pk(pk: int):
    article_pk = ARTICLES.get(pk)
    if article_pk:
        return render_template('articles/details.html', article_name=article_pk)
    raise NotFound()
