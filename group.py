import re
import os
from student import Student
class Group(Student):
    def findGroup(self):
        list = []
        list_group = []
        f = open('Students\students.txt', 'r+', encoding='UTF8').read().split('\n')
        for i in range(len(f)-1):
            group = f[i]
            list.append(group.split(', ')[3])
        for i in list:
            if i not in list_group:
                list_group.append(i)
        return list_group

    def listStudents(self, list_group, num):
        students = []
        if 0 <= num <= (len(list_group)):
            f = open('Students\students.txt', 'r+', encoding='UTF8').read().split('\n')
            for i in range(len(f)):
                student_data = f[i].split(", ")
                if len(student_data) >= 3 and student_data[3] == list_group[num]:
                    students.append(f[i])
            return students

    def deleteGroup(self, current_group):
        with open('Students/students.txt', 'r', encoding='UTF8') as f1, open('Students/students2.txt', 'w',
                                                                             encoding='UTF8') as f2:
            for line in f1:
                if current_group not in line:
                    f2.write(line)

        os.remove('Students/students.txt')
        os.rename('Students/students2.txt', 'Students/students.txt')
