from flask import Blueprint, request, jsonify
from middleware.auth_middleware import token_required
from services.appointments_s import(
    get_all_appointments,
    create_appointment,
    delete_appointment
)

appointments_bp = Blueprint('appointments', __name__)

@appointments_bp.route("/appointments", methods=["GET"])
@token_required
def get_appointments(current_user_id, current_user_role):
    appointments = get_all_appointments()
    return jsonify(appointments), 200

@appointments_bp.route("/appointments", methods=["POST"])
@token_required
def add_appointment(current_user_id, current_user_role):
    data = request.get_json()
    appointment = create_appointment(data, current_user_id)

    return jsonify({
        "message": "Cita creada correctamente",
        "appointment": appointment
    }), 201

@appointments_bp.route("/appointments/<appointment_id>", methods=["DELETE"])
@token_required
def remove_appointment(current_user_id, current_user_role, appointment_id):
    deleted = delete_appointment(appointment_id)

    if deleted:
        return jsonify({
            "message": "Cita eliminada correctamente",
            "appointment_id": appointment_id
        }), 200

    return jsonify({"message": "Cita no encontrada"}), 404
    

    