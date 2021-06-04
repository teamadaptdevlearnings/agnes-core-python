from flask import Blueprint, Response, request, jsonify
from config.database import db
from .models import Devices

devices_page = Blueprint('devices', __name__)

@devices_page.route("/devices", methods=['POST'])
def add_device():
    data = request.get_json()
    device = Devices(
        name=data.get('name'),
        description=data.get('description'),
        password=data.get('password')
    )
    db.session.add(device)
    db.session.commit()
    return jsonify({'response': f"{data.get('name')} added successfully!"}), 201

@devices_page.route('/devices', methods=['GET'])
def get_devices():
    devices = Devices.query.all()
    device_list = []
    for device in devices:
        device_data = dict()
        device_data['id'] = device.id
        device_data['name'] = device.name
        drvice_data['description'] = device.description
        device_data['date_created'] = user.date_created
        device_list.append(device_data)
    return jsonify({'devices': device_list}), 200
