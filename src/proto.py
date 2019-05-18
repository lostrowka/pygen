import socket
import struct
from abc import ABC, abstractmethod

from utils import checksum


class Protocol(ABC):
    def __init__(self, name, ip, port):
        self.sock = None
        self.name = name
        self.ip = ip
        self.port = port

    def get_socket(self):
        return self.sock

    @abstractmethod
    def send_data(self, data):
        pass


class TCP(Protocol):
    def __init__(self, ip, port):
        Protocol.__init__(self, "TCP", ip, port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        # TODO: write connection establishment

    def send_data(self, data):
        # self.sock.sendto(bytes(data, 'utf-8'), (self.ip, self.port))
        # TODO: connection establishment not implemented yet, send data useless
        raise NotImplementedError


class UDP(Protocol):
    def __init__(self, ip, port):
        Protocol.__init__(self, "UDP", ip, port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

    def send_data(self, data):
        self.sock.sendto(bytes(data, 'utf-8'), (self.ip, self.port))


class ICMP(Protocol):
    def __init__(self, ip, port):
        Protocol.__init__(self, "ICMP", ip, port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

    def create_packet(self, id, data):
        # calculate checksum from clear header
        header = struct.pack('bbhhh', 8, 0, 0, id, 1)
        header = struct.pack('bbHHh', 8, 0, socket.htons(checksum(header + bytes(data, 'utf-8'))), id, 1)
        return header + bytes(data, 'utf-8')

    def send_data(self, data):
        self.sock.sendto(self.create_packet(1, data), (self.ip, self.port))
