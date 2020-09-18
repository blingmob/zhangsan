"""
print("hello，world!") #字符串 /str
print(232323) #整数 /int
print(2.22222) #小数 /float
print(True) #布尔值 /bool
print(()) #元组 /tuple
print([]) #数组 /list
print({}) #字典 #号为单行注释，多行注释，注释内容用三对引号包起来 /dict
空/nonetype /none
len()  #计算括号内的字符串的长度，只支持字符串和元组数组字典


多行注释，用三对引号包起来
print 为打印的意思，若是要打印多行内容，可直接在内容里里面用逗号隔开

print("字符串",222,2.33)
print("字符串1"+"字符串2") #字符串的拼接 只能相同的数据类型进行操作
print("字符串"*100) #进行重复生成内容

python的运算符：+ - * / %
逻辑符号 ：and or ==(等于) !=(不等于)

print(1+2) #计算内容（运用运算符）
print(((100+20)*5)/2) #进行计算内容

#布尔值 true false
print(1>2) #进行判断，用到布尔值

#变量 赋值
t = "token" #将token这个值赋值给了名字叫t的这个变量
print(t)
# input 基于变量和赋值的基础上
"""
# 对结果数据格式进行转换
#input 的特点：只要通过input获取的不管是什么类型，对于代码来说都是字符串
# a = float(input("请输入a的赋值内容："))
# b = float(input("请输入b的赋值内容："))
# print("input获取的内容：",a+b)      #字符串是拼接



# 数据格式的转换 type()-----type为读取括号里内容的格式
#print(type(233))
#c = type(233)
#print(c)
# print(type("字符串"))
# print(type(2222))
# print(type(2.333))
# print(type(True))
# print(type(()))
# print(type([]))
# print(type({}))

# 数据的转换规律 
# 任何数据都可以转换为字符串；除了空 nonetype
# 整数和小数可以互相转换；
# 字符串转换为其他类型的数据，必须满足【长得像】的规律；

# 计算对象目标的长度，只针对字符串或元组数组及字典
# a = "啦啦啦啦啦啦"
# print(len(a))

# a = input("请输入a的内容：")
# b = input("请输入b的内容：")
# print("input获取的内容：",len(a+b))

a = input("请输入a的内容：")
b = input("请输入b的内容：")
print("input获取的两段内容之和：",len(a+b))





