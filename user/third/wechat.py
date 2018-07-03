# -*- coding: utf-8 -*-
import datetime

from base import *


class WechatUser(SurrogatePK, Model):

    __tablename__ = 'user_wechat'

    # 关联user表
    user_id = reference_col('user', nullable=False, index=True)
    uid = Column(db.String(64), nullable=False)

    # wechat账户体系
    mp_id = Column(db.String(128), nullable=False, index=True)  # 公众号id
    open_id = Column(db.String(128), nullable=False, index=True)
    union_id = Column(db.String(128), nullable=True)

    subscribe = Column(db.Boolean, nullable=False, default=False)  # 是否关注公众号
    bound = Column(db.Boolean, nullable=False, default=False)  # 是否已经与手机号绑定

    # copy from wechat user system
    city = Column(db.String(128), nullable=True)
    head_img_url = Column(db.String(512), nullable=True)
    nickname = Column(db.String(128), nullable=True)

    created_at = Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = Column(db.DateTime, nullable=False, default=datetime.datetime.now)

    active = Column(db.Boolean(), default=True)

    user = relationship('User', backref=backref('wechat_users'))
