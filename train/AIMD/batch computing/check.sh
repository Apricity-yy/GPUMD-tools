#!/bin/bash

folder_path="/work1/xdsc0365/tf/SWCNT-nanorope/vdw/aimd-single-energy/2"  # 替换为你的文件夹路径

# 遍历文件夹
for folder_name in $(ls -d "$folder_path"/*/); do
    if [ -d "$folder_name" ]; then
        # 检查是否存在OUTCAR文件
        if [ -e "$folder_name/OUTCAR" ]; then
            echo "$folder_name 有OUTCAR文件"
        else
            echo "$folder_name 没有OUTCAR文件"
            missing_outcar_folder="$folder_name"
        fi
    fi
done

# 如果存在没有OUTCAR文件的文件夹，则输出该文件夹的名称
if [ -n "$missing_outcar_folder" ]; then
    echo "no OUTCAR: $missing_outcar_folder"
fi
