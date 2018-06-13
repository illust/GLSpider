# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.utils.project import get_project_settings
import os
import json
import requests
from datetime import datetime

from scrapy import signals
from pydispatch import dispatcher

class fileWriterPipeline(object):

    def open_spider(self,spider):
        settings = get_project_settings()
        self.folder = settings.get('COLLECTION')

        # 若self.folder为空字符，表示数据存储在程序运行磁盘的根目录下的data子目录中
        self.datafolder = self.folder + "data"
        
        if not os.path.exists(self.datafolder):
        # 如果不存在则创建保存data文件的目录
            os.makedirs(self.datafolder)
            
        self.timefolder = self.datafolder +'/' + datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if not os.path.exists(self.timefolder):
        # 如果不存在则创建当前时间戳文件目录
            os.makedirs(self.timefolder)
            
        self.bdffolder = self.timefolder + "/bdf"
        if not os.path.exists(self.bdffolder):
        # 如果不存在则创建保存bdf文件的目录
            os.makedirs(self.bdffolder)  
            
        self.htmlfolder = self.timefolder + "/html"
        if not os.path.exists(self.htmlfolder):
        # 如果不存在则创建保存html文件的目录
            os.makedirs(self.htmlfolder)    
            
        name = settings.get('FILENAME')
        self.file = open('%s/%s.json'%(self.bdffolder,name),'w')

    def close_spider(self,spider):
        self.file.close()

    def process_item(self,item,spider):

        # 保存bdf
        line = json.dumps(item,ensure_ascii=False) + "\n"
        self.file.write(line)
        
        # 保存html文件
        file_name = item['collkey']
        url = "http://" + ("/").join(file_name.split("-"))
        print(url)
        r = requests.get(url)

        if file_name.endswith("html") or file_name.endswith("htm"):
            pass
        else:
            file_name = file_name + ".html"
        with open('%s/%s' % (self.htmlfolder,file_name), 'w+b') as f:
            f.write(r.content)
        return item

class bdfUploaderPipeline(object):

    def open_spider(self,spider):
        settings = get_project_settings()
        self.T = settings.get("T")
        self.headers = {'Content-Type': 'application/json', 't': '8D839EB9C4765ACEEB1EDCBAF8D44031'}

    def process_item(self,item,spider):

        data = {
                'collectionName': 'spider',
                'docList': [item],
                'local': 'false',
                'uid': 'geelink'
        }
        r = requests.put("http://39.106.1.50:9090/v1/api/ume/put", headers=self.headers, json = data)
        print(r.text)