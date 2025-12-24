contacts = []

def add_contact(name: str, phone: str):
    contacts. append({"name": name, "phone": phone})

def get_contacts():
    return contacts

def search_contact(search_name: str):
    return [
        contact for contact in contacts
        if search_name.lower() in contact['name'].lower()
    ]
