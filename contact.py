class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}"


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print("Contact removed successfully.")
                return
        print("Contact not found.")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def display_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for contact in self.contacts:
                print(contact)
                print()


# Main program
contact_manager = ContactManager()

while True:
    print("Contact Manager Menu:")
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. Search Contact")
    print("4. Display Contacts")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")

        contact = Contact(name, phone, email)
        contact_manager.add_contact(contact)

    elif choice == "2":
        name = input("Enter the name of the contact to remove: ")
        contact_manager.remove_contact(name)

    elif choice == "3":
        name = input("Enter the name of the contact to search: ")
        contact = contact_manager.search_contact(name)
        if contact:
            print("Contact found:")
            print(contact)
        else:
            print("Contact not found.")

    elif choice == "4":
        print("Contacts:")
        contact_manager.display_contacts()

    elif choice == "5":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")