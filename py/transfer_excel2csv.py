# -*- coding: utf-8 -*-
# @Last Modified by:   shiqi
# @Last Modified time: 2024-10-10 16:24

import os
import sys
import pandas as pd
import numpy as np
from pathlib import Path
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter


def cmd_line_args(argc, argv):
    """
    处理命令行参数
    """
    if argc < 2 or argc > 3 or argc != len(argv):
        print(f"Usage: python script.py INPUT_FILE <OUTPUT_FILE>")
        return None, None

    if argc == 2:
        output_file = argv[1].replace(".xlsx", ".csv")
        return argv[1], output_file

    return argv[1], argv[2]


def trans_excel2_csv(input_file, output_file):
    try:
        # 读取Excel文件
        excel_file = input_file
        df = pd.read_excel(excel_file)

        # 保存为CSV文件
        csv_file = output_file
        df.to_csv(csv_file, index=False)

        print(f"Excel文件:{excel_file} 已成功转换为CSV:{csv_file}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    input_file, output_file = cmd_line_args(len(sys.argv), sys.argv)
    if input_file is None or output_file is None:
        sys.exit(-1)

    trans_excel2_csv(input_file, output_file)
    print("Done")
