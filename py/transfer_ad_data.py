import pandas as pd
import sys

# 读取CSV文件
df = pd.read_csv(sys.argv[1])

# 确保第一列是日期类型
df.iloc[:, 0] = pd.to_datetime(df.iloc[:, 0])

# 按照第一列日期从小到大排序
df_sorted = df.sort_values(by=df.columns[0])

# 获取最后一列并转置
last_column_transposed = df_sorted.iloc[:, -1].to_numpy().T

# 创建一个新的DataFrame用于存储转置结果
# 这里将数据作为一行存储，每个元素占据一个独立单元格
df_transposed = pd.DataFrame([last_column_transposed])

# 输出到新的CSV文件
df_transposed.to_csv('transposed_output.csv', index=False, header=False)

print("转置后的最后一列已保存到 transposed_output.csv 文件中。")

