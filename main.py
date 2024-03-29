import sys
from peewee import PostgresqlDatabase, Model, CharField
import pyfiglet

db = PostgresqlDatabase('contacts', user='mustafahassan', password='',
                        host='localhost', port=5432)
db.connect()


class Contact(Model):
    first_name = CharField()
    last_name = CharField()
    phone = CharField()

    class Meta:  # magic
        database = db  # This model uses the "contacts.db" database.


db.create_tables([Contact])


def createContacts():
    intro = pyfiglet.figlet_format("Contacts List")
    print(intro)
    print("Create New Contact")
    print("-----Hit Enter without First Name input to Break------")
    created_num = 0
    while True:
        name = input("First Name: ")
        if name == '':
            break
        surname = input("Last Name: ")
        number = input("Phone: ")
        print("Contact created!")
        created_num += 1
        new_contact = Contact(first_name=name, last_name=surname, phone=number)
        new_contact.save()
    print(f'created {created_num} contacts')


def readContacts():
    listed_num = 0
    for contact in Contact.select().order_by(Contact.first_name):
        print(f"{contact.first_name} {contact.last_name} - {contact.phone}")
        listed_num += 1
    print(f'listing {listed_num} records')
    res = input("Would you like to look for a first name? (y or n) ")
    if res == 'y':
        name = input("Enter first name: ")
        record = Contact.select().where(Contact.first_name == name).get()
        if (record):
            print(record.first_name)
            print(record.last_name)
            print(record.phone)
        else:
            print("Sorry there are no records matching that name.")
    else:
        pass


def updateContacts():
    print("update contacts coming soon.")


def deleteContacts():
    print("delete contacts coming soon.")


command = {
    'c': createContacts,
    'r': readContacts,
    'u': updateContacts,
    'd': deleteContacts
}

# main


def _usage():
    print(f'USAGE: python {sys.argv[0]} c|r|u|d')


def _main():
    try:
        command[sys.argv[1]]()
        return 0
    except IndexError:
        _usage()
        return 1
    except KeyError:
        _usage()
        return 2
    finally:
        print("disconnecting from db")
        db.close()


if __name__ == '__main__':
    exitval = _main()

    sys.exit(exitval)