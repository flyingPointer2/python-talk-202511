# json格式文件的读写示例2 读取json文件

import json

json_file_path = 'data/acta-psychologica-sinica-data.json'

with open(json_file_path,'r',encoding='utf-8') as f:
    data = json.load(f)

print(type(data),type(data[0]))
print(data[0])
