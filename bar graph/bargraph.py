# -*- coding: utf-8 -*-
"""bargraph.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aIOmiKHFTz0DttpZz__ETlJNWuofd7eu
"""

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('/sales_summary.csv')

# Generate the bar chart
plt.figure(figsize=(10, 6))
plt.bar(df['product'], df['sales'], color='skyblue')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.title('Sales Summary')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the chart as an image file
plt.savefig('sales_summary_chart.png')
plt.show()