#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shutil
import os

source_folder = "./"  # 源文件夹路径
output_folder = "./perturbation_structures/"  # 输出文件夹路径

# 创建输出文件夹
os.makedirs(output_folder, exist_ok=True)

# 遍历1-50文件夹
for i in range(1, 51):
    folder_path = os.path.join(source_folder, str(i))

    # 检查文件夹是否存在
    if os.path.exists(folder_path):
        # 提取POSCAR_perturbed_1和POSCAR_perturbed_2
        poscar1_path = os.path.join(folder_path, "POSCAR_perturbed_1")
        poscar2_path = os.path.join(folder_path, "POSCAR_perturbed_2")

        # 检查文件是否存在
        if os.path.exists(poscar1_path):
            # 重命名并复制到输出文件夹
            output_poscar1_path = os.path.join(output_folder, f"POSCAR-{i}-1")
            shutil.copy(poscar1_path, output_poscar1_path)

        if os.path.exists(poscar2_path):
            # 重命名并复制到输出文件夹
            output_poscar2_path = os.path.join(output_folder, f"POSCAR-{i}-2")
            shutil.copy(poscar2_path, output_poscar2_path)

print("ok")
