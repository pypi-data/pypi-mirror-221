# -*- coding: utf-8 -*-
__file__ = 'logger.py'
__date__ = '2023/1/25'
__author__ = 'Zhiyong ZHANG'


import logging
from . import folder_file_process as ff


class Log:
    def __init__(self, file_name, file_path=None):
        self.file_name = file_name
        self.file_path = file_path

    def write(self, log_info, log_type='info', blank_line=False):
        # If the log folder doesn't exist, create it.
        self.create_folder()

        # use utf-8 in case of UnicodeEncodeError: 'ascii' codec can't encode characters
        logfile = logging.FileHandler(self.file_path + '/' + self.file_name, encoding='utf-8')
        fmt = logging.Formatter(fmt=self.format('log'), datefmt=self.format('time'))
        logfile.setFormatter(fmt)
        logger = logging.Logger(name='logger')
        logger.addHandler(logfile)

        if blank_line:
            log_info = log_info + '\n'

        if log_type == "info":
            logger.log(msg=log_info, level=logging.INFO)
        elif log_type == "debug":
            logger.log(msg=log_info, level=logging.DEBUG)
        elif log_type == "warning":
            logger.log(msg=log_info, level=logging.WARNING)
        elif log_type == "error":
            logger.log(msg=log_info, level=logging.ERROR)
        elif log_type == "critical":
            logger.log(msg=log_info, level=logging.CRITICAL)
        else:
            log_info = "Your log type %s is not supported: debug, info, warning, error, " \
                       "critical!" % log_type
            logger.log(msg=log_info, level=logging.CRITICAL)

        # If don't remove handler, the msg will append to original file.
        logger.removeHandler(logfile)

    def create_folder(self):
        log_folder = ff.Folder(self.file_path)
        log_folder.create(log_folder.name)

    @staticmethod
    def format(file_type):
        if file_type == 'log':
            # asctime, levelname, message ??
            result = "%(asctime)s - %(levelname)s: %(message)s"
        elif file_type == 'time':
            result = "%Y-%m-%d %H:%M:%S"
        return result
