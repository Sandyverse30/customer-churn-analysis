# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 18:41:37 2026

@author: Sandeep Katta
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r"C:\Users\Sandeep Katta\OneDrive\Documents\TELCO RAW DATA SET.csv")
print(df.head())
df.info()
df.isnull().sum()
df.columns
df.shape
#CHURN DISTRIBUTION 
import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(x='Churn', data=df)
plt.title("Customer Churn Distribution")
plt.show()

#CONTRACT VS CHURN 
sns.countplot(x='Contract', hue='Churn', data=df)
plt.title("Contract Type vs Churn")
plt.xticks(rotation=15)
plt.show()

#INTERNET SERVICE VS CHURN 
sns.countplot(x='InternetService', hue='Churn', data=df)
plt.title("Internet Service vs Churn")
plt.show()

#PAYMENT METHOD VS CHURN
sns.countplot(x='PaymentMethod', hue='Churn', data=df)
plt.title("Payment Method vs Churn")
plt.xticks(rotation=45)
plt.show()

#MONTLY CHARGES DISTRIBUTION 
plt.figure(figsize=(8,5))
sns.histplot(df['MonthlyCharges'], bins=30)
plt.title("Monthly Charges Distribution")
plt.show()

#