from datetime import datetime as dt
from .. import db


class User:

    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self, name):
        self.created_at = dt.now()
        self.updated_at = dt.now()
        self.name = name


class Extra(db.Model):

    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String, nullable=False)
    value = db.Column(db.String, nullable=False)
    teacheruid = db.Column(db.String, db.ForeignKey('teacher.uid'), nullable=True)
    studentuid = db.Column(db.String, db.ForeignKey('student.uid'), nullable=True)
    schooluid = db.Column(db.String, db.ForeignKey('school.uid'), nullable=True)

class DictMixin:
    def to_dict(self):
        return \
            {
            column.name: getattr(self, column.name)
            if not isinstance(
                getattr(self, column.name), (dt, dt.date)
            )
            else getattr(self, column.name).isoformat()
            for column in self.__table__.columns
            }
