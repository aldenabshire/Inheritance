import exercise as e

def main():

    name = 'Bob' 
    address = '9472 Oak Springs Dr'
    phone = '254-544-1341'
    customer_number = '387'
    mailing_list = input('Would you like to be on the mailing list? (Y/N) ')


    name1 = e.Person(name, address, phone)
    cust1 = e.Customer(name, address, phone, customer_number, mailing_list)

    name1.print_person()
    cust1.print_person()



main()