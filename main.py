from phonebook. core import add_contact, get_contacts, search_contact

def main():
    while True:
        print("🌟 Phonebook 🌟")
        print("1️⃣ Add Contact")
        print("2️⃣ Show Contacts")
        print("3️⃣ Search by Name")
        print("4️⃣ Exit")
        choice = input("Your choice: ")
        
        if choice == "1":
            name = input("👤 Name: ")
            phone = input("📞 Phone Number: ")
            add_contact(name, phone)
            print(f"✅ {name} has been added successfully!\n")
        elif choice == "2":
            contacts = get_contacts()
            print("\n📋 Contact List")
            if not contacts:
                print("⚠️ No contacts found.\n")
            else:
                for i, c in enumerate(contacts, start=1):
                    print(f"{i}. 👤 {c['name']} | 📞 {c['phone']}")
            print()
        elif choice == "3":
            search_name = input("👤 Enter name to search: ")
            results = search_contact(search_name)
            if results:
                for c in results:
                    print(f"✅ Found: 👤 {c['name']} | 📞 {c['phone']}")
            else:
                print("❌ Contact not found.\n")
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
