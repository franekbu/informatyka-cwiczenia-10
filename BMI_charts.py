import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


pallet = sns.diverging_palette(250, 30, l=65, center="dark", as_cmap=True)

def get_bmi_category(bmi) -> int:
    if bmi < 18.5:
        return 1
    elif bmi < 25:
        return 2
    elif bmi < 30:
        return 3
    elif bmi < 35:
        return 4
    elif bmi < 40:
        return 5
    else:
        return 6

def get_data(file_name: str) -> pd.DataFrame:

    bmi_data = pd.read_csv(filepath_or_buffer=file_name, sep=';')
    bmi_cat = pd.Series(
        [get_bmi_category(row['bmi']) for _, row in bmi_data.iterrows()], 
        name='bmi_category'
    )
    new_df = pd.concat([bmi_data, bmi_cat], axis=1)
    return new_df


# Create a visualization
def get_replot_plot(data: pd.DataFrame) -> None:
    sns.relplot(
        data=data,
        x="wzrost[cm]", 
        y="waga[kg]",
        hue="bmi",
        palette= pallet,
        size="bmi", sizes=(15, 200)
    )
    plt.show()

def get_displot_plot(data):
    sns.displot(
        data=data,
        x='bmi_category',
        palette=pallet,
        hue='bmi_category',
    )
    plt.show()

def main() -> None:
    data = get_data('wynik_bmi.txt')
    get_replot_plot(data=data)
    get_displot_plot(data=data)


if __name__ == '__main__':
    main()
