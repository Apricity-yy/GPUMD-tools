#!/bin/bash

folder_path="/work1/xdsc0365/tf/SWCNT-nanorope/vdw/aimd-single-energy/2"  # �滻Ϊ����ļ���·��

# �����ļ���
for folder_name in $(ls -d "$folder_path"/*/); do
    if [ -d "$folder_name" ]; then
        # ����Ƿ����OUTCAR�ļ�
        if [ -e "$folder_name/OUTCAR" ]; then
            echo "$folder_name ��OUTCAR�ļ�"
        else
            echo "$folder_name û��OUTCAR�ļ�"
            missing_outcar_folder="$folder_name"
        fi
    fi
done

# �������û��OUTCAR�ļ����ļ��У���������ļ��е�����
if [ -n "$missing_outcar_folder" ]; then
    echo "no OUTCAR: $missing_outcar_folder"
fi
