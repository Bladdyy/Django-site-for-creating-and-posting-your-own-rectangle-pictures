# Big django site assignment in 3 parts

# First part
### Zadanie
W tym zadaniu należy przygotować serwis internetowy do przeglądania i publikacji obrazków.

Obrazek to grafika w formacie SVG, która składa się z dowolnej ilości dowolnych prostokątów (mogą różnić się położeniem, wielkości i kolorem wypełnienia).

Przykładowy kod poprawnego obrazka
```
<svg width="100" height="100" viewBox="0 0 100 100" version="1.1" xmlns="http://www.w3.org/2000/svg">
    <rect x="0" y="0" width="100" height="100" fill="black"></rect>
    <rect x="25" y="25" width="50" height="50" fill="red"></rect>
    <rect x="10" y="10" width="10" height="10" fill="blue"></rect>
</svg>
```
### Użytkownicy
Z serwisu korzystają trzy typy użytkowników:

* zwykły użytkownik
* artysta (użytkownik z kontem)
* administrator serwisu (użytkownik z kontem administracyjnym)
Każdy kolejny typ ściśle rozszerza dostępne w ramach serwisu akcje poprzedniego typu.

#### Zwykły użytkownik
Po wejściu na stronę serwisu może:
* zobaczyć listę wszystkich opublikowanych obrazków
* wybrać obrazek i zobaczyć jego podgląd bezpośrednio w przeglądarce

#### Artysta
* Może zalogować się do serwisu korzystając z konta utworzonego dla niego przez administratora strony. Ponad to co może zrobić zwykły użytkownik, artysta może edytować obrazki, które są mu przypisane przez administratora strony.
 Edycja oznacza, że może on przerobić dowolny obrazek na dowolny inny. Najbardziej minimalistyczna wersja spełnienia tego wymagania to implementacja dwóch akcji:
* usunięcie wszystkich prostokątów z obrazka (poniżej każdy prostokąt można usunąć z osobna)
* dodanie dowolnego prostokąta na koniec obrazka (tzn. wyświetlającego się na wierzchu)
#### Administrator strony
Jako jedyny ma dostęp do admin panelu django, skąd może:

* zarządzać kontami dla artystów
* tworzyć nowe obrazki i przypisywać je do edycji artystom
* modyfikować wielkość obrazków
### Uwagi
Serwis należy zaimplementować z użyciem framework’a django.

Materiał prawie wystarczający do wykonania zadania jest zawarty w trzech pierwszych częściach oficjalnego tutorial’a django:

* podstawowy setup projektu
* modele
* templaty
Zrozumienie generycznych widoków z tutorial’a czwartego może uprzyjemnić i uprościć pracę, choć czasem wymaga znalezienia jakiegoś magicznego atrybutu celem uzyskania tego co się akurat chce (copilot / chatgpt jest w tym całkiem niezły).

Istotą zadania jest zapewnienie użytkownikowi każdego typu opisanych powyżej funkcjonalności. Rozkład dostępnych akcji na poszczególnych stronach nie musi być taki jak na załączonych zrzutach ekranu. Dodatkowo wygląd strony również nie jest ważny.

Nawigacja po serwisie powinna być możliwa jedynie z użyciem linków dostępnych na poszczególnych stronach (bez posługiwania się paskiem przeglądarki w tym przyciskiem wstecz).

Do logowania i wylogowywania artystów można użyć intefejsu zapewnionego przez panel administracyjny django. W takim wypadku powinni oni mieć ustawioną flage staff member, ale nie mogą mieć uprawnień do edycji niczego z użyciem admin panelu.

Nie trzeba zabezpieczać się przed atakami w stylu: preparuję jakimś zewnętrznym narzędziem żądanie http, które wysłałby inny użytkownik celem modyfikacji jego obrazka. Wystarczy, że taka niechciana akcja nie będzie jawnie dostępna na stronie. Niemniej warto pomyśleć, w których miejscach strony może to stanowić potencjalne zagrożenie.

# Second part
### Zadanie
W tym zadaniu należy przygotować przeglądarkę do obrazków (tzw. strona główna). Należy do tego użyć Django oraz Bootstrapa albo TailwindCSS (można użyć obu).

### Zmiany w modelu
* Model obrazka powinien zawierać dodatkowe pole opis (tekstowy, nieobowiązkowy).
* Model obrazka powinien zawierać dodatkowe pole data_publikacji (data i czas publikacji obrazka, obowiązkowy).
* Model obrazka powinien zawierać listę tagów (pole tags), które są przypisane do obrazka. Tagi mogą być zewnętrznym modelem, albo polem w modelu odbrazka.
Dla tych zmian należy przygotować migrację.

### Strona główna
Na stronie głównej powinny się pojawiać:

* Lista (paginowana, czyli np. 10 na stronę) wszystkich obrazków. Każdy obrazek powinien być wyświetlany jako miniaturka (np. 100x100 pikseli). Po kliknięciu na miniaturkę użytkownik powinien być przekierowany na stronę z pełnym obrazkiem.
* Możliwość filtrowania obrazków po tagach.
* Możliwość sortowania obrazków po dacie publikacji (rosnąco i malejąco).
Paginację można zrobić korzystając z Paginator’a https://docs.djangoproject.com/en/5.0/topics/pagination/

# Third part
### Ogólnie
W tym zadaniu należy przygotować serwis RESTowy w oparciu o fastAPI, zaprezentować automatyczną dokumentację tego serwisu oraz przetestować go za pomocą curla.

### Zadania
* Zaimplementuj end-point listujący wszystkie tagi wraz z liczbą obrazków przypisanych do danego tagu. End-point powinien być dostępny pod ścieżką /tags.
* Zaimplementuj end-point listujący wszystkie obrazki wraz z ich tagami. End-point powinien być dostępny pod ścieżką /images.
* Zaimplementuj end-point listujący wszystkie obrazki przypisane do danego tagu. End-point powinien być dostępny pod ścieżką /images/{tag}.
* Zaimplementuj end-point kasujący obrazki. End-point powinien być dostępny pod ścieżką /images/del. Identyfikatory obrazków do skasowania powinny być przekazane w formie JSONa.
