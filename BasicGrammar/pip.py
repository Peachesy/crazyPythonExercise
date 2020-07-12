# 管道，将上一个命令的输出作为第二个命令的输入
# 语法 pip1 | pip2 | pip3
# 即执行完pip1后的输出作为pip2的输入继续执行命令，然后把pip2命令的输出作为pip3命令的输入

# 实例：获取javac命令有module的行

import sys

# sys.stdin是标准输入，即键盘
# 执行该程序时，只需在命令行中输入javac | python pip.py --没有安装Java
# 实际执行： python -h | pip.py
for line in sys.stdin:
    if "debug" in line:
        print(line,end="")

print("Finished!")
