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

#task2
class City:
    def __init__(self, name, region, country, population, postal_code, phone_code):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.postal_code = postal_code
        self.phone_code = phone_code

    def get_info(self):
        return (f"\nНазва міста: {self.name}, \nРегіон: {self.region}, "
                f"\nКраїна: {self.country}, \nКількість жителів: {self.population}, "
                f"\nПоштовий індекс: {self.postal_code}, \nТелефонний код: {self.phone_code}")

    def update_population(self, new_population):
        self.population = new_population
        print(f"\nКількість жителів оновлена: {self.population}")

city1 = City("Київ", "Київська область", "Україна", 2884000, "01001", "+38044")
print(city1.get_info())
city1.update_population(2900000)
print(city1.get_info())

