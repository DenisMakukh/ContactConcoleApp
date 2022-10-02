class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class Contacts:
    def __init__(self):
        self.baza = [[], [], [], [], [], []]

    def __add__(self, contact):
        self.baza[0].append(len(self.baza[0]) + 1)
        fio = contact.name.split(" ")
        while len(fio) < 3:
            fio.append(None)
        self.baza[1].append(fio[0])
        self.baza[2].append(fio[1])
        self.baza[3].append(fio[2])
        if contact.phone != '':
            self.baza[4].append(contact.phone)
        else:
            self.baza[4].append(None)
        if contact.email != '':
            self.baza[5].append(contact.email)
        else:
            self.baza[5].append(None)

    def getContact(self, id):
        ans = "ID: " + str(self.baza[0][id]) + "\n"
        if self.baza[1][id] != None:
            ans += "ФИО: " + self.baza[1][id]
        if self.baza[2][id] != None:
            ans += " " + self.baza[2][id]
        if self.baza[3][id] != None:
            ans += " " + self.baza[3][id]
        if self.baza[4][id] != None:
            ans += "\n" + "Номер телефона: " + self.baza[4][id]
        else:
            ans += "\n" + "Номер телефона: " + "None"
        if self.baza[5][id] != None:
            ans += "\n" + "Почта: " + self.baza[5][id] + "\n"
        else:
            ans += "\n" + "Почта: " + "None" + "\n"
        return ans

    def phoneSearch(self, phone):
        if self.baza[4].__contains__(phone):
            id = self.baza[4].index(phone)
            print(self.getContact(id))
        else:
            print("Не найдено.")

    def emailSearch(self, email):
        if self.baza[5].__contains__(email):
            id = self.baza[5].index(email)
            print(self.getContact(id))
        else:
            print("Не найдено.")

    def search(self, fio):
        sp = []
        if fio[0] != None:
            for i in range(len(self.baza[1])):
                if fio[0] == self.baza[1][i]:
                    sp.append(self.baza[0][i] - 1)
        if fio[1] != None:
            if fio[0] != None:
                for id in sp:
                    if fio[1] != self.baza[2][id]:
                        sp.remove(id)
            else:
                for i in range(len(self.baza[2])):
                    if fio[1] == self.baza[2][i]:
                        sp.append(self.baza[0][i] - 1)

        if fio[2] != None:
            if fio[0] != None or fio[1] != None:
                for id in sp:
                    if fio[2] != self.baza[3][id]:
                        sp.remove(id)
            else:
                for i in range(len(self.baza[3])):
                    if fio[2] == self.baza[3][i]:
                        sp.append(self.baza[0][i] - 1)

        if len(sp) == 0:
            print("Не найдено.")
        else:
            for id in sp:
                print(self.getContact(id))

    def getWithoutPhoneOreMail(self, num):
        if num == 1:
            for i in range(len(self.baza[4])):
                if self.baza[4][i] == None:
                    print(self.getContact(i))
        if num == 2:
            for i in range(len(self.baza[5])):
                if self.baza[5][i] == None:
                    print(self.getContact(i))
        if num == 3:
            for i in range(len(self.baza[4])):
                if self.baza[4][i] == None and self.baza[5][i] == None:
                    print(self.getContact(i))

    def change(self, id, contact):
        id -= 1
        fio = contact.name.split(" ")
        while len(fio) < 3:
            fio.append(None)
        self.baza[1][id] = fio[0]
        self.baza[2][id] = fio[1]
        self.baza[3][id] = fio[2]
        if len(contact.phone) > 0:
            self.baza[4][id] = contact.phone
        else:
            self.baza[4][id] = None
        if len(contact.email) > 0:
            self.baza[5][id] = contact.email
        else:
            self.baza[5][id] = None

    def printAll(self):
        for i in range(len(self.baza[0])):
            print(self.getContact(i))


def printCommands():
    print("Что вы хотите сделать? ")
    print("0 - Показать все контакты", "1 - Поиск по телефону", "2 - Поиск по почте", "3 - Поиск по ФИО",
          "4 - поиск по отсутствию номера/почты", "5 - Изменение контакта", "6 - остановить программу", sep="\n")


print("Введите название файла")
filename = input()
file = open(filename, encoding='utf-8')
funct = Contacts()
for sp1 in file:
    arr = sp1.split(",")
    contact = Contact(arr[0],arr[1].replace(" ",""),arr[2].replace(" ","").replace("\n",""))
    funct.__add__(contact)
printCommands()
x = int(input())
while x!="cristianbenuatopchick":
    if x == 0:
        funct.printAll()
    if x==1:
        print("Введите телефон")
        phone = input()
        funct.phoneSearch(phone)
    elif x == 2:
        print("Введите почту")
        email = input()
        funct.emailSearch(email)
    elif x == 3:
        fio = []
        print("Введите фамилию, если забыли - перейдите на новую строку")
        surname1 = input()
        if surname1=='':
            fio.append(None)
        else:
            fio.append(surname1)
        print("Введите имя, если забыли - перейдите на новую строку")
        name2 = input()
        if name2 == '':
            fio.append(None)
        else:
            fio.append(name2)
        print("Введите отчество, если забыли - перейдите на новую строку")
        ot = input()
        if ot == '':
            fio.append(None)
        else:
            fio.append(ot)
        funct.search(fio)
    elif x == 4:
        print("Введите по чему хотите искать: ", "1 - без номера", "2 - без почты", "3 - без телефона и без почты", sep="\n")
        num = int(input())
        funct.getWithoutPhoneOreMail(num)
    elif x == 5:
        print("Введите id контакта, который хотите изменить и новые данные для него", "через Enter", sep="\n")
        id = int(input())
        q = input().split(",")
        contact = Contact(q[0], q[1].replace(" ", ""), q[2].replace(" ", "").replace("\n", ""))
        funct.change(id, contact)
    elif x == 6:
        "Вы закрыли программу"
        break
    print()
    printCommands()
    x = int(input())
