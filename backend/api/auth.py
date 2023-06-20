from flask.views import MethodView, request
from models import *
from extensions import app
import json
from api.token import *

class UserApi(MethodView):
    def post(self, username):
        if username is None:
            form = json.loads(request.data)
            entry = form['entry']
            password = form['password']
            user = User.query.get(entry)
            if user is None or user.password != password:
                return {
                           'code': 0
                       }, 401
            else:
                token = create_token(user)
                return {
                           'token': token,
                           'level': user.level
                       }, 200
        else:
            form = json.loads(request.data)
            if User.query.get(username) is not None:
                return {}, 400
            else:
                name = form['name']
                password = form['password']
                email = form['email']
                user = User(username=username, name=name, password=password, email=email)
                db.session.add(user)
                db.session.commit()
                return {}, 200
        

    def get(self, username):
        user = verify_token()
        if user is None:
            return 403
        elif user['level'] == 0:
            return 401
        datas = []
        if username is None:
            users = User.query.all()
        else:
            users = User.query.filter(User.username.like('%{key}%'.format(key=username)))
        for user in users:
            datas.append({
                'username': user.username,
                'email': user.email,
                'level': user.level
            })
        return {
                   'users': datas,
               }, 200

        def delete(self, username):
            user = verify_token()
            u = User.query.get(username)
            if u is None:
                return 204
            elif user is None:
                return 403
            elif user['level'] < u.level:
                return 403
            else:
                db.session.delete(u)
                db.session.commit()
                return 200
