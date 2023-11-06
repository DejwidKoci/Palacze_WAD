import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('Data.xlsx')

df.fillna(0, inplace=True)

Y = df['SMOKING (Labels)']
X = df.drop(columns=['SMOKING (Labels)'])


# statystyki
statystyki = []

for kolumna in X.columns:
    odchylenie_std = X[kolumna].std()
    srednia = X[kolumna].mean()
    mediana = X[kolumna].median()
    wariancja = X[kolumna].var()
    kurtoza = X[kolumna].kurtosis()
    skosnosc = X[kolumna].skew()
    wsp_zm = odchylenie_std / srednia
    statystyki.append([kolumna, srednia, mediana, wariancja, kurtoza, skosnosc, odchylenie_std, wsp_zm])

statystyki_df = pd.DataFrame(statystyki, columns=['Kolumna', 'Średnia', 'Mediana', 'Wariancja', 'Kurtoza', 'Skośność', 'Odchylenie standardowe', 'Współczynnik zmienności'])

print(statystyki_df)
statystyki_df.to_excel('statystyki.xlsx', index=False)



# boxploty
import os
if not os.path.exists('boxplots'):
    os.makedirs('boxplots')


for kolumna in X.columns:
    plt.figure(figsize=(8, 6))
    plt.boxplot(X[kolumna])
    plt.title(f'Boxplot dla zmiennej: {kolumna}')
    plt.xlabel(kolumna)
    plt.ylabel('Wartości')
    
    plt.savefig(f'boxplots/{kolumna}_boxplot.png')
    plt.close()