# HYJ
# TIME: 2021-8-2 11:09

import os
import shutil
count1 = []
count2 = []


def move(files, path):
    for file in files:  # 遍历文件夹
        if os.path.isdir(path+"/"+file):  # 判断是否是文件夹，是文件夹才打开
            path_add = path + "/" + file
            files = os.listdir(path_add)
            move(files, path_add)
            count1.append(1)
        else:
            if file.endswith(".mp4"):
                path = path + "/" + file
                try:
                    shutil.move(path, 'D:/下载/视频')
                    print("move {0}".format(file))
                    count2.append(1)
                except:
                    pass


path = "D:/下载/视频"  # 文件夹目录
files = os.listdir(path)  # 得到文件夹下的所有文件名称
move(files, path)
print(sum(count1), "\n", sum(count2))
