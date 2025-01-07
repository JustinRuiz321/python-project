employee = {
  "name": "Tim",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer"
}

employee["job"] = "Software Engineer"
print(employee)

employee.pop("age")
print(employee)

for key, value in employee.items():
  print(f"{key}:{value}")

# Next Exercise

dict_one = {'a': 100, 'b': 400}
dict_two = {'x': 300, 'y': 200}

dict_merged = dict_one.copy()
dict_merged.update(dict_two)
print(dict_merged)

sum_of_values = 0
for value in dict_merged.values():
    sum_of_values = sum_of_values + value
print(sum_of_values)

merged_values = []
for value in dict_merged.values():
    merged_values.append(value)

merged_values.sort()
print(f"min value: {merged_values[0]}")
print(f"max value: {merged_values[len(merged_values)-1]}")

