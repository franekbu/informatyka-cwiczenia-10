import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


df = pd.read_csv(filepath_or_buffer='wynik_bmi.txt', sep=';')
print(df)

# Apply the default theme
sns.set_theme()

# Create a visualization
sns.relplot(
    data=df,
    x="wzrost[cm]", y="waga[kg]",
    hue="bmi",
)

plt.show()
