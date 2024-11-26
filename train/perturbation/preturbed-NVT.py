#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shutil
import dpdata
import os

path = os.getcwd()

# �������΢�ź�ṹ���ļ���
output_folder = path + "/perturbed_structures"
os.makedirs(output_folder, exist_ok=True)

# ���Ʋ�������ԭʼ��50���ļ�����Ӧ���ļ��У�������΢�Ų���
for i in range(50):
    src_file_path = path + f"/POSCAR-{i+1}"
    dst_folder_path = path + f"/{i+1}"

    # ������Ӧ���ļ���
    os.makedirs(dst_folder_path, exist_ok=True)

    # ����ԭʼ�ļ�����Ӧ���ļ��в�������ΪPOSCAR
    shutil.copy(src_file_path, dst_folder_path + "/POSCAR")

    # ��ȡԭʼ��POSCAR�ļ�
    src_file_path = dst_folder_path + "/POSCAR"

    # ִ��΢�Ų������
    for perturbation_num in range(1):  # ִ��n��΢�Ų���
        # ��ȡԭʼ��POSCAR�ļ�
        src_file_path = dst_folder_path + "/POSCAR"

        # ִ��΢�Ų���
        s = dpdata.System(src_file_path).perturb(
            pert_num=1,
            cell_pert_fraction=0.06,
            atom_pert_distance=0,
            atom_pert_style="uniform",
        )

        # ��΢�ź�Ľṹ����ΪPOSCAR�ļ�
        s.to_vasp_poscar(dst_folder_path + f"/POSCAR_perturbed_{perturbation_num + 1}")

        # ����Դ�ļ�Ϊ΢�ź�Ľṹ
        src_file_path = dst_folder_path + f"/POSCAR_perturbed_{perturbation_num + 1}"

    # ����΢�ź���ļ����µ��ļ���
    for j in range(1, 1):  # n��΢�ź���ļ�
        perturbed_file_path = dst_folder_path + f"/POSCAR_perturbed_{j}"
        shutil.copy(perturbed_file_path, output_folder)
