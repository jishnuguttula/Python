contacts = {}

def add_contacts():
    name = input("Enter name: ")
    if name in contacts:
         print ("contact alread exists")
         return

    phone = input("Enter phone: ")
    contacts[name] = phone

def display_contacts():
    for name, phone in contacts.items():
        print(name, phone)


def search_contacts():
    name = input("Enter name to search: ")
    if name in contacts:
        print(name, contacts[name])
    else:
        print("Contact not found")

def delete_contacts():
    name = input ("Enter name to delete: ")
    if name in contacts:
            del contacts[name]
            print("Contact deleted")
    else:
            print("Contact not found")

while True:
    print("1.Add Contact 2.Display Contacts 3.Search Contact 4.Delete Contact 5.Exit")
    ch = int(input())

    if ch == 1:
        add_contacts()
    elif ch == 2:
        display_contacts()
    elif ch == 3:
        search_contacts()
    elif ch == 4:
        delete_contacts()
    else:
        break
