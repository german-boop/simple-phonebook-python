from phonebook. core import add_contact, get_contacts, search_contact

def test_add_and_get():
    add_contact("Ali", "12345")
    add_contact("Sara", "67890")
    contacts = get_contacts()
    assert len(contacts) == 2

def test_search():
    add_contact("John", "11111")
    results = search_contact("John")
    assert len(results) == 1
    assert results[0]["phone"] == "11111"
