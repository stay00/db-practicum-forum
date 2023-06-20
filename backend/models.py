import datetime

from extensions import db

Follows = db.Table('follow',
                   db.Column('follower', db.String(100), db.ForeignKey('user.username'), nullable=False),
                   db.Column('followed', db.String(100), db.ForeignKey('user.username'), nullable=False),
                   db.PrimaryKeyConstraint('follower', 'followed', name='pk_follows')
                   )
PostCollect = db.Table('post_collect',
                       db.Column('username', db.String(100), db.ForeignKey('user.username'), nullable=False),
                       db.Column('article_id', db.Integer, db.ForeignKey('article.id'), nullable=False),
                       db.PrimaryKeyConstraint('username', 'article_id', name='pk_post_collect')
                       )


class User(db.Model):
    # id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    level = db.Column(db.Integer, nullable=True, default=0)
    pic = db.Column(db.String(200))
    followed = db.relationship('User',
                               secondary=Follows,
                               primaryjoin=(Follows.c.follower == username),
                               secondaryjoin=(Follows.c.followed == username),
                               backref=db.backref('followers', lazy='dynamic'),
                               lazy='dynamic')
    post = db.relationship('Article',
                           backref='user')
    reply = db.relationship('Comment',
                            backref='user')
    collected = db.relationship('Article',
                                secondary=PostCollect,
                                backref='collector')

    @staticmethod
    def init_db():
        users = [
            User(username='ruoy', name='方若愚', password='123456', email='1687559852@qq.com', level=2),
            User(username='dogcatcher', name='郑海东', password='123456', email='1687559852@qq.com'),
            User(username='sb', name='杨俊杰', password='123456', email='1687559852@qq.com')
            # (1, 'ruoy', '方若愚', '123456', '12345678901'),
            # (2, 'dogcatcher', '郑海东', '123456', '12345678901'),
            # (3, 'sb', '杨俊杰', '123456', '12345678901'),
        ]
        for user in users:
            db.session.add(user)
        db.session.commit()


def init_relation():
    # follows = [
    #     Follows(uid1=1, uid2=2),
    #     Follows(uid1=1, uid2=3),
    # ]
    # for follow in follows:
    #     db.session.add(relation)
    user1 = User.query.get('ruoy')
    user2 = User.query.get('dogcatcher')
    user3 = User.query.get('sb')
    user1.followed.append(user2)
    user3.followers.append(user1)
    db.session.commit()


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(50), nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    username = db.Column(db.String(100), db.ForeignKey('user.username'), nullable=False)
    visits = db.Column(db.Integer, nullable=False)
    tag = db.Column(db.String(50), nullable=False)
    replies = db.relationship('Comment',
                              backref='article')

    @staticmethod
    def init_db():
        articles = [
            Article(id=1, title='ikun 们进', content='./1.md', time=datetime.datetime.now(), username='ruoy', visits=1, tag='1'),
            Article(id=2, title='溜 igs', content='./2.md', time=datetime.datetime.now(), username='dogcatcher', visits=20, tag='1'),
            Article(id=3, title='信安原理作业是什么', content='懵o.O', time=datetime.datetime.now(), username='sb', visits=10, tag='2-1')
        ]
        for article in articles:
            db.session.add(article)
        db.session.commit()


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(300), nullable=True)
    time = db.Column(db.DateTime, nullable=True)
    username = db.Column(db.String(100), db.ForeignKey('user.username'), nullable=False)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'), nullable=False)

    @staticmethod
    def init_db():
        comments = [
            Comment(id=1, content='hahaha', time=datetime.datetime.now(), username='sb', article_id=1),
            Comment(id=2, content='yes', time=datetime.datetime.now(), username='ruoy', article_id=2)
        ]
        for comment in comments:
            db.session.add(comment)
        db.session.commit()


