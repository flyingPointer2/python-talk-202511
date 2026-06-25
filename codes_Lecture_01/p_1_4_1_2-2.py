# 列表的常用方法举例(2)

names = ['喜羊羊', '美羊羊', '懒羊羊', '沸羊羊', '红太狼', '灰太狼']

# 删除元素

the_pop_element = names.pop()
print("被弹出的元素是：", the_pop_element)
print(names)

names.remove('红太狼')
print(names)
