class Person:

    def __init__(self, name, address, phone):

        self.__name = name
        self.__address = address
        self.__telephone = phone

    def print_person(self):
        print(self.__name, ',', self.__address, ',' ,self.__telephone)

class Customer(Person):

    def __init__(self, name, address, phone, number, boolean):

        Person.__init__(self, name, address, phone)

        self.__custnum = number
        self.__mailist = boolean

    def print_person(self):
        print(Person.print_person, ',', self.__custnum, ',', self.__mailist)
