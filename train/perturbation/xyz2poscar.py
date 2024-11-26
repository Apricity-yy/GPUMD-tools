#!/usr/bin/python
# -*- coding: utf-8 -*-

from ase.io import read, write

# 读取包含多个结构的XYZ文件
structures = read('train1.xyz', index=':')

# 将每个结构保存为单独的POSCAR文件
for i, structure in enumerate(structures):
    write(f'POSCAR-{i+1}', structure, format='vasp')