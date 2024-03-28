from socketIO_client import SocketIO
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from temp import get_lines_from_offset, get_last_n_offset


class EventHandler(FileSystemEventHandler):
    def __init__(self):
        self.socketio = SocketIO('localhost', 5500)
        self.last_offset = get_last_n_offset('app.log', 0)

    def on_any_event(self, event):
        self.last_offset, data = get_lines_from_offset('app.log', self.last_offset)
        data = "".join(data)
        print(data)
        self.socketio.emit("new_log", data)


if __name__ == "__main__":
    path = "app.log"
    event_handler = EventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    observer.join()
