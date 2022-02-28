class Person:
    def __init__(self, name, address, phone):
        self.personName = name
        self.add = address
        self.telephone = phone

    def print_person(self):
        print("Name:", self.personName)
        print("Address:", self.add)
        print("Phone:", self.telephone)


class Customer(Person):
    def __init__(self, name, address, phone, num, mail):
        Person.__init__(self, name, address, phone)

        self.__number = num
        self.__mailList = mail

    def print_person(self):
        print("Name:", self.personName)
        print("Address:", self.add)
        print("Phone:", self.telephone)
        print("Customer Number:", self.__number)
        print("Mail List:", self.__mailList)
