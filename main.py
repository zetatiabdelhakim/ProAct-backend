from flask import request, jsonify, send_file
from config import app, db
import os
from flask import jsonify
import json

from models import User


@app.route("/register", methods=["POST"])
def register():
    data = request.json

    name = data.get('name')
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    gender = data.get('gender')
    major = data.get('major')

    existing_user_by_email = User.query.filter_by(email=email).first()
    existing_user_by_username = User.query.filter_by(username=username).first()

    if existing_user_by_email:
        return jsonify({"pass" : False, "error": "Email already exists"}), 400

    if existing_user_by_username:
        return jsonify({"pass" : False, "error": "Username already exists"}), 400

    new_user = User(
        name=name,
        username=username,
        email=email,
        password=password,
        gender=gender,
        major=major
    )
    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "user": new_user.to_json(),
        "pass": True
    }), 201



if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)