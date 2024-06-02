class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        print(f'Contact "{name}" added.')

    def view_contacts(self):
        if not self.contacts:
            print("No contacts in the contact book.")
        else:
            print("Contact List:")
            for contact in self.contacts:
                print(contact)

    def search_contact(self, name):
        found_contacts = [contact for contact in self.contacts if name.lower() in contact.name.lower()]
        if not found_contacts:
            print(f'No contacts found with the name "{name}".')
        else:
            print("Search Results:")
            for contact in found_contacts:
                print(contact)

    def update_contact(self, name, new_phone=None, new_email=None):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                if new_phone:
                    contact.phone = new_phone
                if new_email:
                    contact.email = new_email
                print(f'Contact "{name}" updated.')
                return
        print(f'No contact found with the name "{name}".')

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f'Contact "{name}" deleted.')
                return
        print(f'No contact found with the name "{name}".')

def main():
    contact_book = ContactBook()
    while True:
        print("\nContact Book Menu:")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Search contact")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            contact_book.add_contact(name, phone, email)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            name = input("Enter the name to search: ")
            contact_book.search_contact(name)
        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            new_phone = input("Enter new phone number (leave blank to keep unchanged): ")
            new_email = input("Enter new email (leave blank to keep unchanged): ")
            contact_book.update_contact(name, new_phone if new_phone else None, new_email if new_email else None)
        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == '6':
            print("Exiting the contact book application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
