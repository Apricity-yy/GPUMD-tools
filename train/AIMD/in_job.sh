#!/bin/bash

# 待复制的文件
files=("INCAR" "KPOINTS" "POTCAR" "vasp.pbs")

# 对文件夹名称进行排序并循环遍历
for folder in $(ls -d [0-9]*/ | sort -V); do
    # 如果是文件夹则进行操作
    if [ -d "$folder" ]; then
        # 从文件夹名称中提取序号
        if [[ "$folder" =~ ^([0-9]+)\/$ ]]; then
            folder_number="${BASH_REMATCH[1]}"
            # 循环复制文件到每个文件夹中
            for file in "${files[@]}"; do
                cp "$file" "$folder"
            done
            echo "success-$folder_number"
        fi
    fi
done