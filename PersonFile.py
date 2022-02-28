import PersonClass as pc


def main():
    generic_person = pc.Person("John", "101 Washington Ave", "814-255-9142")

    customer = pc.Customer("Andrew", "102 Washington Ave", "912-555-1242", 12, True)

    generic_person.print_person()
    print()
    customer.print_person()


main()
