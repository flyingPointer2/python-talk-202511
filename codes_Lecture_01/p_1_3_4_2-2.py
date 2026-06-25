# 逻辑运算举例(2)


# 示例：判断年份是否为闰年
# 若一个年份是闰年，则该年份需至少满足下述两个条件中的一个：（or）
#   - 条件1：年份可以被400整除
#   - 条件2：年份能被4整除，但是不能被100整除（and）

year = 1900
condition_1 = year % 400 == 0
condition_2 = year % 4 == 0 and year % 100 != 0
is_gap_year = condition_1 or condition_2

print(year, " 是否为闰年？ ", is_gap_year) # False

