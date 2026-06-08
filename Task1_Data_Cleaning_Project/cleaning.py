import pandas as pd

df = pd.read_csv("data/raw_employee_data.csv")

print("Original Shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
df["Name"] = df["Name"].fillna("Unknown")
df["Department"] = df["Department"].fillna(df["Department"].mode()[0])
df["Salary"] = df["Salary"].fillna(df["Salary"].median())
df["City"] = df["City"].fillna("Unknown")

# Standardize text
df["Name"] = df["Name"].str.strip().str.title()
df["Department"] = df["Department"].str.strip().str.title()

# Save cleaned data
df.to_csv("data/cleaned_employee_data.csv", index=False)

print("Duplicates:", df.duplicated().sum())
print("Missing values:")
print(df.isnull().sum())
print("Final Shape:", df.shape)
