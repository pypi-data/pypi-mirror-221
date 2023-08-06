# -*- coding = utf-8 -*-
__file__ = 'folder_file_process.py'
__date__ = '2022/11/30'
__author__ = 'Zhiyong ZHANG'

import os
import struct


class Component:
    def __init__(self, name):
        self.name = name

    def move(self, new_path):
        new_folder = get_path(new_path)
        del self.parent.children[self.name]
        new_folder.children[self.name] = self
        self.parent = new_folder

    def delete(self):
        del self.parent.children[self.name]


class Folder(Component):
    def __init__(self, name):
        super().__init__(name)
        self.children = {}

    @staticmethod
    def create(path, report_warning=False):
        if not os.path.isdir(path):
            try:
                os.makedirs(path)
            except Exception as e:
                print('Error: %s, path: %s' % (e.__class__.__name__, path))
        elif report_warning:
            print('Warning: folder %s already exists!' % path)
        else:
            pass

    def add_child(self, child):
        child.parent = self
        self.children[child.name] = child
        path = os.path.join(self.name, child.name)
        self.create(path)

    def list(self, path):
        pass

    def copy(self, new_path):
        pass


class File(Component):
    def __init__(self, name, contents=''):
        super().__init__(name)
        self.contents = contents

    def copy(self, new_path):
        pass

    def get_file_type(self):
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
        with open(self.name, 'rb') as f:    # 读取二进制文件开头一定的长度
            byte = f.read(max_len)

        byte_list = struct.unpack('B' * max_len, byte)  # 解析为元组
        code = ''.join([('%X' % each).zfill(2) for each in byte_list])  # 转为16进制
        result = list(filter(lambda x: code.startswith(x), type_dict))
        if result:
            return type_dict[result[0]]
        else:
            return 'unknown'


root = Folder('')


def get_path(path):
    names = path.split("/")[1:]
    node = root
    for name in names:
        node = node.children[name]
    return node
