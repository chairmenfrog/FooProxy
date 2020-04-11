# coding:utf-8

"""
    @author  : linkin
    @email   : yooleak@outlook.com
    @date    : 2018-10-04
"""
import logging.config

from components.workstation import Workstation
from const.settings import LOG_CONF

logging.config.fileConfig(LOG_CONF)

if __name__ == '__main__':
    workstation = Workstation()
    workstation.work()
