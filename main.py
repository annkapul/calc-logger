from calculator import Calculator
import logging

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

if __name__ == '__main__':
    calc = Calculator()
    logging.info(calc.Divide(4, 2))
    logging.info(calc.Divide(10, 3))
    logging.info(calc.Sum(3.5, 6.7))
    logging.info(calc.Sum('aaaa', 'BB'))
    logging.info(calc.Subtract(10, b=6))
    logging.info(calc.Subtract(-10, b=6))
    logging.info(calc.Multiply(a=6, b=5))
    logging.info(calc.Multiply(-16, 0.00005))

    logging.info(calc.Sum(complex(1, 2), complex(1, 2)))
    logging.info(calc.Divide(complex(1, 2), complex(1, 2)))
    logging.info(calc.Multiply(complex(5, 3), complex(1, 2)))
    logging.info(calc.Subtract(complex(7, 6), complex(1, 2)))

    logging.info(calc.Subtract(complex(1, 2), 2))

    try:
        logging.info(calc.Divide('110', '10'))
    except BaseException as e:
        print("Can't do operation with binary numbers")
