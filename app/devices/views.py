from flask import Blueprint, Response, request, jsonify
from config.database import db
from .models import Devices, Pins

devices_bp = Blueprint('devices', __name__)
pins_bp = Blueprint('pins', __name__)


""" Device endpoints """


@devices_bp.route("/devices", methods=['POST'])
def add_device():
    data = request.get_json()
    device = Devices(
        name=data.get('name'),
        description=data.get('description')
    )
    db.session.add(device)
    db.session.commit()
    return jsonify({'response': f"{data.get('name')} added successfully!"}), 201


@devices_bp.route('/devices', methods=['GET'])
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


@devices_bp.route('/devices/<id>', methods=['GET'])
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


@devices_bp.route('/devices/<id>', methods=['PUT'])
def update_device(id):
    data = request.get_json()
    device = Devices.query.filter_by(id=id).first()

    if not device:
        return jsonify({'response': 'Device not found!'}), 404

    device.name = data.get('name')
    device.email = data.get('description')
    db.session.commit()
    return jsonify({'response': f'Device {device.name} has been updated!'}), 200


""" Pin endpoints """


@pins_bp.route("/pins", methods=['POST'])
def add_pin():
    data = request.get_json()
    pin = Pins(
        name=data.get('name'),
        number=data.get('number'),
        assignment=data.get('assignment'),
        device_id=data.get('device_id')
    )
    db.session.add(pin)
    db.session.commit()
    return jsonify({'response': f"{data.get('name')} added successfully!"}), 201


@pins_bp.route('/pins', methods=['GET'])
def get_pins():
    pins = Pins.query.all()
    pin_list = []
    for pin in pins:
        pin_data = dict()
        pin_data['id'] = pin.id
        pin_data['name'] = pin.name
        pin_data['number'] = pin.number
        pin_data['assignment'] = pin.assignment
        pin_data['date_created'] = pin.date_created
        pin_data['device_id'] = pin.device_id
        pin_list.append(pin_data)
    return jsonify({'pins': pin_list}), 200


@pins_bp.route('/pins/<id>', methods=['GET'])
def get_pin(id):
    pin = Pins.query.filter_by(id=id).first()
    if not pin:
        return jsonify({'response': 'Pin not found'}), 404

    pin_data = dict()
    pin_data['id'] = pin.id
    pin_data['name'] = pin.name
    pin_data['number'] = pin.number
    pin_data['assignment'] = pin.assignment
    pin_data['date_created'] = pin.date_created
    return jsonify({'pins': pin_data}), 200


@pins_bp.route('/pins/<id>', methods=['PUT'])
def update_pin(id):
    data = request.get_json()
    pin = Pins.query.filter_by(id=id).first()

    if not pin:
        return jsonify({'response': 'Pin not found!'}), 404

    pin.name = data.get('name')
    pin.number = data.get('number')
    pin.assignment = data.get('assignment')
    db.session.commit()
    return jsonify({'response': f'Pin {pin.name} has been updated!'}), 200

