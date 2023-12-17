import re  # Import the regular expressions module

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact {contact.name} added successfully.")

    def validate_phone_number(self, phone_number):
        # Check if the phone number has exactly 10 digits
        return re.match(r'^\d{10}$', phone_number)

    def validate_email(self, email):
        # Check if the email ends with "@gmail.com"
        return email.lower().endswith('@gmail.com')

    def view_contacts(self):
        if not self.contacts:
            print("Contact list is empty. Add contacts to display.")
            return

        print("\nContact List:")
        for contact in self.contacts:
            print(f"Name: {contact.name}\tPhone: {contact.phone_number}")

    def search_contact(self, query):
        result = [contact for contact in self.contacts if query.lower() in contact.name.lower() or query in contact.phone_number]
        if result:
            print("\nSearch Results:")
            for contact in result:
                print(f"Name: {contact.name}\tPhone: {contact.phone_number}")
        else:
            print("No matching contacts found.")

    def update_contact(self, name, new_phone_number, new_email, new_address):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                # Validate the new phone number and email before updating
                if self.validate_phone_number(new_phone_number) and self.validate_email(new_email):
                    contact.phone_number = new_phone_number
                    contact.email = new_email
                    contact.address = new_address
                    print(f"Contact {name} updated successfully.")
                else:
                    print("Invalid phone number or email format. Contact not updated.")
                return
        print(f"Contact {name} not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact {name} deleted successfully.")
                return
        print(f"Contact {name} not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")

            # Validate the phone number and email before adding a new contact
            if contact_book.validate_phone_number(phone_number) and contact_book.validate_email(email):
                new_contact = Contact(name, phone_number, email, address)
                contact_book.add_contact(new_contact)
            else:
                print("Invalid phone number or email format. Contact not added.")
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            query = input("Enter name or phone number to search: ")
            contact_book.search_contact(query)
        elif choice == "4":
            name = input("Enter the name of the contact to update: ")
            new_phone_number = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            contact_book.update_contact(name, new_phone_number, new_email, new_address)
        elif choice == "5":
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
