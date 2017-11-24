# -*- coding: utf-8 -*-

# 条件判断
age = 20

# 根据Python的缩进规则，执行代码块
if age >= 28:
	print('大于27岁')
	print('条件判断内')

if age >= 28:
	print('大于27岁')
print('条件判断外')

# 以上两段代码，最后一个打印语句缩进不同，执行结果不同

if age >= 20:
	print('大于20岁')
elif age >= 30:
	print('大于30岁')
else:
	print('未成年')

# 练习
height = 1.75 #身高
weight = 80.5 #体重

bmi = weight / (height * height)

if bmi < 18.5:
	print('过轻')
elif bmi < 25:
	print('正常')
elif bmi < 28:
	print('过重')
elif bmi < 32:
	print('肥胖')
else:
	print('严重肥胖')
	