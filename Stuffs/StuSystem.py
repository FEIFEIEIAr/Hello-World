# HYJ
# TIME: 2021-2-19 17:06

import os
import re

filename = 'student.txt'


def main():
    while True:
        content()
        choice = int(input('please choose what you want to do'))

        if choice == 0:
            answer = input('Do you want to quit?\t\033[0;31my/n\033[m')
            if answer == 'y':
                print('thanks for using')
                break
            else:
                continue
        elif choice == 1:
            insert()
        elif choice == 2:
            search()
        elif choice == 3:
            delete()
        elif choice == 4:
            modify()
        elif choice == 5:
            sort()
        elif choice == 6:
            number()
        elif choice == 7:
            show()


def content():
    print('\033[0;35m----------------------------------------------------------\033[m')
    print('             \033[0;33m0 退出系统')
    print('             1 录入学生信息')
    print('             2 查找学生信息')
    print('             3 删除学生信息')
    print('             4 修改学生信息')
    print('             5 得到排名')
    print('             6 显示学生人数')
    print('             7 显示所有学生信息\033[m')


def insert():
    student_list = []
    while True:
        stu_id = input('please input student\'s id')
        if len(stu_id) == 4:
            pass
        else:
            print('please try again')
            continue
        name = input('please input student\'s name')
        try:
            english = int(input('please input student\'s english grade'))
            python = int(input('please input student\'s Python grade'))
            java = int(input('please input student\'s Java grade'))
        except BaseException as e:
            print(e)
            print('something is wrong, please try again')
            continue

        student = {'stu_id': stu_id, 'name': name, 'english': english, 'python': python, 'java': java}
        student_list.append(student)

        answer = input('continue to input more information?\t\033[0;31my/n\033[m')
        if answer == 'y':
            continue
        else:
            break
    save(student_list)
    print('学生信息录入完毕')


def save(lst):
    with open(filename, 'a', encoding='UTF-8') as stu_txt:
        for item in lst:
            stu_txt.write(str(item) + '\n')


def search():
    stu_id = False
    name = False
    choose = int(input('按照ID查询请输入1，按照姓名查询请输入2：'))
    if choose == 1:
        stu_id = input('please input id:')
    elif choose == 2:
        name = input('please input name:')
    else:
        print('输入有误请重新输入')
        search()

    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            student_info = file.readlines()
    else:
        print('we do not have any information')

    for item in student_info:
        dic = dict(eval(item))
        if stu_id:
            if dic['stu_id'] == stu_id:
                show_student(dic)
        elif name:
            if dic['name'] == name:
                show_student(dic)
    answer = input('want to search for another student?\t\033[0;31my/n\033[m')
    if answer == 'y':
        search()
    else:
        return


def delete():
    while True:
        stu_id = input('please input id of the student that you want to delete')
        if stu_id:
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file1:
                    student_info = file1.readlines()
            else:
                student_info = []
            flag = False  # 标记是否删除学生

            if student_info:
                with open(filename, 'w', encoding='utf-8') as file2:
                    dic = {}
                    for item in student_info:
                        dic = dict(eval(item))
                        if dic['stu_id'] != stu_id:
                            file2.write(str(dic)+'\n')
                        else:
                            flag = True
                if flag:
                    print('已经删除ID为{0}的学生'.format(stu_id))
                else:
                    print('未能找到ID为{0}的学生'.format(stu_id))
            else:
                print('we have no information of any students')
                break
        show()  # 删除后展示现有的学生信息

        answer = input('want to delete more students?\t\033[0;31my/n\033[m')
        if answer == 'y':
            continue
        else:
            break


def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file1:
            student_info = file1.readlines()
    else:
        return
    stu_id = input('please input the ID of the student that you want to modify the information')
    with open(filename, 'w', encoding='utf-8') as file2:
        for item in student_info:
            dic = dict(eval(item))
            if dic['stu_id'] == stu_id:
                print('found the student, you can modify the information')
                while True:
                    try:
                        dic['name'] = input('please input student\'s name')
                        dic['english'] = int(input('please input student\'s english grade'))
                        dic['python'] = int(input('please input student\'s Python grade'))
                        dic['java'] = int(input('please input student\'s Java grade'))
                    except:
                        print('输入有误，重新输入')
                    else:
                        break
                file2.write(str(dic) + '\n')
            else:
                file2.write(str(dic)+'\n')
    answer = input('是否继续修改？'+'\t\033[0;31my/n\033[m')
    if answer == 'y':
        modify()


def sort():
    if os.path.exists(filename):
        show()
        with open(filename, 'r', encoding='utf-8') as file1:
            lst_student = file1.readlines()
        student_new = []
        for item in lst_student:
            char = eval(item)
            student_new.append(char)

    else:
        print('尚未保存数据')
        sort()

    flag = input('请选择，0.升序 1.降序')
    if flag == '0':
        flag = False
    elif flag == '1':
        flag = True
    else:
        print('输入有误，重新输入')
        sort()

    mode = int(input('请选择，0.学号排序 1.英语成绩排序 2.Python成绩排序 3.Java成绩排序 4.总成绩排序'))
    if mode == 0:
        student_new.sort(key=lambda x: int(x['stu_id']), reverse=flag)
    elif mode == 1:
        student_new.sort(key=lambda x: int(x['english']), reverse=flag)
    elif mode == 2:
        student_new.sort(key=lambda x: int(x['python']), reverse=flag)
    elif mode == 3:
        student_new.sort(key=lambda x: int(x['java']), reverse=flag)
    elif mode == 4:
        student_new.sort(key=lambda x: int(x['english'])+int(x['python'])+int(x['java']), reverse=flag)
    else:
        print('输入有误，重新输入')
        sort()
    for item in student_new:
        show_student(item)


def number():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file1:
            lst_student = file1.readlines()
        print('有{0}位学生'.format(len(lst_student)))

    else:
        print('尚未保存数据')


def show():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file1:
            student_info = file1.readlines()
        for item in student_info:
            dic = dict(eval(item))
            show_student(dic)
    else:
        print('尚未保存数据')


def show_student(lst):  # lst是一个字典
    print('学生ID:{0}\t学生姓名:{1}\t英语成绩:{2}\tPython成绩:{3}\tJava成绩:{4}\t总成绩:{5}'.format(lst['stu_id'],
                                                                                   lst['name'],
                                                                                   lst['english'],
                                                                                   lst['python'],
                                                                                   lst['java'],
                                                                                   int(lst['english']) +
                                                                                   int(lst['python']) +
                                                                                   int(lst['java'])))


print('\033[0;34m=================学生信息管理系统=================\033[m')
main()
