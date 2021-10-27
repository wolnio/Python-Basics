from os import system


def cls(): return system('cls')


cls()

userList = []
filename = "users.txt"
align_left = "<13"


class User():

    def __init__(self, name, name2, surname, birthDate, position):
        self.name = name
        self.name2 = name2
        self.surname = surname
        self.birthDate = birthDate
        self.position = position

    def get_personalData(self):
        long_name = f"{self.name} {self.name2 if self.name2 else ''} {self.surname}"
        return long_name.title()


class Employee(User):

    def __init__(self, name, name2, surname, birthDate, position):
        super().__init__(self, name, name2, surname, birthDate, position)

    def get_employee_email(self):
        email = f"{self.name}.{self.name2 + '.' if self.name2 else ''}{self.surname}@employee.university.com"
        return email.lower()


class Student(User):

    def __init__(self, indexNumber, name, name2, surname, birthDate, position):
        super().__init__(name, name2, surname, birthDate, position)
        self.indexNumber = indexNumber

    def get_student_email(self):
        email = f"{self.name}.{self.name2 + '.' if self.name2 else ''}{self.surname}@student.university.com"
        return email.lower()


def addUser():
    #name, name2, surname, birthDate, position, index = None

    name = input("\tFirst name: ")
    name2 = input("\tSecond name: ")
    surname = input("\tSurname: ")
    birthDate = input("\tBirth date: ")
    position = input("\tPosition: ")

    if position.lower() == 's':
        index = input("\tIndex number: ")
        tmp = Student(index, name, name2, surname, birthDate, position)
        tmp.indexNumber = index
        return tmp
    elif position.lower() == 'e':
        tmp = Employee(name, name2, surname, birthDate, position)
        return tmp


print("===== Welcome to DZIEKANAT! =====")

userInput = ''

while userInput.lower() != 'exit':
    userInput = input(
        "\nAdd user [A] | Print users [U] | Print mails [M] | Exit [EXIT]\n")

    if userInput.lower() == 'a':
        temp = addUser()
        userList.append(temp)
        with open(filename, 'a') as file_object:
            file_object.write(
                f"{temp.name:{align_left}}"
                f"{temp.name2 + ' ' if temp.name2 else '':{align_left}}"
                f"{temp.surname:{align_left}}"
                f"{temp.birthDate:{align_left}}"
                f"{'Student' if temp.position.lower()=='s' else 'Employee' if temp.position.lower()=='e' else 'Unknown':{align_left}}"
                f"{temp.indexNumber if temp.position.lower()=='s' else '':{align_left}}"
                f"{temp.get_employee_email() if type(temp) is Employee else temp.get_student_email() if type(temp) is Student else ''}\n"
                )

    elif userInput.lower() == 'u':
        for i in userList:
            print(i.get_personalData())
    elif userInput.lower() == 'm':
        for i in userList:
            if type(i) is Student:
                print(i.get_student_email())
            elif type(i) is Employee:
                print(i.get_employee_email())
