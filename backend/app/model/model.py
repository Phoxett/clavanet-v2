from datetime import datetime as dt
from sqlalchemy import  Column
from sqlalchemy import  String
from sqlalchemy import  Integer
from sqlalchemy import  DateTime


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


class User(DictMixin):

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __init__(self, name):
        self.created_at = dt.now()
        self.updated_at = dt.now()
        self.name = name


class JSONMixin:

    @staticmethod
    def to_json(stable, table_query, many=False):

        schema = stable(many=many)
        json = schema.dump(table_query)
        return json

