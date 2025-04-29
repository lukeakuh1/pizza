import pandas as pd

# Creating a small dataset to practice the apply() method on.
data = {"name": ["Luke", "Smith", "Mathias", "Decoline", "Suzan", "Princely", "Ninian", "Halidate", "Atingi"],
        "age": [29, 31, 60, 45, 50, 7, 30, 35, 15],
        "invest": [20000, 2500, 5000, 1000, 3000, 1500, 12000, 20000, 5000]} # dictionary data

df = pd.DataFrame(data)    # dataframe created

# custom functions

def age_group(row):  # this function categorize the age column in to age group
    return "1-9" if row < 10 else "10-19" if (9 < row < 20) else "20-29" if (19 < row < 30) else "30-39" if (29 < row < 40) else "40-49" if (39 < row < 50) else "50+"


def total(dfs):  # this function sum up the invest and reinvest columns.
    return dfs["invest"] + dfs['reinvest']

# Applying the custom functions on the dataset
df["age_group"] = df['age'].apply(age_group)
df["reinvest"] = df['invest'].apply(lambda x: x *.15)
df["total_invest"] = df.apply(total, axis=1)
print(df)