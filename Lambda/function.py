import random

def test(a,*b,**c):
    print("a::",a)
    print("b::",b)
    print("c::",c)

test(223,'iouoidjf','joinon',q=1,m=0)

# 逆向参数收集
# 将元祖、列表、字典作为参数传给函数
tup=(23,46,7878)
list=[45,'ppp','ooo','Y']
dict={'a':'q','b':3,'c':'vv'}
test(tup)  # 元祖作为一个整体，传到函数中
test(*tup)
# 加*后，元祖自动解包，作为三个参数传入，因为关键字参数收集必须符合字典的key-value对的方式，所以后两个元素46,7878
# 又被封包传入参数b，列表亦如此
test(dict)  # 字典作为整体传入
test(**dict) # 字典解包后，自动传入key对应的value值

