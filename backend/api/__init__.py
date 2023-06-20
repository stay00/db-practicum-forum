from extensions import app
from api.auth import *
from api.articles import *


def register_api(view: MethodView, endpoint, url, pk, pk_type):
    view_func = view.as_view(endpoint)
    app.add_url_rule(url, defaults={pk: None},
                     view_func=view_func, methods=['GET'])
    app.add_url_rule(url, defaults={pk: None},
                     view_func=view_func, methods=['POST'])
    if pk_type == 'str':
        app.add_url_rule("%s/<%s>" % (url, pk),
                         view_func=view_func, methods=['GET', 'POST', 'DELETE'])
    else:
        app.add_url_rule("%s<%s:%s>" % (url, pk_type, pk),
                     view_func=view_func, methods=['GET', 'POST', 'DELETE'])


def register_all():
    register_api(UserApi, 'user_api', '/user/', 'username', 'str')
    register_api(ArticleApi, 'article_api', '/article/', 'id', 'int')

