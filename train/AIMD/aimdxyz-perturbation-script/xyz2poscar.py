#!/usr/bin/python
# -*- coding: utf-8 -*-

from ase.io import read, write

# ��ȡ��������ṹ��XYZ�ļ�
structures = read('train1.xyz', index=':')

# ��ÿ���ṹ����Ϊ������POSCAR�ļ�
for i, structure in enumerate(structures):
    write(f'POSCAR-{i+1}', structure, format='vasp')