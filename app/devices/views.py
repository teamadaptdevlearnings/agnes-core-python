from flask import Blueprint

devices_page = Blueprint('devices', __name__)

@devices_page.route("/devices")
def devices():
    return "<h2>Devices page</h2>"
