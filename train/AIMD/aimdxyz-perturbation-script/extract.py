#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shutil
import os

source_folder = "./"  # Դ�ļ���·��
output_folder = "./perturbation_structures/"  # ����ļ���·��

# ��������ļ���
os.makedirs(output_folder, exist_ok=True)

# ����1-50�ļ���
for i in range(1, 51):
    folder_path = os.path.join(source_folder, str(i))

    # ����ļ����Ƿ����
    if os.path.exists(folder_path):
        # ��ȡPOSCAR_perturbed_1��POSCAR_perturbed_2
        poscar1_path = os.path.join(folder_path, "POSCAR_perturbed_1")
        poscar2_path = os.path.join(folder_path, "POSCAR_perturbed_2")

        # ����ļ��Ƿ����
        if os.path.exists(poscar1_path):
            # �����������Ƶ�����ļ���
            output_poscar1_path = os.path.join(output_folder, f"POSCAR-{i}-1")
            shutil.copy(poscar1_path, output_poscar1_path)

        if os.path.exists(poscar2_path):
            # �����������Ƶ�����ļ���
            output_poscar2_path = os.path.join(output_folder, f"POSCAR-{i}-2")
            shutil.copy(poscar2_path, output_poscar2_path)

print("ok")
