# -*- coding:utf-8 -*-
"""
Created on 2023/7/26 17:43
@File: log.py
---------
@summary:
---------
@Author: luzihang
@Contact: https://github.com/luzihang123
"""
import sys
from datetime import datetime
from os.path import basename
from loguru import logger as logger_
import sys
from sys import exc_info


def get_frame_fallback(n):
    frame = exc_info()[2].tb_frame.f_back
    for _ in range(n):
        frame = frame.f_back
    return frame


if hasattr(sys, "_getframe"):
    get_frame = sys._getframe
else:
    get_frame = get_frame_fallback


def formatted_mob_msg(msg, level, frame):
    """
    :param msg:         日志内容
    :param level:       日志级别
    :return:            格式化后的日志内容
    """
    formatted_level = "{0:>6}".format(f"{level}")
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    formatted_msg = f"[{ts}{formatted_level}] {basename(frame.f_code.co_filename)}.{frame.f_code.co_name}:{str(frame.f_lineno)} {msg}"

    return formatted_msg


class MyLog:
    def __init__(self, log_file_path='', deep=1, con='-'):
        self.log_file_path = log_file_path
        self.logger = logger_
        self.logger.remove()  # 默认
        self._deep = deep
        self._con = con
        self.logger.add(sys.stdout,
                        format="{message}",  # 日志内容
                        )
        if self.log_file_path:
            self.logger.add(self.log_file_path,
                            format='{message}',  # 模块名.方法名:行号
                            rotation="10 MB")

    def base_log(self, msg_type, *args):
        _msg = self._con.join([str(i) for i in args])
        formatted_msg = formatted_mob_msg(
            _msg,
            msg_type, get_frame(self._deep)
        )
        self.logger.log(msg_type, formatted_msg)

    def info(self, *args):
        _msg = self._con.join([str(i) for i in args])
        formatted_msg = formatted_mob_msg(
            _msg,
            "INFO", get_frame(self._deep)
        )
        self.logger.log("INFO", formatted_msg)

    def error(self, *args):
        _msg = self._con.join([str(i) for i in args])
        formatted_msg = formatted_mob_msg(
            _msg,
            "ERROR", get_frame(self._deep)
        )
        self.logger.log("ERROR", formatted_msg)

    def critical(self, *args):
        _msg = self._con.join([str(i) for i in args])
        formatted_msg = formatted_mob_msg(
            _msg,
            "CRITICAL", get_frame(self._deep)
        )
        self.logger.log("CRITICAL", formatted_msg)

    def debug(self, *args):
        _msg = self._con.join([str(i) for i in args])
        formatted_msg = formatted_mob_msg(
            _msg,
            "DEBUG", get_frame(self._deep)
        )
        self.logger.log("DEBUG", formatted_msg)

    def warning(self, *args):
        _msg = self._con.join([str(i) for i in args])
        formatted_msg = formatted_mob_msg(
            _msg,
            "WARNING", get_frame(self._deep)
        )
        self.logger.log("WARNING", formatted_msg)


if __name__ == '__main__':
    logger = MyLog()
    logger.info('aaaa')
    logger.error('aaaa', 'track_id', 'parent_id')
    logger.debug('aaaa', 'track_id', 'parent_id')
