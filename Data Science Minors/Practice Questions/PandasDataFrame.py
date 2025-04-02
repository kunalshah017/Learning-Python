import pandas as pd
import numpy as np

data = [
    {"Name": "ABC", "Age" : 20, "Salary" : 50000, "Department" : "XYZ"},
    {"Name": "David", "Age" : 20, "Salary" : 6000, "Department" : "IT"},
    {"Name": "ABC", "Age" : 20, "Salary" : 120000, "Department" : "IT"},
]

df = pd.DataFrame(data)

df = pd.concat([df, pd.DataFrame([{"Name": "ABC", "Age" : 20, "Salary" : 200, "Department" : "XYZ"}]
)], ignore_index=True)

print(df[["Age", "Salary"]])
print(df[df["Department"] == "IT"])
print(df.sort_values(by="Salary"))

df["Experience"] = np.random.randint(1, 11, size=len(df))
print(df)

df = df.drop(columns=["Department"])
print(df)