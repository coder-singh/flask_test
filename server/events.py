from flask_socketio import SocketIO, emit

from temp import get_lines_from_offset, get_last_n_offset

socketio = SocketIO()


@socketio.on("new_log")
def handle_new_log(data):
    emit("new_log_js", {"message": data}, broadcast=True)


@socketio.on("user_landed")
def handle_user_landed():
    print('came here !!!')
    last_10_offset = get_last_n_offset('app.log', 10)
    _, data = get_lines_from_offset('app.log', last_10_offset)
    data = "".join(data)
    emit("new_log_js", {"message": data}, broadcast=True)
