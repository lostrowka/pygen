import sys


def gui_print(string):
    """ this function flushes output after print (required when printing in gui mode) """
    print(string)
    sys.stdout.flush()


def get_supported_protocols():
    """ get list of supported protocols """
    from proto import Protocol

    protocol_list = []
    for proto in Protocol.__subclasses__():
        protocol_list.append(proto.__name__)
    return protocol_list
