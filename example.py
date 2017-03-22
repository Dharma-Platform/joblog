#!/usr/bin/python3
#
# Example of using joblog.py.
#

import joblog
import logging
import random

joblog.init()
logging.info("example in Python")

total = random.randint(1000000, 2000000)
for i in range(0, total):
    if ((i + 1) % 100000) == 0 or i + 1 == total:
        logging.info("%i/%i (%.1f%%) processed", i + 1, total, 100.0 * (i + 1) / total)

logging.warn("all done")

try:
    x = 5 / 0
except Exception:
    logging.exception("intentional exception")

logging.info("log file was %s", joblog.logfile_name)
