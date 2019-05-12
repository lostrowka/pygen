import sys


def gui_print(string):
    """ this function flushes output after print (required when printing in gui mode) """
    print(string)
    sys.stdout.flush()


def checksum(data):
    """ calculate network checksum out of given data """
    if len(data) % 2 != 0:
        data += b'\x00'

    chksum = 0
    for i in range(0, len(data), 2):
        if i + 1 >= len(data):
            chksum += data[i] & 0xFF
        else:
            w = ((data[i] << 8) & 0xFF00) + (data[i + 1] & 0xFF)
            chksum += w

    while (chksum >> 16) > 0:
        chksum = (chksum & 0xFFFF) + (chksum >> 16)

    return ~chksum & 0xFFFF


def get_supported_protocols():
    """ get list of supported protocols """
    from proto import Protocol

    protocol_list = []
    for proto in Protocol.__subclasses__():
        protocol_list.append(proto.__name__)
    return protocol_list
