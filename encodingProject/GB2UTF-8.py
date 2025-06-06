"""
 v1.0
    1、修复部分GB2312文件解码错误的bug，测试ok；

"""
import os

def convert_encoding(file_path, from_encoding, to_encoding):
    """
    将指定文件从一种编码转换为另一种编码
    """
    try:
        # 尝试直接转换，忽略非法字节
        with open(file_path, 'r', encoding=from_encoding, errors='replace') as file:
            content = file.read()
        with open(file_path, 'w', encoding=to_encoding, newline='') as file:
            file.write(content)
        print(f"Converted {file_path} from {from_encoding} to {to_encoding}")
    except Exception as e:
        print(f"Error converting {file_path}: {e}")

def batch_convert(directory, from_encoding, to_encoding, extensions):
    """
    批量转换指定目录中的文件
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # 检查文件扩展名是否为 .c 或 .h 或 .txt，忽略大小写
            if any(file.lower().endswith(ext.lower()) for ext in extensions):
                print(f"Processing file: {file_path}")
                convert_encoding(file_path, from_encoding, to_encoding)
            else:
                print(f"Skipped {file_path} (not a .c, .h or .txt file)")

# 设置要转换的目录和编码
directory = "F:/boatman/firmware/remote/bm-dhrc/bm-dhrc-3518-fw"  # 替换为你的文件夹路径
from_encoding = "gb2312"
to_encoding = "utf-8"
extensions = ['.c', '.h', '.txt']  # 只处理 .c、.h 和 .txt 文件

# 执行批量转换
batch_convert(directory, from_encoding, to_encoding, extensions)

# 测试代码
def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')


# test code

def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
