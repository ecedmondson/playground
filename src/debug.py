from traceback import print_stack
import signal

def runtime_debug(signal_number, stack):
    print_stack()

