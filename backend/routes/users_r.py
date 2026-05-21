from flask import Blueprint, request, jsonify
from services.users_s import create_user, login_user, get_all_users
from middleware.auth_middleware import token_required, admin_required

users_bp = Blueprint("users", __name__)

@users_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    result = login_user(data)

    if not result:
        return jsonify({"message": "Credenciales incorrectas"}), 401

    return jsonify(result), 200

@users_bp.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    user = create_user(data)

    if not user:
        return jsonify({"message": "El usuario ya existe"}), 400

    return jsonify({
        "message": "Usuario creado correctamente",
        "user": user
    }), 201

@users_bp.route("/users", methods=["GET"])
def list_users():
    users = get_all_users()
    return jsonify(users), 200