import sys


def gui_print(string):
    """ this function flushes output after print (required when printing in gui mode) """
    print(string)
    sys.stdout.flush()
