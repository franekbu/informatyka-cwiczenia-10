import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


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

def add_bmi_zones(axe, min_height: int, max_height: int) -> None:
    height_line = np.linspace(min_height, max_height, 100)

    bmi_zones: list[tuple[float, float, str]] = [
        (0, 18.5, 'yellow'),
        (18.5, 25, 'green'),
        (25, 30, 'yellow'),
        (30, 35, 'orange'),
        (35, 40, 'orange'),
        (40, 80, 'red'),
    ]
    for zone in bmi_zones:

        # retransform bmi formula 
        min_zone_weights = zone[0] * pow((height_line / 100), 2)
        max_zone_weights = zone[1] * pow((height_line / 100), 2)

        axe.plot(height_line, min_zone_weights, color=zone[2], linestyle='--', alpha=0.5)
        axe.plot(height_line, max_zone_weights, color=zone[2], linestyle='--', alpha=0.5)
        axe.fill_between(height_line, min_zone_weights, max_zone_weights, color=zone[2], alpha=0.15)
    
    axe.set_ylim(bottom=30, top=150)

def prepare_scatter_plot(data: pd.DataFrame, axe) -> None:
    add_bmi_zones(
        axe=axe,
        min_height=data['wzrost[cm]'].min(),
        max_height=data['wzrost[cm]'].max(),
    )
    sns.scatterplot(
        data=data,
        x="wzrost[cm]", 
        y="waga[kg]",
        hue="bmi",
        palette=pallet,
        # facecolor='grey',
        edgecolor='black',
        size="bmi",
        sizes=(15, 200),
        ax=axe
    )

    axe.set_title("Relacja waga vs wzrost")


def prepare_histplot_plot(data: pd.DataFrame, axe):
    sns.histplot(
        data=data,
        x='bmi_category',
        hue='bmi_category',
        palette=pallet,
        discrete=True,
        shrink=0.8,
        legend=False,
        ax=axe
    )
    axe.set_title("Liczebność kategorii BMI")


def prepare_box_plot(data: pd.DataFrame, axe) -> None:
    sns.boxplot(
        data=data,
        x='bmi_category',
        y='waga[kg]',
        hue='bmi_category',
        palette=pallet, #type: ignore
        ax=axe
    )
    axe.set_title("Rozkład wagi w kategoriach BMI")

def combined_plots(data: pd.DataFrame) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(18,6))

    prepare_scatter_plot(data=data, axe=axes[0])
    prepare_histplot_plot(data=data, axe=axes[1])
    prepare_box_plot(data=data, axe=axes[2])

    plt.tight_layout()
    plt.show()

def main() -> None:
    data = get_data('wynik_bmi.txt')
    combined_plots(data=data)


if __name__ == '__main__':
    main()
