from calculator import Calculator
import logging

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

if __name__ == '__main__':
    logging.info(Calculator().Divide(4, 2))
    logging.info(Calculator().Sum(3.5, 6.7))
    logging.info(Calculator().Subtract(10, b=6))
    logging.info(Calculator().Multiply(a=6, b=5))
