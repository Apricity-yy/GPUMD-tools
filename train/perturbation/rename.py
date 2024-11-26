#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

source_folder = "./combined_structures/"  # 输入文件夹路径

# 获取文件夹内所有文件
file_list = os.listdir(source_folder)

# 排序文件列表
sorted_files = sorted(file_list)

# 重命名文件
for index, file_name in enumerate(sorted_files, start=1):
    # 获取文件扩展名
    file_name_parts = file_name.split('.')
    extension = ""
    if len(file_name_parts) > 1:
        extension = "." + file_name_parts[-1]

    # 构造新的文件名
    new_file_name = f"POSCAR-{index}{extension}"

    # 重命名文件
    old_file_path = os.path.join(source_folder, file_name)
    new_file_path = os.path.join(source_folder, new_file_name)
    os.rename(old_file_path, new_file_path)

print("ok")
