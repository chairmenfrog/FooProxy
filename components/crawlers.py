# coding:utf-8
"""
    @author  : linkin
    @email   : yooleak@outlook.com
    @date    : 2018-10-04
"""
import logging
import re

from bs4 import BeautifulSoup        as bs

from const.settings import _66ip_params
from const.settings import builtin_crawl_urls   as _urls
from const.settings import headers
from tools.util import base64_decode
from tools.util import get_cookies
from tools.util import get_nyloner_params

logger = logging.getLogger('Collector')


def ip66():
    """
    内置的IP代理采集爬虫,必须添加到下方的builtin_crawlers中才会生效
    :return: 采集到的代理IP数据,list类型 ['<ip>:<port>',..]
    """
    s = requests.Session()
    url = _urls['66ip']['url']
    try:
        response = s.get(url, headers=headers, params=_66ip_params)
        soup = bs(response.text, 'lxml')
    except Exception as e:
        logger.error('Error class : %s , msg : %s ' % (e.__class__, e))
    else:
        data = [re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b\:\d+', i)
                for i in soup.body.text.split('\r\n') if i.strip()]
        data = [i[0] for i in data if i]
        data = list(set(data))
        return data


def nyloner():
    s = requests.Session()
    url = _urls['nyloner']['url']
    count = _urls['nyloner']['count']
    params = get_nyloner_params(1, count)
    try:
        cookies = get_cookies(url, headers=headers)
        __cookie = {'sessionid': cookies['sessionid']}
        response = s.get(url, headers=headers, params=params, cookies=__cookie)
    except Exception as e:
        logger.error('Error class : %s , msg : %s ' % (e.__class__, e))
    else:
        crypted_data = response.json()
        data = base64_decode(crypted_data['list'])
        res = [':'.join([i['ip'], i['port']]) for i in data]
        return res


import requests


def get_proxy():
    res = requests.get("http://127.0.0.1:5010/get_all/").json()
    useful = []
    for i in res:
        # print(i['proxy'])
        useful.append(i['proxy'])
    # res=requests.get("http://127.0.0.1:5010/get/").json() #只采集1条ip,量太小
    # return ''.join(useful)
    return useful


def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))


builtin_crawlers = [get_proxy]  # 作者内置爬虫才能加入data collectors，ｃｕｓｔｏｍ加不进去
# builtin_crawlers = [get_proxy, ]
