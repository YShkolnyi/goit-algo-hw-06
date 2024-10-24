from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError
        super().__init__(value) 

class Phone(Field):
    def __init__(self, value):
        if not (value.isdigit() and len(value) == 10):
            raise ValueError
        super().__init__(value) 

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self,phone):
        self.phones.append(Phone(phone))

    def remove_phone(self,phone):
        for i in self.phones: #V03 - перебираємо елементи списку.
            if i.value == phone: #V03 - зводимо все до str і шукаємо відповідність. #V04 - str(i) замінено на i.value
                self.phones.remove(i) #V03 - видаляємо елемент списку класу Phone
    
    def edit_phone(self,old_phone,new_phone): #V05 - видалено try-except
        for i in self.phones: #V03 - перебираємо елементи списку.
            if i.value == old_phone: #V03 - зводимо все до str і шукаємо відповідність.  #V04 - str(i) замінено на i.value
                index = self.phones.index(i) #V03 - якщо є відповідність, то дізнаємось індекс оригінального екземпляра класу Phone.
                self.phones[index] = Phone (new_phone) #V03 - знаючи індекс замінюємо один об'єкт Phone на інший.
                break #V04 - якщо відповідний телефон знайдено і замінено, то далі for може не ітерувати.
        else: #V04 - цей else виконується, якщо цикл for добіг кінця і не наткнувся на break під час виконання. Тобто помилка виникне, якщо old_phone не буде знайдено в self.phones.
            raise ValueError (f"This phone {old_phone} doesn't exist in address book.")

    def find_phone(self,phone):
        for i in self.phones: #V03 - перебираємо елементи списку.
            if i.value == phone: #V03 - зводимо все до str і шукаємо відповідність. #V04 - str(i) замінено на i.value
                return i #V02 - замінив строку на об'єкт класу Phone.  #V03 - якщо вони однакові, то замість шукати за індексом, можна перетворити строку в об'єкт класу Phone. Виведення від цього не зміниться. #V04 - повертаємо знайдений об'єкт.
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self,record):
        self.data[record.name.value]=record

    def find(self,name):
        return self.data.get(name)
    
    def delete(self,name):
        del self.data[name]

    def __str__(self):
        records = "\n".join(str(record) for record in self.data.values())
        return f"{records}"

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
    
print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Видалення номеру телефону
john.remove_phone('1112223333')

print(john) # Виведення: Contact name: John, phones: 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")

# V06
#V07