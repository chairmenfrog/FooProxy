# coding:utf-8

"""
    @author  : linkin
    @email   : yooleak@outlook.com
    @date    : 2018-10-04
"""
import requests


def some_crawler_func():
    """
    自己定义的一个采集爬虫
    约定：
        1.无参数传入
        2.返回格式是：['<ip>:<port>','<ip>:<port>',...]
        3.写完把函数名加入下面的my_crawlers列表中，如
          my_crawlers = [some_crawler_func,...]
    """
    pass


def get_proxy():
    res = requests.get("http://127.0.0.1:5010/get_all/").json()
    useful = []
    for i in res:
        # print(i['proxy'])
        useful.append(i['proxy'])
    # res=requests.get("http://127.0.0.1:5010/get/").json() #只采集1条ip,量太小
    # return ''.join(useful)
    return useful


my_crawlers = [get_proxy()]
# print('\n\n') #调试查看有无引号用打
print(my_crawlers)
