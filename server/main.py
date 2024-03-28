from flask import Flask
from events import socketio
from routes import routes_bp

app = Flask(__name__)
app.config["Debug"] = True


if __name__ == "__main__":
    app.register_blueprint(routes_bp)
    socketio.init_app(app)
    socketio.run(app, port=5500)
