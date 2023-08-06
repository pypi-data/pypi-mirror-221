# -*- coding = utf-8 -*-
__file__ = 'log_process.py'
__date__ = '2022/11/30'
__author__ = 'Zhiyong ZHANG'

import logging
from . import folder_file_process as ff


class Log:
    def __init__(self, file_name, file_path):
        self.file_name = file_name
        self.file_path = file_path

    def write(self, contents, log_type='info'):
        # If the log folder doesn't exist, create it.
        self.create_folder()

        logfile = logging.FileHandler(self.file_path + '/' + self.file_name)
        fmt = logging.Formatter(fmt=self.format('log'), datefmt=self.format('date'))
        logfile.setFormatter(fmt)
        logger = logging.Logger(name='logger')
        logger.addHandler(logfile)

        if log_type == "info":
            logger.log(msg=contents, level=logging.INFO)
        elif log_type == "debug":
            logger.log(msg=contents, level=logging.DEBUG)
        elif log_type == "warning":
            logger.log(msg=contents, level=logging.WARNING)
        elif log_type == "error":
            logger.log(msg=contents, level=logging.ERROR)
        elif log_type == "critical":
            logger.log(msg=contents, level=logging.CRITICAL)
        else:
            contents = "Your log type %s is not supported: debug, info, warning, error, " \
                       "critical!" % log_type
            logger.log(msg=contents, level=logging.CRITICAL)

        # If don't remove handler, the msg will append to original file.
        logger.removeHandler(logfile)

    def create_folder(self):
        log_folder = ff.Folder(self.file_path)
        log_folder.create(log_folder.name)

    @staticmethod
    def format(f_type):
        if f_type == 'log':
            # asctime, levelname, message ??
            result = "%(asctime)s - %(levelname)s: %(message)s"
        elif f_type == 'date':
            result = "%Y-%m-%d %H:%M:%S"
        return result
