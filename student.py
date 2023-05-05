import os
import re
class Student:
    def __init__(self,studentName,studentSurname,studentPatronymic,studentgroup,studentAvgScrore):
        self.studentName = studentName
        self.studentSurname = studentSurname
        self.studentPatronymic = studentPatronymic
        self.studentgroup = studentgroup
        self.studentAvgScrore = studentAvgScrore
    def addStudent(self):
        if not os.path.exists("Students"):
            os.makedirs("Students")
        with open('Students\students.txt', 'a', encoding='UTF8') as f:
            f.write(f"{self.studentName}, {self.studentSurname}, {self.studentPatronymic}, {self.studentgroup}, {self.studentAvgScrore}\n")

    @staticmethod
    def find_Student(Search):
        results = []
        f = open('Students\students.txt', 'r+', encoding='UTF8').read().split('\n')
        for i in range(len(f)):
            if re.search(Search,str(f[i])):
                if str(f[i]) != '':
                    results.append(f[i])
        return results

    @staticmethod
    def removeStudent(results):
        with open('Students\students.txt', 'r', encoding='UTF8') as f1, open('Students\students2.txt', 'w', encoding='UTF8') as f2:
            lines = f1.readlines()
            for line in lines:
                line = line.strip()
                if line != results:
                    f2.write(line)
                    f2.write('\n')
        with open('Students\students.txt', 'w', encoding='UTF8') as f1, open('Students\students2.txt', 'r', encoding='UTF8') as f2:
            lines = f2.readlines()
            for line in lines:
                f1.write(line)

    @staticmethod
    def editStudent(results, row_values):
        with open('Students/students.txt', 'r', encoding='UTF8') as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            if line.strip() == results:
                lines[i] = f"{row_values[0]}, {row_values[1]}, {row_values[2]}, {row_values[3]}, {row_values[4]}\n"
                break

        with open('Students/students.txt', 'w', encoding='UTF8') as f:
            f.writelines(lines)
