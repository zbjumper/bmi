import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dataset/SOCR-HeightWeight.csv')

hm = df['Height(Inches)'] * 0.0254 
wkg = df['Weight(Pounds)'] * 0.453592
bmi = wkg / (hm ** 2)

# 使用 Matplotlib 展示身高、体重和BMI数据
plt.scatter(hm.values.reshape(-1, 1), wkg.values.reshape(-1, 1), c=bmi.values.reshape(-1, 1), cmap='viridis')
plt.xlabel('Height (m)')
plt.ylabel('Weight (kg)')
plt.title('Scatter Plot of Height, Weight, and BMI')
plt.colorbar(label='BMI')
plt.show()
