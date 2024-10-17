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

#task3
class Country:
    def __init__(self, name, continent, population, phone_code, capital, cities):
        self.name = name
        self.continent = continent
        self.population = population
        self.phone_code = phone_code
        self.capital = capital
        self.cities = cities  # Список міст

    def get_info(self):
        return (f"\nНазва країни: {self.name}, \nКонтинент: {self.continent}, "
                f"\nКількість жителів: {self.population}, \nТелефонний код: {self.phone_code}, "
                f"\nСтолиця: {self.capital}, \nМіста: {', '.join(self.cities)}")

    def update_population(self, new_population):
        self.population = new_population
        print(f"\nКількість жителів оновлена: {self.population}")

country1 = Country("Україна", "Європа", 40000000, "+380", "Київ", ["Львів", "Харків", "Одеса"])
print(country1.get_info())
country1.update_population(42000000)
print(country1.get_info())

#task4
import math

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Знаменник не може бути нулем!")
        self.numerator = numerator
        self.denominator = denominator

    def get_info(self):
        return f"{self.numerator}/{self.denominator}"

    def add(self, other):
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den).simplify()

    def subtract(self, other):
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den).simplify()

    def multiply(self, other):
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return Fraction(num, den).simplify()

    def divide(self, other):
        if other.numerator == 0:
            raise ValueError("Не можна ділити на нуль!")
        num = self.numerator * other.denominator
        den = self.denominator * other.numerator
        return Fraction(num, den).simplify()

    def simplify(self):
        gcd = math.gcd(self.numerator, self.denominator)
        return Fraction(self.numerator // gcd, self.denominator // gcd)

frac1 = Fraction(3, 4)
frac2 = Fraction(5, 6)

print("\nДріб 1:", frac1.get_info())
print("Дріб 2:", frac2.get_info())

sum_result = frac1.add(frac2)
print("Сума:", sum_result.get_info())

diff_result = frac1.subtract(frac2)
print("Різниця:", diff_result.get_info())

mul_result = frac1.multiply(frac2)
print("Добуток:", mul_result.get_info())

div_result = frac1.divide(frac2)
print("Частка:", div_result.get_info())
