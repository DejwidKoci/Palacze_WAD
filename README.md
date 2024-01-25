# Analiza skupień krajów Europy pod względem liczby palaczy

Link do danych z Eurostatu: https://ec.europa.eu/eurostat/databrowser/view/hlth_ehis_sk3u/default/table?lang=en

W tym projekcie dokonujemy analizy skupień krajów Europy pod względem nawyku  palenia papierosów przez obywateli w 2019 roku. Chcemy określić, które państwa mają zbliżone właściwości statystyczne w zakresie zwyczajów palenia, dzieląc je na klastry.
W pracy tej skupiliśmy się na selekcji, wizualizacji zebranych zmiennych dot. częstości palenia w krajach europejskich, opisaniu ich za pomocą statystyk opisowych, standaryzacji i poddaniu zabiegom klasteryzacji przy użyciu modeli z biblioteki sci-kit learn języka Python. Następnie jakość podziałów została oceniona metodą wizualną, jak i szeregiem miar opisujących jakość klastrowania, by na koniec wybrać najskuteczniejszą metodę dzielenia państw europejskich na skupienia z podobnymi nawykami odnośnie spożywania wyrobów tytoniowych wewnątrz klastrów. Wybrany podział dokonany został przy użyciu optymalnej metody klastrowania, jak i odpowiedniej liczby klastrów. Na koniec podejmujemy próbę interpretacji wyników, żeby ocenić merytoryczny skład skupień.


## Pliki:
- `Cigarettes.xlsx` - dane z eurostatu w oryginalnej postaci z opisem struktury
- `Data.xlsx` - poprawione dane `Cigarettes.xlsx` wykorzystywane w kodzie Pythona
- `projekt_WAD.ipynb` - plik Jupyter opisujący krok po kroku algorytm postępowania w analizie skupień z użyciem języka Python
- `projekt_WAD.html` - wygenerowany raport na podstawie pliku `projekt_WAD.ipynb`

