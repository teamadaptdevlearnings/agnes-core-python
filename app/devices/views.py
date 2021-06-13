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
        device_data['description'] = device.description
        device_data['date_created'] = device.date_created
        device_list.append(device_data)
    return jsonify({'devices': device_list}), 200

@devices_page.route('/devices/<id>', methods=['GET'])
def get_device(id):
    device = Devices.query.filter_by(id=id).first()
    if not device:
        return jsonify({'response': 'Device not found'}), 404

    device_data = dict()
    device_data['id'] = device.id
    device_data['name'] = device.name
    device_data['description'] = device.description
    device_data['date_created'] = device.date_created
    return jsonify({'device': device_data}), 200


@devices_page.route('/devices/<id>', methods=['PUT'])
def update_device(id):
    data = request.get_json()
    device = Devices.query.filter_by(id=id).first()

    if not device:
        return jsonify({'response': 'Device not found!'}), 404

    device.name = data.get('name')
    device.email = data.get('description')
    db.session.commit()
    return jsonify({'response': f'Device {device.name} has been updated!'}), 200


@devices.route('/devices/<id>', methods=['DELETE'])
def delete_device(id):
    device = Devices.query.filter_by(id=id).first()
    if not device:
        return jsonify({'response': 'Device not found!'}), 404

    device_name = device.name
    db.session.delete(device)
    db.session.commit()
    return jsonify({'message': f'Device {device_name} has been deleted!'}), 200
