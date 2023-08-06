# -*- coding: utf-8 -*-
__file__ = 'folder_process.py'
__date__ = '2023/1/26'
__author__ = 'Zhiyong ZHANG'

import os


def get_folder_list(path):
    """
    递归读取folder下的目录与文件
    usage:
    """
    items = {'folder': [], 'file': []}
    for i in os.listdir(path):
        i = i.strip(' ')
        if i == '' or i == '.DS_Store':    # 过滤Mac中的.DS_Store文件
            continue

        temp_dir = os.path.join(path, i)
        if os.path.isdir(temp_dir):
            temp = {"dirname": temp_dir, 'folder': [], 'file': []}
            items['folder'].append(items(temp_dir, temp))
        else:
            items['file'].append(i)
    return items
