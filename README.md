# Palacze_WAD

Wszystkie pliki na razie zostały przeniesione do branchu `Etap_01`.

Link do danych z Eurostatu: https://ec.europa.eu/eurostat/databrowser/view/hlth_ehis_sk3u/default/table?lang=en

## Pliki:
- `Cigarettes.xlsx` - dane z eurostatu w oryginalnej postaci z opisem struktury
- `Data.xlsx` - poprawione dane `Cigarettes.xlsx` wykorzystywane w kodach Pythona
- `analiza.py` - kod, w którym policzono wstępne statystyki (wyeksportowane do `statystyki.xlsx`), dodatkowo wykreowano boxploty i wykresy słupkowe, które zostały wyeksportowane do folderów `boxplots` oraz `plots`. Osobiście uważam, że wykresy w lepszej postaci będą wyglądały z excela xd
- `ward.py` - wstępna implementacja metody Warda
- `k-means.py` - wstępna implementacja metody k-średnich
- `quality_model.py` - analiza indeksu Calińskiego i Harabasz
