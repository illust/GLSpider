#!/usr/bin/env python
#-*- coding:utf-8 -*-
import optparse
import scrapy.cmdline as cmd
import os
from os import path
import shutil
import json
from datetime import datetime

def test():
    usage = "glspider [options] [args]"
    parser = optparse.OptionParser(usage,description='GLSpider v1.0\t©Copyright 2018, GeeLink Inc.')
    parser.add_option("-c","--cmdfile",dest="cmdfile",help="please specify the absolute path of configuration file ",type="string")
      
    options,args=parser.parse_args()

    # if options.runspider == "spider":
    #     cmd.execute('scrapy crawl spider'.split())
            
    if options.cmdfile:
        # print(options.cmdfile)
        # config.set_cmdfile(options.cmdfile)
        # shutil.copy(options.cmdfile,os.path.abspath('.'))
        cmd.execute('scrapy crawl spider'.split())


if __name__ == '__main__':
    test()