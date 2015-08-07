#!/usr/bin/env python

from distutils.core import setup

setup(name='PypeR',
	version='1.1.2',
	description='Call R in Python by pipe',
	author='Xiao-Qin Xia',
	author_email='xqxia70@gmail.com',
	url='http://bioinfo.ihb.ac.cn/softwares/PypeR/',
	#packages=['bin'], # copy to site-packages
	#scripts=['Rinpy.py'], # copy to /usr/bin
	py_modules=['pyper'], # copy to site-packages
	)

