# pylint:disable=no-member
from argparse import ArgumentParser
from time import sleep

import RPi.GPIO as gpio


def main():
    parser = ArgumentParser(
        prog='gpiooutputtest',
        description='Individually test the given GPIO output pins'
    )
    parser.add_argument(
        'pins',
        type=int,
        nargs='+',
        help='The list of pins to test'
    )
    args = parser.parse_args()
    gpio.setmode(gpio.BOARD)
    for pin in args.pins:
        print('Testing pin', pin)
        gpio.setup(pin, gpio.OUT)
        gpio.output(pin, True)
        sleep(1)
        gpio.output(pin, False)
    gpio.cleanup()


if __name__ == '__main__':
    main()
