class Person:
    def __init__(self, name, address, phone):
        self.__personName = name
        self.__add = address
        self.__telephone = phone

    def print_person(self):
        print("Name:", self.__personName)
        print("Address:", self.__add)
        print("Phone:", self.__telephone)


class Customer(Person):
    def __init__(self, name, address, phone, num, mail):
        Person.__init__(self, name, address, phone)

        self.__number = num
        self.__mailList = mail

    def print_person(self):
        Person.print_person(self)
        print("Customer Number:", self.__number)
        print("Mail List:", self.__mailList)
