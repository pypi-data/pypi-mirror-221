"""
    QuaO Project logging_config.py Copyright © CITYNOW Co. Ltd. All rights reserved.
"""
import sys
import threading

from loguru import logger

logger.add(sink=sys.stderr,
           format=threading.current_thread().name + " : {level} : {time} : {message}: {process}",
           level='DEBUG')

