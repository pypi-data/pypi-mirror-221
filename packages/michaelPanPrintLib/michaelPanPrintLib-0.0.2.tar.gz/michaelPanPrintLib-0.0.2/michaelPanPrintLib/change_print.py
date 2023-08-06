# ***************************************************************
# Maintainers:
#     chuntong pan <panzhang1314@gmail.com>
# Date:
#     2023.7
# ***************************************************************
import datetime
from colorama import init, Fore, Style
import os
import inspect
"""
    1.改变原有python的控制台打印样式
    2.旨在简单高效
    ✅  ⚠️  🚀
"""


def print_with_style(args, color='red'):
    """
    :param args: 要打印的字符串
    :param color: 打印字体颜色
    :return: 无返回值
    """
    if color == "red":
        color = Fore.RED
    elif color == "black":
        color = Fore.BLACK
    elif color == "white":
        color = Fore.WHITE
    elif color == "magenta":
        color = Fore.MAGENTA
    elif color == "green":
        color = Fore.GREEN
    elif color == "yellow":
        color = Fore.YELLOW
    elif color == "blue":
        color = Fore.BLUE
    elif color == "cyan":
        color = Fore.CYAN
    else:
        raise Exception("未找到该颜色")
    args = f"{color}{Style.BRIGHT}{args}{Style.RESET_ALL}"
    init()  # 改变颜色初始化
    frame = inspect.stack()[1]  # 获取代码位置
    info = inspect.getframeinfo(frame[0])
    # 打印代码位置和要输出的内容
    if 10 <info.lineno < 100:
        print(f"{os.path.basename(info.filename)}:{info.lineno} 【{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}】", args)
    elif info.lineno > 100:
        print(f"{os.path.basename(info.filename)}:{info.lineno}【{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}】", args)
    else:
        print(f"{os.path.basename(info.filename)}:{info.lineno}  【{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}】", args)
