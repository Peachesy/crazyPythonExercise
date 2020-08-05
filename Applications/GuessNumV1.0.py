# 猜数小程序v1.0，用户输入猜数范围，系统自动生成一个目标数goal，
# 然后提示游戏开始，每次用户输入所猜的数guess之后，都要与goal进行比较
# 比goal大的话提示用户：猜大了，目标范围在（a, guess）
# 比goal小的话提示用户：猜小了，目标范围在（guess, b)
# 与goal相等的话提示用户：猜数成功！
# 每次猜完之后更新范围a, b

import random

print("请输入一个范围，从a到b")
a = int(input("a="))
b = int(input("b="))

goal = random.randint(a, b)
print(goal)

print("猜数开始")

# 定义一个列表储存用户猜的数字
guess = []
# 用count来记录用户猜数轮数
count = 1
length = int(b-a)
print(range(length))
for i in range(length):
    guess.append(int(input("请猜数：")))
    if guess[i] > goal:
        b = guess[i]
        print("猜大了，范围在：%d, %d" % (a, b))
        count = count + 1
    if guess[i] < goal:
        a = guess[i]
        print("猜小了，范围在：%d, %d" % (a, b))
        count = count + 1
    if guess[i] == goal:
        print("恭喜猜数成功！")
        break
print(guess)
print(count)


