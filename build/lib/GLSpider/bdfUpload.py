# -*- coding: utf-8 -*-

import json
import sys
import requests

# try:
#     if sys.argv[1].startswith("--cmdfile="):
#         try:
#             with open(sys.argv[1].split("=")[1]) as f:
#                 settings = json.load(f)
#         except json.JSONDecodeError:
#             print("Configure Errors: some fields of the configure file expecting value!")
#     elif sys.argv[1] == "-c":
#         try:
#             with open(sys.argv[2]) as f:
#                 settings = json.load(f)
#         except json.JSONDecodeError:
#             print("Some Errors: some fields of the configure file expecting value!")
#
# except ValueError:
#     print("Command Errors: input command is wrong!")
#
# # bdf存储路径
# if 'COLLECTION' in settings:
#     COLLECTION = settings['COLLECTION']
# else:
#     COLLECTION = ""

doclst = []

with open("/home/sven/project/work/data/20180518_091045/bdf/51cto.json") as file:
    for line in file.readlines():
        doclst.append(json.loads(line))

headers = {'Content-Type': 'application/json', 't': '8D839EB9C4765ACEEB1EDCBAF8D44031'}
data = {
                'collectionName': 'spider',
                'docList': doclst,
                'local': 'false',
                'uid': 'geelink'
        }
r = requests.put("http://39.106.1.50:9090/v1/api/ume/put", headers=headers, json = data)
print(r.text)