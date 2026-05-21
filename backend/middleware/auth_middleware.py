import os
import jwt
from functools import wraps
from flask import request, jsonify

JWT_SECRET = os.getenv('JWT_SECRET')

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']

            if auth_header.startswith("Bearer "):
                token = auth_header.split(" ")[1]

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
            current_user_id = data['user_id']
            current_user_role = data['role']

        except Exception as e:
            return jsonify({
                'message': 'Token is invalid!',
                'error': str(e)
            }), 401

        return f(current_user_id, current_user_role, *args, **kwargs)

    return decorated


def admin_required(f):
    @wraps(f)
    def decorated(current_user_id, current_user_role, *args, **kwargs):

        if current_user_role != 'admin':
            return jsonify({'message': 'Admin access required!'}), 403

        return f(current_user_id, current_user_role, *args, **kwargs)

    return decorated