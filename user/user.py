# -*- coding: utf-8 -*-
import datetime

from ..base import *


class PasswordUserMixin(object):

    password = Column(db.String(128), nullable=True)

    def set_password(self, password, bcrypt, commit=True):
        self.password = bcrypt.generate_password_hash(password)
        if commit:
            self.save()

    def check_password(self, value, bcrypt):
        return bcrypt.check_password_hash(self.password, value)


class User(PasswordUserMixin, SurrogatePK, Model):

    __tablename__ = 'user'

    uid = Column(db.String(64), nullable=False)

    status = Column(db.Integer, nullable=False, default=0)

    mobile = Column(db.String(32), index=True, nullable=True)
    age = Column(db.Integer, nullable=True)
    gender = Column(db.Integer, nullable=True, default=0)
    name = Column(db.String(32), nullable=True)
    nick_name = Column(db.String(32), nullable=True)
    city = Column(db.String(32), nullable=True)
    address = Column(db.String(255), nullable=True)

    registered_at = Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    created_at = Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    memo = Column(db.String(255), nullable=True)


class UserAuth(SurrogatePK, Model):

    __tablename__ = 'user_auth'

    user_id = reference_col('user', nullable=False, index=True)
    uid = Column(db.String(64), nullable=False)

    status = Column(db.Integer, nullable=False, default=0)

    # Auth登录id
    access_id = Column(db.String(64), unique=True, index=True, nullable=False)
    # Auth登录token
    access_token = Column(db.String(512), nullable=True)
    # Auth登录平台, wechat, weibo, etc...
    access_platform = Column(db.String(16), nullable=True)
    # Auth登录类型
    access_type = Column(db.String(16), index=True, nullable=False, default='OAuth2')
    # Auth登录过期时间
    access_expires = Column(db.DateTime, nullable=True)

    login_count = Column(db.Integer, nullable=False, default=0)

    last_login_at = Column(db.DateTime, nullable=True)
    first_login_at = Column(db.DateTime, nullable=False, default=datetime.datetime.now)

    user = relationship('User', backref=backref('auth_list'))
