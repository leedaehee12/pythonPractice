import os

CONTACTS_FILE = "contact.txt"

def load_contact():
    contacts = {}
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            for line in file:
                name, phone = line.strip().split(",")
                contacts[name] = phone
    return contacts
            
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        for name, phone in contacts.items():
            file.write(f"{name}, {phone}")

def add_contacts(contacts):
    name = input("Enter contact name : ")
    phone = input("Enter contact phone number : ")
    contacts[name] = phone
    print(f"Contact {name} added")

def delete_contact(contacts):
    name = input("Enter contact name for delete")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted")
    else:
        print(f"Contact {name} not found")    

def view__contacts(contacts):
    if contacts:
        print("Contacts List: ")
        for name, phone in contacts.items():
            print(f"{name} : , {phone} ")
        else:
            print("No contacts found.")

def main():
    contacts = load_contact()    

    while True:
        print("\nContact Manager")
        print("1. Add Contacts")
        print("2. Delete Contacts")
        print("3. View Contacts")
        print("4. Exit")

        choice = input("choose an option : ")
        if choice == "1":
            add_contacts(contacts)
        elif choice == "2":
            delete_contact(contacts)
        elif choice == "3":
            view__contacts(contacts)
        elif choice == "4":
            save_contacts(contacts)
            print("Exiting.....")
            break

        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
    







