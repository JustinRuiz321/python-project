import pandas as pd

df = pd.read_excel("employees.xlsx")
print(df.columns)

df_sorted = df.sort_values(by="Years of Experience", ascending=False)

df_sorted = df_sorted[["Name", "Years of Experience"]]

df_sorted.to_excel("employees_sorted.xlsx", index=False)

print("The sorted employees data has been saved to 'employees_sorted.xlsx'.")