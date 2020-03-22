import datetime
import random
import string

my_list1=[12,34,56,78,90]
my_list2=[23,45,67,89,10,-98]
sum_list=my_list1+my_list2
print(sum_list)
my_tuple1=(23,78,342,2342,23)
my_tuple2=(-19,-8342,'0983',3287,'v587')
print(my_tuple1+my_tuple2)

# # 为元素增加表示日期的后缀
# order_endings=('st','nd','rd')+('th',)*17+('st','nd','rd')+('th',)*7+('st',)
# print(order_endings)
# day=input("输入日期(1-31)：")
# day_int=int(day) # 把字符串转成整型
# print(day+order_endings[day_int-1])

# 应用max、min函数比较大小的时候，要求列表或元祖中的每个元素是同一种类型的
# range函数：range(start,stop,step)，从start开始计数到stop停止，步长为step，创建一个整数列表，多用在for中
new_tuple=tuple(my_list2)
print("new_tuple is:",new_tuple) # 将列表转换为元祖
a=tuple(range(1,10,2))
print("打印a:",a)
*begin,last=a # *begin表示一序列（可以是列表或元祖）
print(begin,last)
# 将元祖转换为列表
a_list=list(a)
print(a_list)
a_range=range(1,5) # 将一个区间对象转换为列表
print(a_range)
b_list=list(a_range)
print(b_list)

# 用append为列表追加元素，可以追加单个元素、列表和元祖，内容会被当做一个元素追加到列表中
b_list.append('ojbk')
print(b_list)
b_list.append(a)
print(b_list)
b_list.append(my_list2)
print(b_list)
b_list.append(['a','ui'])
print(b_list)

# 用extend为列表追加元素，追加的内容不会被当做一个整体放到列表的元素中，而是被打散，每个元素被追加到列表的每个元素中
b_list.extend(('e','wer',7687))
print(b_list)
b_list.extend(my_list1)
print(b_list)
b_list.extend(range(2,6))
print(b_list)

# 插入元素insert，在指定索引位置插入元素，后面的元素依次向后移动
b_list.insert(3,'tttyyy')
print(b_list)
b_list.insert(6,('a','lalalala'))
print(b_list)

# 删除列表中的元素，可以删除单个元素，也可以删除中间一段，删除一段内容是会使用列表的slice语法，即切片函数【start,stop,step】
del b_list[2]
print(b_list)
del b_list[5:8]
print(b_list)

# del、remove、clear三者的区别：
# del根据索引来删除，可以删除列表中的一个或多个元素，也可以删除变量，变量被删除后再访问会触发nameError错误
# remove不根据索引删除元素，根据元素本身来删除元素，且只删除找到的第一个元素，若找不到该元素，会引发ValueError错误
# clear用于清空列表中的所有元素
b_list[2:2]=['ojbk']
print(b_list)
b_list[2:2]='ojbk'
print(b_list)
b_list[1:4]='ABCD'
print(b_list)

# 列表可以当做栈来使用，但python没有push方法，用append来代替
stack=[]
stack.append('qwerty')
stack.append('asdfgh')
stack.append('zxcvb')
stack.append('poijkl')
print(stack)
stack.pop()
print(stack)
print(stack.pop()) # 出栈操作会返回栈顶元素
stack.reverse() # 翻转列表中的元素
print(stack)

# 字典  元祖可以作为字典的key，但列表不能作为字典的key，因为列表可变

# str=tuple(input("请输入N个字符串："))
# print(str)
# print(str*3+('fkjava','crazyit'))

# 给定一个list，把列表中所有元素复制到另一个list中
time_stamp=datetime.datetime.now()
print(time_stamp)
ori_list=['a', 'b', 'c', 'd', 'e']
new_list=[]

# for i in range(len(ori_list)):
#     new_list[i]=ori_list[i]
# print("结果为：")
# print("结果为：",new_list)

# 用户输入一个整数N，生成长度为N的列表，将N个随机数放入
n=int(input("请输入N："))
newlist=list(range(n))
print(newlist)
# 用户输入一个整数N，生成长度为N的列表，将N个随机的奇数放入
n=int(input("请输入N："))
nnlist=[]
while len(nnlist)<n:
    a=random.randint(1,200)
    if a%2==1:
        nnlist.append(a)
print(nnlist)

# 用户输入一个整数N，生成长度为N的列表，将N个随机的大写字符放入
# 生成大写字符要导入string，然后再使用里面的ascii_uppercase方法产生大写字符
# 再用random函数的choice方法以ascii_uppercase方法产生的大写字符作为参数产生随机大写字符

n=int(input("请输入N："))
strlist=[]
while len(strlist) < n:
    s=string.ascii_uppercase
    a=random.choice(s)
    strlist.append(a)
print(strlist)
