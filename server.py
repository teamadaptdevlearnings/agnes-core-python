from flask import Flask
from app.users.views import users_bp
from app.devices.views import devices_bp, pins_bp
from config.database import initialize_db

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/agnes_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'nsx)e96@!)p*=)%adhig8mv$5x0psx38ywj(@k18zx70pu=4yq'

initialize_db(app)


@app.route("/")
def main():
    return 'Welcome to Agnes API'


# Register Blueprint
app.register_blueprint(users_bp)
app.register_blueprint(devices_bp)
app.register_blueprint(pins_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
