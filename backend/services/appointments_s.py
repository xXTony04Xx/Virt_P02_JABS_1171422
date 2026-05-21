from bson import ObjectId
from config.DataBase import appointments_collection

def serialize_appointment(appointment):
    appointment['_id'] = str(appointment['_id'])
    appointment["user_id"] = str(appointment["user_id"])
    return appointment

def get_all_appointments():
    appointments = appointments_collection.find() 
    return [serialize_appointment(appointment) for appointment in appointments]

def create_appointment(data, user_id):
    appointment = {
        'user_id': ObjectId(user_id),
        'clienteName': data.get('clienteName'),
        'manicuristsName': data.get('manicuristsName'),
        'service': data.get('service'),
        'date': data.get('date'),
        'time': data.get('time'),
        'status': data.get('status')
    }
    result = appointments_collection.insert_one(appointment)
    appointment['_id'] = str(result.inserted_id)
    appointment["user_id"] = str(appointment["user_id"])

    return appointment

def delete_appointment(appointment_id):
    result = appointments_collection.delete_one({'_id': ObjectId(appointment_id)})
    return result.deleted_count > 0
