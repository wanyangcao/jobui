# jobui
爬取网站数据，结果写入mysql

目的：从网上获取不同地区不同职位的平均收入，目前我只爬了全国各地区的平均收入，
至于不同地区不同职位的平均工资今后再补充。

方法：主要用到scrapy框架，一个是因为使用比较方便，另外一个是结构清晰结果易于存储，我最终把结果
写入了mysql,具体细节可以参考scrapy文档:http://scrapy-chs.readthedocs.org/zh_CN/0.24/.



