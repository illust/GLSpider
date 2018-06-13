#coding:utf8
from setuptools import setup,find_packages
 
setup(
    name='GLSpider',      # 应用名
    version='1.0',        # 版本号
    packages=find_packages(),    # 包括在安装包内的Python包
    include_package_data=True, # 启用清单文件MANIFEST.in
    exclude_package_data={'GLSpider':['.pyc']}, # 将所有.pyc文件排除在包外
    # dependency_links=['https://github.com/illust/scrapy/tarball/master#egg=package-1.0'],
    zip_safe=False,
    entry_points={
        'console_scripts':['glspider = GLSpider:test'],
        }
)