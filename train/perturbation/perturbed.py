#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shutil
import dpdata
import os

path = os.getcwd()
os.makedirs(path+"/"+"0")

src_file_path = path+"/"+"POSCAR"
dst_folder_path = path+"/"+"0"
shutil.copy(src_file_path, dst_folder_path)  # 

for i in range(50):  
    s = dpdata.System("./POSCAR").perturb(
        pert_num=1,
        cell_pert_fraction=0.05,
        atom_pert_distance=0.05,
        atom_pert_style="uniform",
    )
    perpath = path+"/"+str(i+1)
    os.makedirs(perpath)
    s.to_vasp_poscar(perpath+"/"+"POSCAR")