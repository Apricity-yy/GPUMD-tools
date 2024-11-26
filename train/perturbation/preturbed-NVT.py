#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shutil
import dpdata
import os

path = os.getcwd()

# 创建存放微扰后结构的文件夹
output_folder = path + "/perturbed_structures"
os.makedirs(output_folder, exist_ok=True)

# 复制并重命名原始的50个文件到对应的文件夹，并进行微扰操作
for i in range(50):
    src_file_path = path + f"/POSCAR-{i+1}"
    dst_folder_path = path + f"/{i+1}"

    # 创建对应的文件夹
    os.makedirs(dst_folder_path, exist_ok=True)

    # 复制原始文件到对应的文件夹并重命名为POSCAR
    shutil.copy(src_file_path, dst_folder_path + "/POSCAR")

    # 读取原始的POSCAR文件
    src_file_path = dst_folder_path + "/POSCAR"

    # 执行微扰操作多次
    for perturbation_num in range(1):  # 执行n次微扰操作
        # 读取原始的POSCAR文件
        src_file_path = dst_folder_path + "/POSCAR"

        # 执行微扰操作
        s = dpdata.System(src_file_path).perturb(
            pert_num=1,
            cell_pert_fraction=0.06,
            atom_pert_distance=0,
            atom_pert_style="uniform",
        )

        # 将微扰后的结构保存为POSCAR文件
        s.to_vasp_poscar(dst_folder_path + f"/POSCAR_perturbed_{perturbation_num + 1}")

        # 更新源文件为微扰后的结构
        src_file_path = dst_folder_path + f"/POSCAR_perturbed_{perturbation_num + 1}"

    # 复制微扰后的文件到新的文件夹
    for j in range(1, 1):  # n个微扰后的文件
        perturbed_file_path = dst_folder_path + f"/POSCAR_perturbed_{j}"
        shutil.copy(perturbed_file_path, output_folder)
