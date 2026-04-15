import pandas as pd

df = pd.read_csv('Telco-Customer-Churn.csv')
df.columns = df.columns.str.lower().str.replace(' ', '_')

# 1. Shape - how many rows and columns
print(f"Shape: {df.shape}")

# 2. Data types of every column
print("\nData types:")
print(df.dtypes)

# 3. Null count per column
print("\nNull counts:")
print(df.isna().sum())

# 4. Unique values for every categorical column
categorical_cols = ['gender', 'seniorcitizen', 'partner', 'dependents',
                    'phoneservice', 'multiplelines', 'internetservice',
                    'onlinesecurity', 'onlinebackup', 'deviceprotection',
                    'techsupport', 'streamingtv', 'streamingmovies',
                    'contract', 'paperlessbilling', 'paymentmethod', 'churn']

print("\nUnique values per column:")
for col in categorical_cols:
    print(f"{col}: {df[col].unique()}")

# 5. Summary stats for numeric columns
print("\nNumeric summary:")
print(df[['tenure', 'monthlycharges', 'totalcharges']].describe())