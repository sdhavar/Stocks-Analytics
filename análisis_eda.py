import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

file_path = 'supermarket_sales.csv'
df = pd.read_csv(file_path)

"""# Análisis EDA"""

# Visualización valores categóricos

categorical = ['Branch', 'City', 'Customer type', 'Gender', 'Product line', 'Payment']
df[categorical].info()

for col in categorical:
    plt.figure(figsize=(8, 4))
    sns.countplot(data=df, x=col, palette="viridis", order=df[col].value_counts().index)
    plt.title(f"Distribución de {col}", size=14)
    plt.xticks(rotation=45)
    plt.show()

# Visualización variables numéricas

numerical = ['Unit price', 'Quantity', 'Tax 5%', 'Total', 'Rating']
df[numerical].describe()

numeric_cols = ['Unit price', 'Quantity', 'Tax 5%', 'Total', 'cogs', 'gross income', 'Rating']
df[numeric_cols].hist(bins=20, figsize=(15, 10), color='skyblue', edgecolor='black')
plt.suptitle("Distribución de variables numéricas", size=18)
plt.show()

# Correlaciones
plt.figure(figsize=(10, 8))
correlation_matrix = df[numeric_cols].corr()
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
plt.title("Mapa de calor de la correlación", size=16)
plt.show()

# Relación entre Product line y gross income
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x="Product line", y="gross income", palette="Set2")
plt.title("Relación entre Product line y Gross Income", size=16)
plt.xticks(rotation=45)
plt.show()