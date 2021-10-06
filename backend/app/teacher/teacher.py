from flask import jsonify
from flask import request
from flask import make_response
from ..model import Teacher
from .. import db
from . import teacherbp


@teacherbp.route("/teacher/notice/<int:id>", methods=['DELETE'])
def teachersignup():
    count = 0
    email = request.get_json()["email"]
    teacherid = request.get_json()["teacherid"]
    password = request.get_json()["password"]

    t = Teacher(name + str(count),name + str(count), email, teacherid)
    t.set_password(password)
    count += 1
    db.add(t)
    db.commit()
    db.close()

    return t.to_dict()


@teacherbp.route("/login", methods=['POST'])
def teacherlogin():

    return make_response(jsonify(request.get_json, 200),200)