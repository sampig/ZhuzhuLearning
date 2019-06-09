#!/usr/bin/env python

import logging


def my_log():
    # https://docs.python.org/2/library/logging.html#logrecord-attributes
    output_format = "%(asctime)s %(levelname)s\t%(module)s %(funcName)s %(lineno)d %(message)s %(process)d %(processName)s %(thread)d %(threadName)s"
    # logging.basicConfig(filename="program.log",level=logging.DEBUG)
    logging.basicConfig(format=output_format, level=logging.DEBUG)
    logging.debug("This is a Debug message.")
    logging.info("This is an Info message.")
    logging.warning("This is a Warning message.")
    logging.warning("This is another Warning message.")


if __name__ == "__main__":
    my_log()
