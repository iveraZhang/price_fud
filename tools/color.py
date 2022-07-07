#!/usr/bin/python3
# -*- coding:utf-8 -*-

STYLE = {
    # 前景色
    'fore':
        {
            'black': 30,  # 黑色
            'red': 31,  # 红色
            'green': 32,  # 绿色
            'yellow': 33,  # 黄色
            'blue': 34,  # 蓝色
            'purple': 35,  # 紫红色
            'cyan': 36,  # 青蓝色
            'white': 37,  # 白色
        },
    # 背景
    'back':
        {
            'black': 40,  # 黑色
            'red': 41,  # 红色
            'green': 42,  # 绿色
            'yellow': 43,  # 黄色
            'blue': 44,  # 蓝色
            'purple': 45,  # 紫红色
            'cyan': 46,  # 青蓝色
            'white': 47,  # 白色
        },
    # 显示模式
    'mode':
        {
            'normal': 0,  # 终端默认设置
            'bold': 1,  # 高亮显示
            'underline': 4,  # 使用下划线
            'blink': 5,  # 闪烁
            'invert': 7,  # 反白显示
            'hide': 8,  # 不可见
        },
    # 默认
    'default': 0
}


def use_style(string, fore='', back='', mode=''):
    mode = '%s' % STYLE['mode'][mode] if STYLE['mode'].get(mode) else ''
    fore = '%s' % STYLE['fore'][fore] if STYLE['fore'].get(fore) else ''
    back = '%s' % STYLE['back'][back] if STYLE['back'].get(back) else ''
    style = ';'.join([s for s in [mode, fore, back] if s])
    style = '\033[%sm' % style if style else ''
    end = '\033[%sm' % STYLE['default']
    return '%s%s%s' % (style, string, end)


class ColourPrint:
    @staticmethod
    def print_red(text):
        print(use_style(text, fore="red"))

    @staticmethod
    def print_yellow(text):
        print(use_style(text, fore="yellow"))

    @staticmethod
    def print_green(text):
        print(use_style(text, fore="green"))


def print_error(text):
    ColourPrint.print_red(f"[ERROR]{text}")


def print_warning(text):
    ColourPrint.print_yellow(f"[WARNING]{text}")


def print_success(text):
    ColourPrint.print_green(f"[SUCCESS]{text}")


def print_info(text):
    print(f"[INFO]{text}")


if __name__ == '__main__':
    #样式开始+被修饰字符串+样式结束
    a = "\033[31m"
    b = "\033[0m"
    msg = "hello world!"
    print(msg)
    print(a + msg + b)
    print_error(msg)
    print_warning(msg)
    print_success(msg)
    print_info(msg)