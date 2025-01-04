from flask import request, jsonify, send_file, abort
from config import app, db
import os
from flask import jsonify
import json

from ia import ask_question
from models import User, Level


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
        major=major,
        level=1
    )
    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "user": new_user.to_json(),
        "pass": True
    }), 201

@app.route("/login", methods=["POST"])
def login():
    data = request.json

    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if not user:
        return jsonify({"valid": False, "error": "Username does not exist"}), 400

    if user.password != password:
        return jsonify({"valid": False, "error": "Invalid password"}), 400

    return jsonify({
        "valid": True,
        "user": user.to_json()
    }), 200

@app.route('/level/<int:level_id>', methods=['GET'])
def get_level(level_id):
    level = Level.query.get(level_id)
    if not level:
        abort(404, description="Level not found")
    return jsonify(level.to_json())

@app.route('/user/level/<int:user_id>', methods=['GET'])
def get_user_level(user_id):
    user = User.query.get(user_id)
    if not user:
        abort(404, description="User not found")
    return jsonify({
        'level': user.level
    })

@app.route('/user/<int:user_id>/increment-level', methods=['POST'])
def increment_user_level(user_id):
    user = User.query.get(user_id)
    if not user:
        abort(404, description="User not found")
    user.level += 1
    db.session.commit()
    return jsonify({
        'message': f"User {user_id}'s level has been incremented.",
        'new_level': user.level
    })

@app.route("/submit_level", methods=["POST"])
def submit_level():
    data = request.json

    level_id = int(data.get('level_id'))
    user_answer = data.get('answer')

    level = Level.query.get(level_id)
    if not level:
        abort(404, description="Level not found")

    send = ask_question(level.problem, user_answer)

    return jsonify(send), 200

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
