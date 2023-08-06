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
    parser.add_argument(
        '-b',
        '--bcm',
        action='store_true',
        help='Set the GPIO mode to BCM rather than BOARD'
    )
    args = parser.parse_args()
    if hasattr(args, 'b') and args.b or hasattr(args, 'bcm') and args.bcm:
        gpio.setmode(gpio.BCM)
    else:
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
