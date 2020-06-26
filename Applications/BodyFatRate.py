# 体脂率计算公式：
# BMI=体重（kg）/ [身高(m)的平方]
# 体脂率=1.39*BMI+0.16*年龄-10.34*性别-9    女性性别值为0，男性为1

# def BodyFatRate(self):
#     print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
#     age = input("请输入年龄：")
#     height = input("请输入身高，单位为米：")
#     weight = input("请输入体重，单位为千克")
#     gender = input("请输入性别：")
#     if gender == "男":
#         gendernum = 1
#     else:
#         gendernum = 0
#     BMInum = weight/(height*height)
#     BFRnum = 1.39 * BMInum + 0.16 * age - 10.34 * gendernum - 9
#     print("体脂率为：%f", BFRnum)
#

print("--------------粗略估算体脂率------------------")
age = int(input("请输入年龄："))
height = float(input("请输入身高，单位为米："))
weight = float(input("请输入体重，单位为千克："))
gender = input("请输入性别：")
if gender == "男":
    gendernum = 1
else:
    gendernum = 0
BMInum = weight/(height*height)
BFRnum = 1.39 * BMInum + 0.16 * age - 10.34 * gendernum - 9
print("体脂率为：", BFRnum)

