#!/usr/bin/python3
# -*- coding:utf-8 -*-
import configparser
import os

from tools.color import print_error

CONFIG_PATH = os.path.dirname(__file__) + "/../config/env.ini"

def readConfig(section, option, config_path=CONFIG_PATH):
    parser = configparser.ConfigParser()
    parser.read(config_path, encoding="utf-8")
    result = None
    try:
        result = parser.get(section, option)
    except configparser.Error as e:
        print_error(e)

    return result

def writeConfig(section, option, value, config_path=CONFIG_PATH):
    parser = configparser.ConfigParser()
    parser.read(config_path, encoding="utf-8")

    if not parser.has_section(section):
        parser.add_section(section)
    parser.set(section, option, value)

    config = None
    try:
        config = open(config_path, "w+")
        parser.write(config)
    except FileNotFoundError as e:
        print_error(e)
    finally:
        if config is not None:
            config.close()


if __name__ == '__main__':
    print(readConfig("engine_key", "stag"))