from sqlalchemy import Integer
from sqlalchemy import SmallInteger
from sqlalchemy import DateTime
from sqlalchemy import Column
from sqlalchemy import String
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from ..database import Base
from .model import User


class Teacher(User, Base):

    __tablename__ = "teacher"

    surname = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    uid = Column(Integer, nullable=False)



    def __init__(self, name, email, uid):

        User.__init__(self, name)

        self.email = email
        self.uid = uid
        
    
    def set_password(self, password):

        self.password = generate_password_hash(password, "sha256", 32)
    
    def check_password(self, password):

        return check_password_hash(self.password, password)



