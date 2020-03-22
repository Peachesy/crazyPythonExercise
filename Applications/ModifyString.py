# 输入一个字符串，修改该字符串中哪个位置的字符，程序输出修改后结果，如输入：
# ‘fkjava.org’
# 6 -
# 输出：fkjava-org

originalStr=input("请输入原始字符串")
posi=input("请输入修改的位置（字符串位置从0开始计算）")
newStr=input("请输入新的字符")


for i in originalStr:
    res[i]=originalStr[i]
