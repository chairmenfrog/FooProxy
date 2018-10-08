# FooProxy
稳健高效的评分制 IP代理池 + API服务提供，可以自己插入采集器进行代理IP的爬取，支持 MongoDB 4.0 使用 Python3.7 
## 背景
 因为平时爬取某些网站数据时，经常被封IP，同时网上很多的接口又不方便，免费的也少，稳定的更少，所以自己写了一个评分制的ip代理API进行爬虫的供给
 起初对MySQL和MongoDB进行了兼容的编写，后来发现在高并发的情况下，MySQL并不能很好的读写数据，经常莫名其妙的出现死机、读写巨慢、缓执行等各种奇
 葩现象，对比MongoDB高效的数据文档读写，最终还是放弃了mysql的兼容。*(dev分支保留了对mysql的部分支持，如爬取评分)*


## 基本流程
整个项目的流程其实很简单
* 采集数据
* 验证数据
* 打分存储
* 循环检测
* 择优剔劣
* API调用
流程图：


