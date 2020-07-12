# with语句可以用来管理资源关闭
# 比如把打开的文件放到with语句中，他可以帮助自动关闭文件

# 使用with语句管理的资源必须时一个实现上下文管理协议的类（context manage protocol），必须实现以下两个方法：
# context_manager.__enter__():进入上下文管理器自动调用的方法
# context_manager.__exit__(exc_type,exc_value,exc_traceback)：退出上下文管理器自动调用的方法
# exc_type,异常类型
# exc_value,异常的值
# exc_traceback,异常的traceback

# with open("with_test.py",'r',True,'UTF-8') as f:
#     for line in f:
#         print(line,end="")
# print("success!")

class FkResource:
    def __init__(self, tag):
        self.tag = tag

    def __enter__(self):
        print("该资源的tag：",self.tag)
        return "Hey,man,what/'s up"

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb:
            print("因为异常，关闭资源")
        else:
            print("程序正常结束，关闭资源")

# 使用with
with FkResource('Not much') as fk:
    print("fk为：",fk)
    print("---before---")
    # raise  Exception(20, '自定义异常')
    print("---after---")

'''
程序的执行结果：
该资源的tag： Not much
fk为： Hey,man,what/'s up
---before---
---after---
程序正常结束，关闭资源

执行顺序：先执行类FkResource的__init__构造函数，然后将Not much作为参数传给构造函数的tag变量，
接着执行__enter__函数，返回Hey,man,what/'s up
然后将__enter__的输出即返回值Hey,man,what/'s up作为输入（参数）赋值给fk
最后执行with的语句块，打印Hey,man,what/'s up，before，after
'''



