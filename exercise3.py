from tkinter.font import names

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

for employee in employees:
    print(f"name: {employee['name']}")
    print(f"job: {employee['job']}")
    print(f"city: {employee['address']['city']} \n")

print(employees[1]['address']['country'])
