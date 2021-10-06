from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from .model import db 
from .model import User
from .. import marshmallow


class Teacher(User, db.Model):

    surname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    uid = db.Column(db.String, nullable=False)

    extras = db.relationship('Extra')

    def __init__(self, name, surname, email, uid):

        User.__init__(self, name)

        self.email = email
        self.surname = surname
        self.uid = uid
    
    def set_password(self, password):

        self.password = generate_password_hash(password, "sha256", 32)
    
    def check_password(self, password):

        return check_password_hash(self.password, password)

