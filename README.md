# ume-spider项目——GLSpider使用指南  

## 一、环境搭建
glspider工具是在python3下基于流行的开源爬虫项目scrapy开发的，python版本要求**python3.4+**。  
1. 如果你的电脑上没有python开发环境，首先需要进行环境安装，推荐使用Anaconda3，它是一个开源的python发行版本，内置了很多直接使用的工具包，方便快捷。Anaconda3的安装操作，可以直接到[官网](https://www.anaconda.com/download/)选择对应的操作系统下的图形安装包手动进行安装。  
下面三个链接分别为Anaconda官网上针对Windows、Liunx和MacOS的安装教程：  
- [Windows](https://docs.anaconda.com/anaconda/install/windows)
- [Liunx](https://docs.anaconda.com/anaconda/install/linux)
- [MacOS](https://docs.anaconda.com/anaconda/install/mac-os#macos-graphical-install)  

再给出一个Windows用户的Anaconda安装的[中文博客](https://blog.csdn.net/u012318074/article/details/77075209)，其他两个平台安装过程类似，不再赘述。  
*验证安装结果*：命令行输入``conda list``，如果Anaconda安装成功，则会显示所有的工具包及版本号。  
2. 安装好Anaconda3之后，再利用命令工具conda进行scrapy的安装。  
```python
conda install scrapy
```
**注意**：也可以不选择安装Anaconda3，但是需要有python3环境，再利用pip工具安装scrapy。
```python
pip3 install scrapy
```
*验证安装结果*：命令行输入``scrapy``，如果scrapy安装成功，则显示其版本号和可用的命令操作。  
至此，项目运行环境搭建完成。  

## 二、GLSpider工具安装  
1. 利用git工具克隆此项目：
```git
git clone https://gitee.com/cracker2017/umm-spider.git
```
2. 工具打包：  
进入umm-spider/GLSpider目录下，执行以下两条命令：
```python
python setup.py bdist_egg 
python setup.py install
```
如果可以使用shell，则可以直接键入以下命令打包：
```bash
sh packiage.sh
```
*验证安装结果*：在当前目录下，命令行输入``glspider -h``，出现glspider工具的版本号，则表示安装成功。  

## 三、工具使用
1. QuickStart
想要快速体验爬虫效果，可以键入以下命令，直接使用样例配置文件进行测试爬取。  
```
glspider -c settings.json
```
2. 详细信息参见[GLSpider技术文档](https://gitee.com/cracker2017/umm-spider/raw/master/GLSpider/GLSpider_release1.0.pdf)