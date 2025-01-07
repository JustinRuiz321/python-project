employees = [{
  "name": "Tina",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer",
  "address": {
    "city": "New York",
    "country": "USA"
  }
},
{
  "name": "Tim",
  "age": 35,
  "birthday": "1985-02-21",
  "job": "Developer",
  "address": {
    "city": "Sydney",
    "country": "Australia"
  }
}]


def youngest_employee(employees):
    print(f"Youngest employee name: {employees[0]['name']}")
    print(f"Youngest employee age: {employees[0]['age']}")

youngest_employee(employees)

def uppercase_vs_lowercase(string):
    lowercase = 0
    uppercase = 0
    for char in string:
        if char.islower():
            lowercase += 1
        elif char.isupper():
            uppercase += 1
    print(f'Number of lowercase letters = ', lowercase)
    print(f'Number of uppercase letters = ', uppercase)

uppercase_vs_lowercase("akjsfhkjhsaLAKJSDFKALJNFB")

def even_numbers(list_of_numbers):
    for even in list_of_numbers:
        if even % 2 == 0:
            print(even)

even_numbers([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])