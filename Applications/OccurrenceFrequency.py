# 用户输入一个字符串和一个子串，打印出给定子串在目标字符串中出现的次数
# 如，ABCDCDC和CDC，输出结果为2

str=input("请输入字符串：")
s=input("请输入子串：")
num=0
for i in range(len(str)):
    temp=str[i:i+3]
    if s in temp:
        num+=1
print(num)



