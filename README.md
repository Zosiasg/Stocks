# Stocks App
Dokumentacja projektu - Portal sprawdzający kursy akcji
Autorzy: [Zofia Syrek-Gerstenkorn, Alena Mikhalkiewicz] Data: [06.06.2023]

Wprowadzenie
Projekt "Portal sprawdzający kursy akcji" jest aplikacją webową napisaną w języku Python z wykorzystaniem frameworku Flask. Aplikacja umożliwia użytkownikom sprawdzanie kursów akcji na podstawie informacji pobieranych ze strony https://www.marketwatch.com/investing/stock/. Użytkownicy mają możliwość logowania i rejestracji, a następnie mogą wybrać akcję z listy lub wpisać symbol akcji, która ich interesuje. Po wybraniu akcji, użytkownik otrzymuje informacje takie jak Stock Price, Closing Price, 52-Week Range oraz Analyst Rating.

Jak uruchomić projekt
Aby uruchomić projekt, należy postępować zgodnie z poniższymi krokami:
1.	Sklonuj repozytorium projektu (https://github.com/Zosiasg/Stocks.git) na swój lokalny komputer.
2.	Upewnij się, że masz zainstalowaną najnowszą wersję Pythona na swoim systemie.
3.	Otwórz projekt w środowisku Visual Studio Code.
4.	Zainstaluj wymagane biblioteki, korzystając z menedżera pakietów pip. W terminalu Visual Studio Code wykonaj poniższą komendę:
pip install flask sqlalchemy beautifulsoup4 requests 
5.	Uruchom projekt, wykonując poniższą komendę w terminalu:
python app.py 
lub przyciskiem: run python file
6.	Aplikacja zostanie uruchomiona

Informacje o bibliotekach
Projekt wykorzystuje następujące biblioteki:
1.	Flask - framework webowy napisany w języku Python, służący do budowy aplikacji internetowych.
2.	Sqlite - baza danych wbudowana w Pythona, służąca do przechowywania informacji o użytkownikach i akcjach.
3.	SQLAlchemy - narzędzie umożliwiające łatwą pracę z bazami danych w języku Python.
4.	Beautiful Soup - biblioteka do parsowania i ekstrakcji danych z plików HTML i XML.
5.	Requests - biblioteka do wykonywania żądań HTTP.

Opis modułów
1.	main.py - główny moduł aplikacji, uruchamiający aplikację
2.	models.py - moduł zawierający definicje klas modeli używanych do przechowywania danych w bazie danych.
3.	views.py - moduł zawierający kod odpowiedzialny za pobieranie informacji o kursach akcji ze strony https://www.marketwatch.com/investing/stock/.
4.	templates/ - folder zawierający szablony HTML używane do wyświetlania interfejsu użytkownika.
5.	static/ - folder zawierający pliki statyczne, takie jak arkusze stylów CSS czy skrypty JavaScript.

Opis kodu w module views.py
Moduł views.py zawiera implementację funkcji obsługujących widoki aplikacji. Poniżej został opisany przepływ danych oraz funkcjonalność poszczególnych części kodu.
Importowane biblioteki
•	Blueprint - klasa z modułu flask, służąca do definiowania grupy widoków dla aplikacji.
•	render_template - funkcja z modułu flask, używana do renderowania szablonów HTML.
•	request - obiekt z modułu flask, umożliwiający dostęp do informacji o żądaniu HTTP.
•	login_required - dekorator z modułu flask_login, sprawdzający, czy użytkownik jest zalogowany.
•	current_user - obiekt z modułu flask_login, reprezentujący zalogowanego użytkownika.
•	Flask - klasa z modułu flask, służąca do tworzenia instancji aplikacji.
•	requests - biblioteka do wykonywania żądań HTTP.
•	BeautifulSoup - klasa z modułu bs4, używana do analizy i przetwarzania danych HTML.
Blueprint views
Blueprint to grupa powiązanych ze sobą widoków, które mogą być zarejestrowane w aplikacji Flask. W przypadku tego projektu, blueprint views jest używany do zdefiniowania widoków związanych z interfejsem użytkownika.
Funkcja get_stock_data
Funkcja get_stock_data przyjmuje jeden argument stock_symbol, który jest symbolem akcji. Wykorzystuje ten symbol do skonstruowania odpowiedniego URL-a do strony MarketWatch, z której pobierane są informacje o akcji. Następnie funkcja wykonuje żądanie HTTP do strony, pobiera treść odpowiedzi, a za pomocą biblioteki BeautifulSoup parsuje dane i ekstrahuje potrzebne informacje o akcji, takie jak cena, cena zamknięcia, przedział cenowy z ostatnich 52 tygodni oraz ocena analityków. Zwraca te informacje w postaci słownika.

Widok home
Widok home jest dostępny pod adresem głównym „/” aplikacji. Jest również dekorowany dekoratorem login_required, co oznacza, że użytkownik musi być zalogowany, aby uzyskać dostęp do tego widoku.
•	Jeśli metoda żądania HTTP to POST, oznacza to, że użytkownik wysłał formularz na stronie. W takim przypadku odczytuje wartości pól stock_symbol i custom_symbol z żądania i przekazuje je do funkcji get_stock_data, aby pobrać informacje o akcji. Następnie renderuje szablon stock.html, przekazując do niego pobrane informacje o akcji oraz obiekt current_user, który reprezentuje zalogowanego użytkownika.
•	Jeśli metoda żądania HTTP to GET, oznacza to, że użytkownik otworzył stronę po raz pierwszy lub odświeżył ją. W takim przypadku renderuje szablon home.html, przekazując do niego obiekt current_user, który reprezentuje zalogowanego użytkownika.
W przypadku, gdy nie zostanie podany symbol akcji (ani stock_symbol, ani custom_symbol), wyświetlane jest komunikat o błędzie, a użytkownik jest ponownie przekierowany na stronę główną.
Dzięki temu kodowi, aplikacja obsługuje zarówno wyświetlanie strony głównej, jak i przetwarzanie formularza, umożliwiając użytkownikowi wyszukiwanie informacji o kursach akcji.

