# TornadoWX   微信机器人。

TornadoWX 是用python的web框架tornadoWeb开发的，专门为微信公众帐号提供开发者后台。

将提供sinaAppEngine GoogleAppEngine BaiduAppEngine 以及直接运行在vps上面的4个不同版本分支。

>目前刚提交vps版的分支。


## vps安装需求
使用到的框架
* TornadoWeb
使用到的模块
* import json
* import lxml
* import redis


## 安装步骤
步骤 1: 部署 TornadoWeb:

	wget https://pypi.python.org/packages/source/t/tornado/tornado-3.0.1.tar.gz
	tar xvzf tornado-3.0.1.tar.gz
	cd tornado-3.0.1
	python setup.py build
	sudo python setup.py install

步骤 2: 部署 Redis:

	wget http://redis.googlecode.com/files/redis-2.6.13.tar.gz
	tar xzf redis-2.6.13.tar.gz
	cd redis-2.6.13
	make
    
步骤 3: 安装 Redis的Python模块:

	wget https://pypi.python.org/packages/source/r/redis/redis-2.7.5.tar.gz
	tar xvzf redis-2.7.5.tar.gz
	cd redis-2.7.5
	python setup.py build
	sudo python setup.py install

步骤 4: 运行代码:
>cd TornadoWX
>python index.py

## 配置文件

config.py是缺省的配置文件
‘WXPassword’是登录密码

1,‘WXPassword’是登录密码，配置自己的密码如下：
	import hashlib
	hashlib.sha1('123456').hexdigest()
	'7c4a8d09ca3762af61e59520943dc26494f8941b'

2,填写到公众帐号的‘token’和‘url’,可以自行修改
>WeixinToken = '654321'
>WeixinUrl='''/1984'''

3,‘smdmy’自动回复的信息。
