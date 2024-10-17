#task1
class Person:
    def __init__(self, name, date, number, city, country, haddress):
        self.name = name
        self.date = date
        self.number = number
        self.city = city
        self.country = country
        self.haddress = haddress

    def update_phone(self, new_phone):
        self.number = new_phone
        print(f"\nНомер телефону оновлено: {self.number}")

    def update_address(self, new_address):
        self.haddress = new_address
        print(f"\nДомашня адреса оновлена: {self.haddress}")

    def getInfo(self):
        return (f"\nПІБ: {self.name}, \nДата народження: {self.date}, "
              f"\nКонтактний телефон: {self.number}, \nМісто: {self.city},"
              f"\nКраїна: {self.country}, \nДомашня адреса: {self.haddress}")

Person1 = Person("Самойленко Настя Ігорівна","28.10.1998", "+380990960178","Дніпро", "Україна", "ж/м Тополя2")
print(Person1.getInfo())
Person1.update_phone("+380960960179")
print(Person1.getInfo())