# HYJ
# TIME: 2021-2-2 16:44
import random
# 分数
score = 0
# 游戏提示
print("WASD为移动方式;'+'代表你的当前位置,'*'代表目标位置;quit退出游戏！")
print("游戏开始！！！")
userX = random.randint(0, 9)
userY = random.randint(0, 9)
targetX = random.randint(0, 9)
targetY = random.randint(0, 9)

while True:
    for one in range(0, 10):
        xz = ""
        outStr = ""
        for two in range(0, 10):
            if userX == targetX and userY == targetY:
                targetX = random.randint(0, 9)
                targetY = random.randint(0, 9)
                score += 1
                print("当前分数:{0}".format(score))
            if userX == one and userY == two:
                xz = "+"
            elif targetX == one and targetY == two:
                xz = "*"
            else:
                xz = "-"
            outStr += xz
        print(outStr)

    # print(move)
    move = input("请移动或退出：").upper()
    x = len(move)
    if move == "QUIT":
        break
    else:
        for i in range(0, x):
            if (move[i] == "S") and userX < 9:
                userX += 1
            elif (move[i] == "W") and userX > 0:
                userX -= 1
            elif (move[i] == "D") and userY < 9:
                userY += 1
            elif (move[i] == "A") and userY > 0:
                userY -= 1
            elif (move[i] == "S") and userX == 9:
                userX = 0
            elif (move[i] == "W") and userX == 0:
                userX = 9
            elif (move[i] == "D") and userY == 9:
                userY = 0
            elif (move[i] == "A") and userY == 0:
                userY = 9


print("游戏结束，最终得分：{}".format(score))
