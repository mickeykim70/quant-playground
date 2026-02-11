import os
import readline

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")
        print(f"Address: {self.address}")

def set_contact():
    name = input("Name: ")
    phone = input("Phone Number: ")
    email = input("E-mail: ")
    address = input("Address: ")
    return Contact(name, phone, email, address)

def print_menu():
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Print All Contacts")
    print("4. Exit")
    menu = input("Menu: ")
    return menu

def print_contacts(contacts):
    for contact in contacts:
        contact.print_info()

def delete_contact(contacts, name):
    for i, contact in enumerate(contacts):
        if contact.name == name:
            del contacts[i]

def store_contact(contacts):
    with open("contact_db.txt", "wt", encoding="utf-8") as f:
        for contact in contacts:
            f.write(f"{contact.name}/{contact.phone}/{contact.email}/{contact.address}\n")

def load_contact(contacts):
    if not os.path.exists("contact_db.txt"):
        return
    
    with open("contact_db.txt", "rt", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            if line.strip():
                name, phone, email, address = line.strip().split("/")
                contact = Contact(name, phone, email, address)
                contacts.append(contact)

def run():
    contacts = []
    load_contact(contacts)  # 프로그램 시작 시 데이터 로드
    while True:
        menu = print_menu()
        if menu == '1':
            contact = set_contact()
            contacts.append(contact)
        elif menu == '2':
            name = input("Name to delete: ")
            delete_contact(contacts, name)
        elif menu == '3':
            print_contacts(contacts)
        elif menu == '4':
            store_contact(contacts)  # 종료 전 데이터 저장
            break

if __name__ == "__main__":
    run()
