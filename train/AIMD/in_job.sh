#!/bin/bash

# �����Ƶ��ļ�
files=("INCAR" "KPOINTS" "POTCAR" "vasp.pbs")

# ���ļ������ƽ�������ѭ������
for folder in $(ls -d [0-9]*/ | sort -V); do
    # ������ļ�������в���
    if [ -d "$folder" ]; then
        # ���ļ�����������ȡ���
        if [[ "$folder" =~ ^([0-9]+)\/$ ]]; then
            folder_number="${BASH_REMATCH[1]}"
            # ѭ�������ļ���ÿ���ļ�����
            for file in "${files[@]}"; do
                cp "$file" "$folder"
            done
            echo "success-$folder_number"
        fi
    fi
done