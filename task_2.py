class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Invalid phone number format. Must be 10 digits.")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        try:
            phone_obj = Phone(phone)
            self.phones.append(phone_obj)
            return f"Phone {phone_obj} added."
        except ValueError as e:
            return str(e)

    def remove_phone(self, phone):
        for phone_obj in self.phones:
            if phone_obj.value == phone:
                self.phones.remove(phone_obj)
                return f"Phone {phone} removed."
        return f"Phone {phone} not found."

    def edit_phone(self, old_phone, new_phone):
        for i, phone_obj in enumerate(self.phones):
            if phone_obj.value == old_phone:
                try:
                    new_phone_obj = Phone(new_phone)
                    self.phones[i] = new_phone_obj
                    return f"Phone {old_phone} edited to {new_phone}."
                except ValueError as e:
                    return str(e)
        return f"Phone {old_phone} not found."

    def find_phone(self, phone):
        for phone_obj in self.phones:
            if phone_obj.value == phone:
                return phone_obj
        return None

    def __str__(self):
        phones_str = "; ".join(str(phone) for phone in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"


class AddressBook:
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return f"Contact {name} deleted."
        return f"Contact {name} not found."


if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    print(john_record.add_phone("1234567890"))  # Виведення: Phone 1234567890 added.
    print(john_record.add_phone("5555555555"))  # Виведення: Phone 5555555555 added.

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    print(jane_record.add_phone("9876543210"))  # Виведення: Phone 9876543210 added.
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    print(
        john.edit_phone("1234567890", "1112223333")
    )  # Виведення: Phone 1234567890 edited to 1112223333.

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name.value}: {found_phone}")  # Виведення: John: 5555555555

    # Видалення запису Jane
    print(book.delete("Jane"))  # Виведення: Contact Jane deleted.
