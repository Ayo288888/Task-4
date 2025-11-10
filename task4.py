
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


sns.set_theme(style="whitegrid")


df = pd.read_csv("heart.csv")

print(df.head())
print(df.info())



plt.figure(figsize=(12, 5))


plt.subplot(1, 2, 1)
plt.plot(df['age'], df['trestbps'], color='blue', linewidth=2)
plt.title('Line Plot: Age vs Resting BP (Matplotlib)')
plt.xlabel('Age')
plt.ylabel('Resting Blood Pressure (trestbps)')


plt.subplot(1, 2, 2)
plt.scatter(df['age'], df['thalach'], color='red', alpha=0.6)
plt.title('Scatter Plot: Age vs Max Heart Rate (Matplotlib)')
plt.xlabel('Age')
plt.ylabel('Maximum Heart Rate (thalach)')

plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 5))


plt.subplot(1, 2, 1)
sns.histplot(data=df, x='chol', hue='target', kde=True, palette='cool')
plt.title('Histogram: Cholesterol by Target (Seaborn)')
plt.xlabel('Cholesterol Level (chol)')

plt.subplot(1, 2, 2)
sns.boxplot(data=df, x='target', y='thalach', palette='Set2')
plt.title('Box Plot: Max Heart Rate by Target (Seaborn)')
plt.xlabel('Heart Disease (1 = Yes, 0 = No)')
plt.ylabel('Max Heart Rate (thalach)')

plt.tight_layout()
plt.show()
