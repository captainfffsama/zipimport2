# 说明
参考了 python 标准库中 zipimport 源码,现在 zipimport2 支持加密 zip 包导入,并支持对 zip 包密码进行加密

# 安装方式
安装 Cython:
```python
pip install Cython
pip install .
```

# 使用方式
假设你写了一个非常碉堡的包,比如叫`iamsohandsome.py`,其内容大概如下:
```python
class IAmYourDaddy:
    def __init__(self):
        print("daddy coming")
```
然后我们想加密这个包,密码使用`daddycoming`,则可以执行以下命令:
```shell
zip -P daddycoming -r d.zip iamsohandsome.py
```

得到一个`d.zip`,这个压缩包中包含了你的包中的所有文件.
然后我们使用以下代码把明文密码`daddycoming`加密:
```python
from zipimport2 import encrypt
print(encrypt("daddycoming"))
```
得到以下输出:
```shell
>>> >393>3>3.47333531343;3
```
这里 `>393>3>3.47333531343;3` 就是加密之后的密码.

然后加加密之后密码和加密zip包发给老王,老王在自己的代码中想要引入这个加密的包,可以使用如下方式:
```python
from zipimport2 import zipimporter
zip_path="~/d.zip"
pwd=">393>3>3.47333531343;3"
# 若使用加密的密码,那么zipimporter 位置2的参数就用 True
i=zipimporter(zip_path+'@'+pwd,True)
# 这里 m 就是加载进来的 iamsohandsome 模块
m=i.load_module("iamsohandsome")
# 加载进来之后就可以使用包里面的方法和类
m.IAmYourDaddy()
```
可以得到以下输出:
```shell
>>> daddy coming
```

# API 说明
- `zipimporter.__init__(self, path, pwd_encry=False)`
总体和原始标准库差不多,就是新增一个 pwd_encry 指示用的是明文密码还是加密密码

- `encrypt(pwd:str)`
用来帮助用户加密zip包的密码



