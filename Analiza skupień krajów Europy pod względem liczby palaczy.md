## Autorzy: 
Adam Dohojda, Kacper Kiereś, Dawid Koceniak, Wiktoria Stęczna

## Streszczenie

W tym projekcie dokonujemy analizy skupień krajów Europy pod względem liczby palaczy. Chcemy określić, które państwa mają zbliżone właściwości statystyczne, dzieląc je na klastry. 

W pierwszej kolejności zaczęliśmy od przygotowywania danych do analizy.  
Przedstawiliśmy cel badania, dane oraz zmienne wybrane do analizy. Policzyliśmy główne miary statystyczne, a następnie dokonaliśmy doboru zmiennych eliminując zmienne quasi-stałe. 

Następnie przedstawiliśmy opis wybranych metod do analizy skupień - metodę Warda oraz metodę k - średnich. 

Na końcu przedstawiamy wyniki przeprowadzonych analiz wraz z omówieniem rezultatów.

## Słowa kluczowe

- skupienia

## Wprowadzenie



## Cel badania
  
Zadaniem zespołu było wymodelowanie skupień, do których zostaną przydzielone kraje Unii Europejskiej na podstawie 24 zmiennych. Do osiągnięcia tego celu zostały zbudowane skupienia za pomocą metody Warda oraz metody k-średnich. 

## Zmienne wybrane do analizy

Dane wykorzystane w tym projekcie pochodzą z Eurostatu. Zmienne decyzyjne palaczy poszczególnych krajów Europy i to na ich podstawie zostały stworzone skupienia. Opis zmiennych został przedstawiony poniżej:

$X_1$ - procent palących w danym kraju
$X_2$ - procent palących mniej niż 20 papierosów na dzień
$X_3$ - procent palących więcej niż 20 papierosów na dzień
$X_4$ - procent palących zamieszkujących tereny metropolii miejskich
$X_5$ - procent palących zamieszkujących tereny małych miast
$X_6$ - procent palących zamieszkujących tereny wiejskie
$X_7$ - procent palących mężczyzn
$X_8$ - procent palących kobiet
$X_9$ - procent palących z przedziału wiekowego 15 - 19 lat
$X_{10}$ - procent palących z przedziału wiekowego 15 - 24 lata
$X_{11}$ - procent palących z przedziału wiekowego 15 - 29 lat
$X_{12}$ - procent palących z przedziału wiekowego 15 - 64 lata
$X_{13}$ - procent palących z przedziału wiekowego 18 - 24 lata
$X_{14}$ - procent palących posiadających co najmniej 18 lat.
$X_{15}$ - procent palących z przedziału wiekowego  20 - 24 lata
$X_{16}$ - procent palących z przedziału wiekowego 25 - 29 lata
$X_{17}$ - procent palących z przedziału wiekowego 25 - 34 lata
$X_{18}$ - procent palących z przedziału wiekowego 35 - 44 lata
$X_{19}$ - procent palących z przedziału wiekowego 45 - 54 lata
$X_{20}$ - procent palących z przedziału wiekowego 45 - 64 lata
$X_{21}$ - procent palących z przedziału wiekowego 55 - 64 lata
$X_{22}$ - procent palących z przedziału wiekowego 65 - 74 lata
$X_{23}$ - procent palących posiadających co najmniej 65 lat
$X_{24}$ - procent palących posiadających co najmniej 75 lat

Założyliśmy, że wszystkie zmienne są destymulantami. 
Po dokonaniu analizy zmiennych quasi stałych stwierdziliśmy brak takich zmiennych. 

Dane nie zostały poddane żadnym dodatkowym zabiegom unitaryzacji albo normalizacji. Były one podane w postaci procentowi i zespołowo stwierdziliśmy, że nie będziemy zmieniać sposobu wizualizacji tych danych.


## Braki danych
Występują cztery puste komórki. Zostały do nich dopisane zera.





## Wstępna analiza danych

### Statystyki opisowe

| Kolumna | Średnia | Mediana | Wariancja | Kurtoza | Skośność | Odchylenie standardowe | Współczynnik zmienności |
|---------|---------|---------|-----------|---------|----------|------------------------|-------------------------|
| X1      | 17,672  | 18,550  | 29,932    | -0,229  | -0,190   | 5,471                  | 0,310                   |
| X2      | 11,372  | 11,950  | 7,882     | -0,493  | -0,564   | 2,808                  | 0,247                   |
| X3      | 6,322   | 5,400   | 13,426    | 0,737   | 1,060    | 3,664                  | 0,580                   |
| X4      | 15,616  | 17,250  | 43,084    | 0,510   | -0,715   | 6,564                  | 0,420                   |
| X5      | 16,016  | 17,700  | 44,264    | 0,655   | -0,706   | 6,653                  | 0,415                   |
| X6      | 16,163  | 18,050  | 44,280    | 0,513   | -0,768   | 6,654                  | 0,412                   |
| X7      | 22,078  | 22,650  | 67,886    | -0,167  | 0,138    | 8,239                  | 0,373                   |
| X8      | 13,666  | 13,850  | 18,595    | -0,092  | 0,201    | 4,312                  | 0,316                   |
| X9      | 11,350  | 10,750  | 22,093    | 0,468   | 0,222    | 4,700                  | 0,414                   |
| X10     | 12,681  | 13,200  | 20,306    | 0,210   | -0,543   | 4,506                  | 0,355                   |
| X11     | 15,572  | 16,800  | 28,754    | -0,066  | -0,785   | 5,362                  | 0,344                   |
| X12     | 20,353  | 21,800  | 44,075    | -0,190  | -0,268   | 6,639                  | 0,326                   |
| X13     | 16,384  | 17,350  | 32,493    | 0,269   | -0,624   | 5,700                  | 0,348                   |
| X14     | 18,213  | 19,300  | 31,784    | -0,179  | -0,162   | 5,638                  | 0,310                   |
| X15     | 18,441  | 19,450  | 41,020    | 0,230   | -0,716   | 6,405                  | 0,347                   |
| X16     | 20,609  | 22,150  | 52,613    | -0,192  | -0,770   | 7,253                  | 0,352                   |
| X17     | 21,256  | 23,200  | 57,931    | -0,398  | -0,600   | 7,611                  | 0,358                   |
| X18     | 22,419  | 23,700  | 61,657    | 0,179   | 0,078    | 7,852                  | 0,350                   |
| X19     | 22,469  | 22,600  | 59,204    | 0,400   | 0,174    | 7,694                  | 0,342                   |
| X20     | 21,750  | 22,550  | 47,489    | 0,019   | 0,101    | 6,891                  | 0,317                   |
| X21     | 20,978  | 21,450  | 39,975    | -0,357  | 0,067    | 6,323                  | 0,301                   |
| X22     | 12,181  | 12,200  | 14,054    | -0,552  | 0,051    | 3,749                  | 0,308                   |
| X23     | 8,750   | 8,750   | 6,653     | -0,005  | 0,111    | 2,579                  | 0,295                   |
| X24     | 4,394   | 4,400   | 2,098     | -0,623  | -0,071   | 1,448                  | 0,330                   |


(interpretacje)


### Boxploty


### Wykresy





## Opis metod

### Metoda Warda

**Metoda Warda** to jedna z aglomeracyjnych metod grupowania, którą spośród pozostałych wyróżnia wykorzystanie podejścia analizy wariancji do oszacowania odległości między skupieniami. Zmierza ona do minimalizacji sumy kwadratów odchyleń dowolnych dwóch skupień, które mogą zostać uformowane na każdym etapie. Traktowana jest jako bardzo efektywna, chociaż zmierza do tworzenia skupień o małej wielkości. Daje pełną kontrolę nad wynikową liczbą grup oraz przedstawia najbardziej naturalne skupiska elementów.
Kolejność postępowania w metodzie Warda jest podobna jak w pozostałych metodach aglomeracyjnych. Znaczące różnice występują w użytych we wzorze parametrach. Schemat postępowania wygląda następująco:

1. Wyznaczenie macierzy odległości taksonomicznych o wymiarach $n \times n$, która zawiera odległość każdej pary obiektów. Macierz ta jest symetryczna względem głównej przekątnej, którą stanowią same zera.
2. Wyszukanie par obiektów (a w dalszej części skupień), dla których wzajemna odległość jest najmniejsza. Przyjąć należy, że obiekty te mają numery $p$ i $q$, przy czym $p<q$.
3. Złączenie $p$ i $q$ w jedno nowe skupienie, które zajmuje pozycję o numerze $p$. Jednocześnie usuwa się obiekt (skupienie) o numerze $q$, zaś numery skupień o numerze od niego wyższym zmniejsza się o jeden. W ten sposób wymiar macierzy zmniejsza się o 1.  
    Np. jeżeli dla grupy 10 obiektów łączy się obiekt 4 i 7, nowe skupienie powstaje w miejscu 4, w miejsce obiektu siódmego przechodzi dotychczasowy ósmy, 9 zmienia się w 8 i 10 w 9.  Macierz 10x10 zmienia się w 9x9.
4. Wyznacza się odległość nowego skupienia od każdego pozostałego według wzoru: $$D_{pr} = a_1 \cdot d_{pr} + a_2 \cdot d_{qr} + b \cdot d_{pq}$$
gdzie:
- $r$ przebiega numery skupień różne od $p$ i $q$
- $D_{pr}$ - odległość nowe skupienia od skupienia od skupienia o numerze $r$.
- $d_{pr}$ - odległość pierwotnego skupienia $p$ od skupienia $r$
- $d_{qr}$ - odległość pierwotnego skupienia $q$ od skupienia $r$
- $d_{pq}$ - wzajemna odległość pierwotnych skupień $p$ i $q$
- $a_1$, $a_2$, $b$ - parametry które w metodzie Warda mają wzory: $$a_1 = \frac{n_p + n_r}{n_p + n_q + n_r} \quad  a_2 = \frac{n_q + n_r}{n_p + n_q + n_r} \quad b = \frac{-n_r}{n_p + n_q + n_r}$$ we wzorach tych $n$ oznacza liczebność pojedynczych obiektów w poszczególnych obiektach.

Krok drugi i trzeci powtarza się tak długo, aż wszystkie jednostki zostaną połączone w jedno n-elementowe skupienie.


### Metoda k - średnich

Metoda k-średnich jest metodą należącą do grupy algorytmów analizy skupień tj. analizy polegającej na szukaniu i wyodrębnianiu grup obiektów podobnych (skupień) . Reprezentuje ona grupę algorytmów niehierarchicznych. Główną różnicą pomiędzy niehierarchicznymi i hierarchicznymi algorytmami jest konieczność wcześniejszego podania ilości skupień.

Przy pomocy metody k-średnich zostanie utworzonych k różnych możliwie odmiennych skupień. Algorytm ten polega na przenoszeniu obiektów ze skupienia do skupienia tak długo aż zostaną zoptymalizowane zmienności wewnątrz skupień oraz pomiędzy skupieniami. Oczywistym jest, iż podobieństwo w skupieniu powinno być jak największe, zaś osobne skupienia powinny się maksymalnie od siebie różnić.

Niech $C_k$ -funkcja, która przyporządkowuje obiektowi numer skupienia. Niech $C_k^*$ -funkcja realizująca optymalny podział. Wtedy
$$C_k^* = \arg \min_{C_k} \sum_{j=1}^k \sum_{C_k(i) = j} \rho^2(x_i, \bar{x_j})$$
gdzie $\rho$ - odległość euklidesowa


#### Zasada działania algorytmu jest następująca:

1) w losowy sposób rozmieszamy $m$ obiektów w $k$ skupieniach $(C_k^{(1)})$
2) dla każdego z $k$ skupień obliczamy wektory średnich $\bar{x_j}$ dla $j = 1, \cdots, k$
3) w kroku $I$ ponownie rozmieszamy obiekty do $k$ skupień aby
$$C_k^{(I)}(i) = \arg \min_{1 \leq j \leq k} \rho^2(x_i, \bar{x_j})$$
4) powtarzamy kroki 2) i 3) aż przyporządkowania obiektów do skupień pozostaje niezmienione $C_k^{(I)}(i) = C_k^{(I-1)}(i)$


#### Optymalny wybór k

Niech $W(C_k), B(C_k)$ - macierze zmienności wewnątrz i między skupieniami
$$W(C_k) = \sum_{j = 1}^k \sum_{C_k(i) = j}(x_i - \bar{x_j})(x_i - \bar{x_j})^T$$
$$B(C_k) = \sum_{j = 1}^k n_j(x_j - \bar{x})(x_j - \bar{x})^T$$
gdzie $\bar{x_j}$ - średnia w $j$-tym skupieniu, $\bar{x}$ - średnia ogólna, $n_j$ - liczebność $j$-tego skupienia.

1) rysujemy osypisko np. $W_k = \log(tr(W(C_k)))$, patrzymy gdzie zaczynają się zdecydowane mniejsze różnice $W_1 - W_2, W_2 - W_3, W_3 - W_4$ itd (heurystyczna metoda).

2) Indeks Calińskiego i Harabasza (1974), wybieramy $k$ które maksymalizuje wartość pseudostatystyki $F$ postaci $$CH(k) = \frac{tr(B(C_k))/(k-1)}{tr(W(C_k))/(m - k)}$$
3) maksymalizujemy statystykę odstępu (gap statistic) Hastie, Tibshirani, Walter (2001) postaci $$Gap(k) = W_k^* - W_k$$
gdzie $W_k^*$ - obliczone jest na podstawie danych wygenerowanych z rozkładu jednostajnego na odpowiedniej kostce w $R^p$.







## Rezultaty

![[Pasted image 20231112201405.png]]


![[Pasted image 20231112201425.png]]




## Podsumowanie


## Bibliografia



