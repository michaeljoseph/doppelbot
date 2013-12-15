"""
doppelbot.

Usage:
  doppelbot [options] command <param> <another_params>
  doppelbot [options] another-command <param>

  doppelbot -h | --help

Options:
  --kw-arg=<kw>         Keyword option description.
  -b --boolean          Boolean option description.
  --debug               Debug.

  -h --help             Show this screen.
"""

from docopt import docopt
import logging

import doppelbot

log = logging.getLogger(__name__)


def main():
    arguments = docopt(__doc__, version=doppelbot.__version__)
    debug = arguments['--debug']
    logging.basicConfig(level=logging.DEBUG if debug else logging.INFO)
    log.debug('arguments: %s', arguments)
