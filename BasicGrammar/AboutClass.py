
class Book:
    var_one = "one"
    var_two = "two"
    var_three = "three"
    print("This is a class named book")
    print("Welcome!")
    print("Do all the print-function execute?")


# python是动态语言，可以在任意地方为类增加或删除实例变量
# 增加
Book.test = "balabala"
del Book.var_two
print("test:", Book.test)
print("test:", Book.var_one)
# print("test:", Book.var_two)


# 在类外新增一个方法，改方法不会自动传入self参数，需要手动传入
def fun(self):
    print("类外的方法fun")
    return "fun"


b = Book()
b.nfun = fun
b.nfun(b)
# 另一种在类外增加方法的方式，用methodtype方法来进行包装
from types import MethodType
b.nfun1 = MethodType(fun, b) # 把函数fun包装成类Book的方法nfun1,且b自动绑定第一个参数
# 调用nfun1方法
b.nfun1()

# 方法中的self总是代表该方法的调用者




