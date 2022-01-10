#!/usr/bin/env python3
import argparse
from func import Get
import sys

__version__ = '0.1.0'

# disables default help
parser = argparse.ArgumentParser(prog='shorty_erl.py', description='Shorten URLs or fetch full URLs.',
                                 usage='%(prog)s [-h] [-u URL] [-s SHORTEN] [-us UNSHORTEN]', add_help=False)
required = parser.add_argument_group('required arguments')
one_or_both = parser.add_argument_group(
    'possible actions (at least one is required)')
optional = parser.add_argument_group('optional arguments')
# adds help back
optional.add_argument(
    '-h',
    '--help',
    action='help',
    default=argparse.SUPPRESS,
    help='show this help message and exit'
)

required.add_argument('-u', '--url', required=True,
                      help='URL', metavar='')
one_or_both.add_argument('-s', '--shorten', action='store_const', const=Get.get_shorten,
                         help='Shorten URL')
one_or_both.add_argument('-us', '--unshorten', action='store_const', const=Get.get_unshorten,
                         help='Check URL shorten status')
optional.add_argument('-v', '--version', action='version',
                      version=f'%(prog)s (version {__version__})')


def main(args=None):
    parsed = parser.parse_args(args=args)
    func = Get(url=parsed.url)
    if parsed.unshorten:
        func.get_unshorten()
    if parsed.shorten:
        func.get_shorten()
    if not parsed.shorten and not parsed.unshorten:
        parser.error('no URL given.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
