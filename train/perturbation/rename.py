#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

source_folder = "./combined_structures/"  # �����ļ���·��

# ��ȡ�ļ����������ļ�
file_list = os.listdir(source_folder)

# �����ļ��б�
sorted_files = sorted(file_list)

# �������ļ�
for index, file_name in enumerate(sorted_files, start=1):
    # ��ȡ�ļ���չ��
    file_name_parts = file_name.split('.')
    extension = ""
    if len(file_name_parts) > 1:
        extension = "." + file_name_parts[-1]

    # �����µ��ļ���
    new_file_name = f"POSCAR-{index}{extension}"

    # �������ļ�
    old_file_path = os.path.join(source_folder, file_name)
    new_file_path = os.path.join(source_folder, new_file_name)
    os.rename(old_file_path, new_file_path)

print("ok")
