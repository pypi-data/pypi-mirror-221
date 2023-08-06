# encoding: utf-8
from setuptools import find_packages
from distutils.core import setup
import io

# setup(
#     name='zerocap_rest_client',
#     version='0.1',
#     # packages = find_packages(),
#     py_modules=['zerocap_rest_client']      # py 文件
# )

REQUIRED = [
    'requests',
    'json',
    'hmac',
    'hashlib'
]

with open("README.rst", "r", encoding="utf-8") as f:
  long_description = f.read()

setup(
    name="rest_zerocap_client", # 用自己的名替换其中的YOUR_USERNAME_
    version="0.0.4",    #包版本号，便于维护版本
    author="Tkon",    #作者，可以写自己的姓名
    author_email="1741226849@qq.com",    #作者联系方式，可写自己的邮箱地址
    description="Order Operation",#包的简述
    long_description=long_description,    #包的详细介绍，一般在README.md文件内
    url="",    #自己项目地址，比如github的项目地址
    install_requires=REQUIRED,
    packages=find_packages(),
    platforms=["all"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',    #对python的最低版本要求
)