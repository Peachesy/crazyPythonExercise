import  math
#单行注释  快捷键：Ctrl+/
"""
多行注释
啦啦啦啦啦
"""
'''
多行注释
balbalbalba
'''
#
# print("Hello World!!!:D")
# print(math.sin(2))
# a='98709yuyiudididi'
# print(type(a))
# name="Charlie Smith"
# age=26
# # print默认用空格分隔输出内容，参数sep='|'表示用|对输出的内容进行分隔
# # print函数中end参数的默认值就是\n，即回车换行
# print("姓名：",name,"年龄：",age,end='\n')
# print("姓名：",name,"年龄：",age,sep='|')
#
# # print函数的file参数，默认值为sys.stdout，即系统标准输出，默认将结果输出到屏幕
# f=open("poem.txt","w") # 打开文件写入
# print("沧海月明珠有泪",file=f)
# print("蓝田玉暖日生烟",file=f)
# f.close()
#
# # 数值中可以使用下划线
# c=123_7895_520
# print(c)
#
#
# b=None
# print(b)
#
# # python中，51200是整形，512E2是浮点型，只有浮点型才能用科学计数法表示
# d=51200
# e=512e2
# print(d,type(d))
# print(e,type(e))
# # 当字符串中包含了引号，则用不同的引号将其括起来，或者对引号进行转义
# str1="I'm a coder"
# str2='I\'m a coder'
# print(str1)
# print(str2)
#
# # 将数值转换为字符串，两个函数 str()和repr（）
# # repr()函数对字符串处理后，再print，输出结果是python的表达式形式
# str3="这本书的价格是："
# p=99.8
# print(str3)
# print(repr(str3))
# print(repr(p))
# print(str3+str(p))
# print(str3+repr(p))
#
# # 长字符串
# lstr='''"Let's go fishing",said Mary.
# "OK,Let's go",said her brother.
# They walked to a lake.'''
# print(lstr)
# # 用转义字符对换行符进行转义，输出效果：还是一行，只是在书写代码的时候不让输入的回车中断字符串
# lstr2='The quick brown fox \
# jumps over the lazy dog'
# print(lstr2)
# # 原始字符串r'C:\balabala\balabala'
# # 效果等同于C:\\balabala\\balabala
# # 如果原始字符串中包含反斜杠，则反斜杠会变成字符串的一部分

# 字节串
b1=bytes() #创建一个空的字节串
b2=b'' #创建一个空的bytes值
b3=b'Hello' #通过b前缀指定Hello是bytes类型的值
print(b1)
print(b2)
print(b3)
print(b3[0])
print(b3[2:4])
b4=bytes('我爱python编程',encoding='UTF-8') # 调用bytes方法将字符串转换为bytes对象
print(b4)
b5='学习python很有趣'.encode('utf-8') # 利用字符串的encode方法编码成bytes，默认使用utf-8字符集
print(b5)

s='  This is a puppy '
print(s.lstrip())
print(s.strip())
print(s)

str='ABCDCDC'
print(str.count('CDC'))

