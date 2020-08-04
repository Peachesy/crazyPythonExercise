# 猜数小程序v1.0，用户输入猜数范围，系统自动生成一个目标数goal，
# 然后提示游戏开始，每次用户输入所猜的数guess之后，都要与goal进行比较
# 比goal大的话提示用户：猜大了，目标范围在（a, guess）
# 比goal小的话提示用户：猜小了，目标范围在（guess, b)
# 与goal相等的话提示用户：猜数成功！
import random

print("请输入一个范围，从a到b")
a = int(input("a="))
b = int(input("b="))

goal = random.randint(a, b)
print(goal)

print("猜数开始")

# 用count来记录用户猜数轮数
length  = int(b-a)
for i in range(length):
    guess = int(input("请猜数："))
    if guess > goal:
        print("猜大了，范围在：，" % a, guess)
        count = count+1
    if guess < goal:
        print("猜小了，范围在：，" % guess, b)
        count = count + 1
    if guess == goal:
        print("恭喜猜数成功！")
        break



