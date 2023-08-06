# -*- coding: utf-8 -*-
__file__ = 'file_process.py'
__date__ = '2023/1/26'
__author__ = 'Zhiyong ZHANG'

import struct
import pandas as pd
from shutil import copyfile


class File:
    def __init__(self, file_path=None, content=None):
        self.file_path = file_path
        self.content = content

    @staticmethod
    def copy(src_full_path, target_full_path):
        try:
            copyfile(src_full_path, target_full_path)
        except Exception as e:
            print('wrong in copy %s to %s, ' % (src_full_path, target_full_path, str(e)))

    @staticmethod
    def get_file_type(file_path, file_name):
        type_dict = {'424D': 'bmp', 'FFD8FF': 'jpg', '2E524D46': 'rm', '4D546864': 'mid',
                     '89504E47': 'png', '47494638': 'gif', '49492A00': 'tif', '41433130': 'dwg',
                     '38425053': 'psd', '2142444E': 'pst', 'FF575043': 'wpd', 'AC9EBD8F': 'qdf',
                     'E3828596': 'pwl', '504B0304': 'zip', '52617221': 'rar', '57415645': 'wav',
                     '41564920': 'avi', '2E7261FD': 'ram', '000001BA': 'mpg', '000001B3': 'mpg',
                     '6D6F6F76': 'mov', '7B5C727466': 'rtf', '3C3F786D6C': 'xml',
                     '68746D6C3E': 'html', 'D0CF11E0': 'doc/xls', '255044462D312E': 'pdf',
                     'CFAD12FEC5FD746F': 'dbx', '3026B2758E66CF11': 'asf',
                     '5374616E64617264204A': 'mdb', '252150532D41646F6265': 'ps/eps',
                     '44656C69766572792D646174653A': 'eml'}
        max_len = len(max(type_dict, key=len)) // 2
        file_full_path = file_path + '/' + file_name

        try:
            with open(file_full_path, 'rb') as f:    # 读取二进制文件开头一定的长度
                byte = f.read(max_len)
            byte_list = struct.unpack('B' * max_len, byte)  # 解析为元组
            code = ''.join([('%X' % each).zfill(2) for each in byte_list])  # 转为16进制
            result = list(filter(lambda x: code.startswith(x), type_dict))
            if result:
                return type_dict[result[0]]
            else:
                return 'unknown'
        except Exception as e:
            print('error in get file type: %s, %s' % (file_full_path, str(e)))
            return 'error'


class CSVFile:
    def __init__(self, file_name, file_path=None):
        self.file_name = file_name
        self.file_path = file_path

    def read_file(self, column_name):
        df = pd.read_csv(self.file_path + '/' + self.file_name)
        column_values = list(df[column_name])
        return column_values

    def read_file_distinct(self, column_name1, column_name2):
        df = pd.read_csv(self.file_path + '/' + self.file_name)
        column1_values = list(df[column_name1])
        column2_values = list(df[column_name2])

        column2_value_distinct = []
        for i, column1_value in enumerate(column1_values):
            if column1_value not in column1_values[:i]:
                column2_value_distinct.append(column2_values[i])
        return column2_value_distinct

    def write_file(self, line, header=False):
        df = pd.read_csv(self.file_path + '/' + self.file_name)
        column_values = list(df[column_name])

