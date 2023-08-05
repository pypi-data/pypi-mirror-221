"""
- author:Auorui(夏天是冰红茶)
- creation time:2022.10
- pyzjr is the Codebase accumulated by my python programming.
  At present, it is only for my personal use. If you want to
  use it, please contact me. Here are my email and WeChat.
- WeChat: z15583909992
- Email: zjricetea@gmail.com
- Note: Currently still being updated, please refer to the latest version for any changes that may occur
"""

import codecs
import os
from setuptools import setup, find_packages

# these things are needed for the README.md show on pypi (if you don't need delete it)
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

# you need to change all these
VERSION = '1.0.0'
DESCRIPTION = 'foxpay sdk for python version'
LONG_DESCRIPTION = 'foxpay sdk for python version'

setup(
    name="FoxPay",
    version=VERSION,
    author="Lin",
    author_email='404885236@qq.com',
    url='https://github.com/KamenSoftware/foxpay-sdk-python',
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    license='Apache License',
    install_requires=[],
    keywords=['python', 'foxpay-sdk', 'Lin','wallet'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows",
    ]
)

