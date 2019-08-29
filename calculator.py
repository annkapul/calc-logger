import logging

logging.basicConfig(level=logging.DEBUG, format='%(message)s')


def logger(func):
    def wrapper(*args, **kwargs):
        a = args[1] if args.__len__() > 1 else kwargs.get('a')
        b = args[2] if args.__len__() > 2 else kwargs.get('b')
        logging.info(f"Входными значениями A и B являются ‘{a}’ и ‘{b}’")
        return func(*args, **kwargs)
    return wrapper


class Calculator(object):
    @logger
    def Sum(self, a, b):
        return a + b

    @logger
    def Multiply(self, a, b):
        return a * b

    @logger
    def Divide(self, a, b):
        return a / b

    @logger
    def Subtract(self, a, b):
        return a - b
