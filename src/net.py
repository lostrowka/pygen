import threading
import time

from proto import *


class PktFlow:
    """ PktFlow class represents single generator task with appropriate socket """

    def __init__(self, dest, dest_port, proto, message, freq):
        self.dest = dest
        self.dest_port = dest_port
        self.proto = self.init_socket(proto)
        self.data = message
        self.freq = freq
        self.keep_running = True
        self.thread = threading.Thread(target=self.run_task)
        self.exit_thread = False

    def init_socket(self, proto_name):
        for proto in Protocol.__subclasses__():
            if proto.__name__ == proto_name:
                return proto(self.dest, int(self.dest_port))

    def send_data(self):
        self.proto.send_data(self.data)

    def flip_keep_sending(self):
        self.keep_running = not self.keep_running

    def start(self):
        self.thread.start()

    def run_task(self):
        while not self.exit_thread:
            while self.keep_running:
                self.send_data()
                time.sleep(int(self.freq) / 1000)
