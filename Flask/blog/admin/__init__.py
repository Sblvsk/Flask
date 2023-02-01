def register_views():
    from Flask.blog import models
    from Flask.blog.admin.views import TagAdminView, ArticleAdminView, UserAdminView
    from Flask.blog.extensions import admin, db

    admin.add_view(ArticleAdminView(models.Article, db.session, category='Models'))
    admin.add_view(TagAdminView(models.Tag, db.session, category='Models'))
    admin.add_view(UserAdminView(models.User, db.session, category='Models'))