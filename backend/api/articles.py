from flask.views import MethodView, request
from models import *
from extensions import app
import json
from api.token import *


class ArticleApi(MethodView):
    def get(self, id):
        user = verify_token()
        if user is None:
            return 403
        datas = []
        if id is None:
           articles = Article.query.all()
        else: 
            pass
        for article in articles:
            datas.append({
                'id': article.id,
                'title': article.title,
                'content': article.content,
                'time': article.time,
                'username': article.username,
                'visits': article.visits,
            })
        return { 'articles': datas }, 200