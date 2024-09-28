## Spis treści

- [Wprowadzenie](#wprowadzenie)
- [Zbieranie danych](#zbieranie-danych)
- [Przetwarzanie i analiza danych](#przetwarzanie-i-analiza-danych)


## Wprowadzenie

Rynek kart graficznych jest dynamiczny i pełen różnorodnych modeli, co może sprawić trudności w wyborze odpowiedniego sprzętu. Celem tego projektu jest zebranie i analiza danych dotyczących kart graficznych dostępnych na stronie [morele.net](https://www.morele.net/kategoria/karty-graficzne-12). 

## Zbieranie danych

Pobrane cechy kart graficznych:

- **Tytuł** produktu
- **Cena**
- **Długość karty**
- **Ilość pamięci RAM**
- **Rodzaj chipsetu**
- **Taktowanie rdzenia w trybie boost**

Dane zostały pobrane z pierwszych 10 stron kategorii kart graficznych na morele.net i zapisane w pliku `products.csv`. Do zbierania danych zostały wykorzystane techniki web scrapingu z użyciem biblioteki **BeautifulSoup**.

## Przetwarzanie i analiza danych

### Import i wstępne przetwarzanie danych

Aby móc efektywnie analizować zebrane dane, konieczne było ich wstępne przetworzenie:

- **Czyszczenie danych**: Usunięto zbędne znaki, takie jak spacje, znaki walut czy jednostki miary, aby umożliwić konwersję do odpowiednich typów danych.
- **Konwersja typów danych**: Kolumny zawierające wartości liczbowe zostały przekonwertowane na typy numeryczne (`int`, `float`), co pozwala na wykonywanie operacji matematycznych i statystycznych.
- **Obsługa brakujących danych**: Zidentyfikowano i odpowiednio obsłużono wartości brakujące (`NaN`), aby nie zaburzały wyników analizy.

