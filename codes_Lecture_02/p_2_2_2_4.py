# 参数传递示例4 任意数目关键字参数示例


def build_profile(first, last, **user_info):
    """ 构建包含用户信息的字典 """
    profile = {'first_name': first, 'last_name': last}
    profile.update(user_info)   # 将字典user_info的内容添加到字典profile
    return profile


user = build_profile('Harry', 'Potter', location='Hogwarts', field='Wizarding')
print(user)

