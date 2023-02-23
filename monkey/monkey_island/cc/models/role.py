from __future__ import annotations

from flask_login import RoleMixin
from mongoengine import Document, StringField


class Role(Document, RoleMixin):
    name = StringField(max_length=80, unique=True)
    description = StringField(max_length=255)
    permissions = StringField(max_length=255)
