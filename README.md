# 测试cop 第一次作业
豆瓣公开了图书查询API，文档在[这里](http://developers.douban.com/wiki/?title=book_v2#get_book)
请尝试使用你所熟悉的语言或者API框架对该API进行**契约测试**(验证该接口：`GET  https://api.douban.com/v2/book/search`)

- 语言：[python](https://www.python.org/)
- 测试框架：[unittest](https://docs.python.org/2.7/library/unittest.html)

## how to 
- clone this repo
- cd test_douban
- install virtualenv & pip
- run `virtualenv .env && . .env/bin/activate && pip install -r requirements.txt -i http://mirrors.zte.com.cn/pypi/simple && python main.py`