# json格式文件的读写示例1 字典或字典列表写入json文件

students_info = {
    2024999001:{
        '姓名':'Emily',
        '成绩':{
            '微积分':84,
            '大雾':77,
            '小雾':71
        }
    },
    2024999002:{
        '姓名':'Jacob',
        '成绩':{
            '微积分':92,
            '大雾':77,
            '小雾':78
        }
    }
}

import json

json_file_path = "data/students_info.json"

with open(json_file_path,"w",encoding='utf-8') as f:
    # json.dump(students_info, f)
    json.dump(students_info, f, indent=4, ensure_ascii=False)

