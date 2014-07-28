*****************
Wzorce projektowe
*****************

Podstawy OOP - przypomnienie
============================

* Obiekt / Interfejs / Klasa
* Dziedziczenie a składanie obiektów
* Mechanizm delegowania żądań
* SOLID OOP
 
Podstawy OOP
    * Abstrakcja 
    * Enkapsulacja 
    * Polimorfizm 
    * Dziedziczenie 

Abstrakcja
    Każdy obiekt w systemie służy jako model abstrakcyjnego "wykonawcy", który może
    wykonywać pracę, opisywać i zmieniać swój stan oraz komunikować się z innymi
    obiektami w systemie, bez ujawniania, w jaki sposób zaimplementowano dane cechy

Enkapsulacja (ukrywanie implementacji, hermetyzacja)
    Zapewnia, że obiekt nie może zmieniać stanu wewnętrznego innych obiektów w
    nieoczekiwany sposób. Tylko wewnętrzne metody obiektu są uprawnione do zmiany
    jego stanu. Każdy typ obiektu prezentuje innym obiektom swój "interfejs", który
    określa dopuszczalne metody współpracy

Polimorfizm
    Referencje i kolekcje obiektów mogą dotyczyć obiektów różnego typu, a wywołanie
    metody dla referencji spowoduje zachowanie odpowiednie dla pełnego typu obiektu
    wywoływanego. Jeśli dzieje się to w czasie działania programu, to nazywa się to
    późnym wiązaniem lub wiązaniem dynamicznym

Dziedziczenie
    Porządkuje i wspomaga polimorfizm i enkapsulację dzięki umożliwieniu
    definiowania i tworzenia specjalizowanych obiektów na podstawie bardziej
    ogólnych. Dla obiektów specjalizowanych nie trzeba redefiniować całej
    funkcjonalności, lecz tylko tę, której nie ma obiekt ogólniejszy
 
Obiekt / Interfejs / Klasa
--------------------------

Obiekt  
    * Zawiera zarówno dane składowe jak i operujące na nich metody 
    * Wykonuje operacje po otrzymaniu żądania (lub komunikatu) od klienta (innego obiektu) 
    * Wewnętrzny stan obiektu jest zaenkapsulowany 
 
Interfejs
    obiektu określa kompletny zbiór żądań, jakie mogą być wysyłane do obiektu 

    * Interfejs obiektu nie mówi nic o implementacji obiektu - różne obiekty mają prawo różnie implementować żądania 
    * Implementacja obiektu jest zdefiniowana przez jego klasę.  

Klasa
    specyfikuje dane składowe obiektu i ich reprezentację oraz definiuje operacje, które obiekt może wykonywać 

    * Obiekty powstają w wyniku tworzenia egzemplarzy klas 
    * Za pomocą dziedziczenia klas można definiować nowe klasy w kategoriach klas już istniejących 
 
Klasa abstrakcyjna
    klasa, której głównym celem jest zdefiniowanie  wspólnego interfejsu dla jej podklas (klas pochodnych)

    * Operacje, które klasa abstrakcyjna deklaruje, ale których nie implementuje, nazywa się operacjami abstrakcyjnymi  
    * Klasy, które nie są abstrakcyjne, nazywamy klasami konkretnymi 

Polimorfizm
    * Wykazywanie różnych form działania podczas wywoływania metody w zależności od tego jakiego typu obiekt jest wskazywany przez wskaźnik lub referencję (pomijając typ wskaźnika lub referencji) 
    * Umożliwia zastępowanie w czasie wykonywania programu jednych obiektów drugimi, jeśli mają identyczny interfejs 
    * Skojarzenie żądania z obiektem i z jedną z jego operacji podczas wykonywania programu nazywa się wiązaniem dynamicznym 

Podstawowe techniki OOP
-----------------------

* Dziedziczenie 
* Składanie 
* Delegowanie 

Dziedziczenie
^^^^^^^^^^^^^

Dziedziczenie - rodzaje
    * Dziedziczenie implementacji 

        - Definiuje implementację obiektu w kategoriach implementacji innego obiektu 
        - Jest to mechanizm do współdzielenia kodu i reprezentacji 
        - Dziedziczenie implementacji można aproksymować dziedziczeniem prywatnym 

    * Dziedziczenie interfejsu 

        - Określa, kiedy jeden obiekt może być używany zamiast drugiego 
        - Standardowym sposobem dziedziczenia interfejsu w C++ jest publiczne dziedziczenie po klasie, która ma (czysto) wirtualne funkcje składowe 
 
Programowanie nakierowane na interfejsy
    Odwoływanie się do obiektów wyłącznie przy pomocy interfejsu zdefiniowanego przez klasę abstrakcyjną redukuje zależności implementacyjne w projekcie.
    Ma dwie zalety: 
      * Klienci pozostają nieświadomi specyficznego typu używanych przez siebie obiektów, o ile tylko te obiekty zachowują oczekiwany przez klientów interfejs 
      * Klienci pozostają nieświadomi klas implementujących te obiekty. Znają tylko klasę abstrakcyjną definiującą ten interfejs 
 
**Wady dziedziczenia klas**

* Narusza enkapsulację - ujawnia klasie pochodnej szczegóły implementacji jej klas bazowych 
* Zależności implementacyjne mogą powodować problemy przy próbie ponownego użycia klasy pochodnej 
 
Składanie obiektów (kompozycja)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Składanie obiektów (kompozycja) 
    Utworzenie nowego typu obiektu poprzez złożenie innych już istniejących typów obiektów

    * Jest definiowane dynamicznie podczas wykonywania programu za pośrednictwem obiektów, które pozyskują odwołania (referencje lub wskaźniki) do innych obiektów 
    * Nie prowadzi do naruszenia hermetyzacji, ponieważ dostęp do obiektów jest możliwy jedynie poprzez ich interfejsy.

**Składanie obiektów - zalety**

* Preferowanie składania obiektów zamiast dziedziczenia klas ułatwia podtrzymywanie hermetyzacji klas i pomaga ukierunkować klasy na pojedyncze zadania (SRP) 
* Klasy i ich hierarchie pozostają niewielkie 

Delegowanie
^^^^^^^^^^^
 
Delegowanie żądań
    * Bardziej uniwersalny od dziedziczenia sposób rozszerzania zachowania klasy 
    * Dwa obiekty są zaangażowane w obsługę żądania - obiekt przyjmujący żądanie przekazuje operacje swojemu delegatowi 
 
Delegowanie
    * Zaleta - umożliwia składanie zachowań w czasie wykonywania programu - obiekt przyjmujący żądanie może zmieniać swoje zachowanie 
    * Wada - dynamiczne, wysoce sparametryzowane oprogramowanie jest trudniej zrozumieć niż oprogramowanie bardziej statyczne 
 
Relacje między klasami
----------------------

**Asocjacja / Agregacja / Kompozycja**

    * Asocjacja (znajomość) 

          - Jeden obiekt wie o drugim obiekcie 
          - Zaznajomione obiekty mogą żądać od siebie nawzajem wykonywania swoich operacji 
          - Luźne powiązanie między obiektami 
    * Agregacja  

          - Jeden obiekt jest właścicielem drugiego lub jest za niego odpowiedzialny 
          - Agregowany obiekt może  (ale nie musi) być współdzielony 
    * Kompozycja 

          - Jeden obiekt jest właścicielem drugiego 
          - Wymaga, by obiekt zagregowany miał taki sam czas życia jak jego właściciel 
          - Istnienie obiektu podrzędnego poza właścicielem nie ma sensu  
 
Zasady OOP
----------

* Dobre projekty zorientowane obiektowo: 

    - Powinny nadawać się do wielokrotnego użytku 
    - Być proste do rozbudowy 
    - Być łatwe w serwisowaniu i modyfikacji 
 
Wytyczne dobrego OOD/OOP
^^^^^^^^^^^^^^^^^^^^^^^^

- Programuj pod kątem interfejsu, a nie implementacji 
- Preferuj składanie obiektów, a nie dziedziczenie klas 
- Poddawaj hermetyzacji to co się zmienia 
- Preferuj luźne powiązania między obiektami, które ze sobą współpracują 
- Klasy powinny być otwarte na rozszerzanie, a zamknięte na modyfikację 
- Przypisuj każdej klasie jeden zakres odpowiedzialności 
 
S.O.L.I.D. OOP
--------------

* Single Responsibility Principle 
* Open/Closed Principle 
* Liskov Substitution Principle 
* Interface Segregation Principle 
* Dependency Inversion Principle 
 
Zasada pojedynczej odpowiedzialności
    * Zasada pojedynczej odpowiedzialności (SRP) - każdy obiekt w kodzie
      powinien mieć tylko jedną odpowiedzialność, a wszystkie usługi tego
      obiektu powinny koncentrować się na jej realizacji 
    * Jeśli dla każdego obiektu w systemie istnieje tylko jeden powód do jego
      modyfikacji, oznacza to, że zasada pojedynczej odpowiedzialności została
      zaimplementowana prawidłowo. 
 
Zasada otwarte/zamknięte
    * Zasada otwarte-zamknięte (Open/Close Principle) - klasy powinny być
      otwarte na rozbudowę i zamknięte na modyfikacje. 
    * Jeśli dysponujemy klasą o określonym zachowaniu, które działa prawidłowo,
      należy uniemożliwić wprowadzenie modyfikacji w jej działającym kodzie 
    * W przypadku konieczności rozbudowy kodu, należy stworzyć klasy pochodne,
      w których można przesłonić wybrane metody i dostosować ich działanie do
      bieżących potrzeb 
    * Choć nie można modyfikować kodu klasy (zasada zamknięte), to jednak jest
      ona otwarta na rozbudowę (zasada otwarte). 
 
Zasada otwarte/zamknięte
    * Naruszenie OCP 
    * Poprawione rozwiązanie 
 
Zasada podstawiania Liskov
    * Zasada podstawiania Liskov (*Liskov Substitution Principle*) - musi istnieć
      możliwość podstawiania typów pochodnych w miejsce ich typów bazowych. 
    * LCP dotyczy prawidłowo zaprojektowanego dziedziczenia 

          - Tworząc klasę pochodną, musimy być w stanie użyć jej zamiast klasy
            bazowej 
          - Jeśli nie ma takiej możliwości, to dziedziczenie zostało
            nieprawidłowo użyte 
 
    * Oprócz dziedziczenia istnieje kilka technik używania zachowań
      zdefiniowanych w innych klasach: 
          - Delegowanie - wykonanie zadania można delegować do innej klasy,
            jeśli nie chcemy zmieniać sposobu jego realizacji, a jego
            implementacja nie należy do odpowiedzialności danego obiektu. 
          - Kompozycja - zebranie niezbędnych zachowań zdefiniowanych w jednej
            lub kilku klasach, a także w całych rodzinach klas. Wszystkie
            obiekty należące do kompozycji całkowicie należą do obiektu, który
            ich używa i nie mogą istnieć poza nim. 
          - Agregacja - używana, kiedy chcemy skorzystać z zachowań
            zdefiniowanych w innych klasach, bez ograniczania czasu życia tych
            zachowań.  
 
Zasada segregacji interfejsów
    * Zasada segregacji interfejsów (Interface Segregation Principle) -klient
      nie powinien być zmuszany do zależności od metod, których nie używa. 
    * Jeśli klient zależy od klasy zawierającej metodę, której ten klient nie
      używa, ale której używają pozostałe klasy klienckie, to zmiany tych klas
      będą miały wpływ na naszą klasę 
    * Aby uniknąć tego rodzaju związków, należy podzielić interfejsy 
    * Najlepszym sposobem zapewnienia zgodności z zasadą ISP jest zastosowanie
      techniki dziedziczenia wielokrotnego 

          - Mimo że obiekty klienckie dwóch klas bazowych mogą korzystać z tego
            samego interfejsu, żadna z tych klas nie jest zależna od tego
            interfejsu 
          - Oznacza to, że obiekty kliencie korzystają z tego samego obiektu za
            pośrednictwem różnych interfejsów 
 
Zasada odwracania zależności (*Dependency Inversion Principle*)
    * Moduły wysokopoziomowe nie powinny zależeć od modułów niskopoziomowych.
      Obie grupy modułów powinny zależeć od abstrakcji 
    * Abstrakcje nie powinny zależeć od szczegółowych rozwiązań. To szczegółowe
      rozwiązania powinny zależeć od abstrakcji. 
    * Tradycyjnie programowanie proceduralne prowadzi do powstawania struktur
      złożoności, w których ogólna strategia jest uzależniona od szczegółowych
      rozwiązań w zakresie implementacji 

          - Istnienie takich zależności jest o tyle niekorzystne, że czyni
            strategię wrażliwą na zmiany szczegółów 

    * Programowanie obiektowe odwraca tę strukturę zależności w taki sposób,
      aby zarówno szczegóły, jak i strategie zależały od abstrakcji 

          - W modelu obiektowym interfejsy usług są często przypisane do swoich klientów 
          - Odwracanie zależności jest swoistym certyfikatem dobrego projektu obiektowego 
 

Wzorce projektowe
=================

.. epigraph::

    Wzorzec opisuje problem występujący wielokrotnie w danym środowisku,
    pokazując podstawowe rozwiązanie tego problemu dane w taki sposób, aby można
    wielokrotnie użyć tego rozwiązania do wszystkich wystąpień danego problemu, bez
    konieczności ponownego wykonywania tych samych czynności projektowych

    -- Christopher Alexander  "A Pattern Language", 1977
 
Wzorce projektowe - zalety
    * Znakomicie sprawdziły się w wielu rzeczywistych aplikacjach systemów
      zorientowanych obiektowo 
    * Wskazują sposoby tworzenia całych systemów posiadających cechy
      charakterystyczne dobrych projektów zorientowanych obiektowo 
    * Nie udostępniają gotowego kodu, a jedynie ogólne sposoby rozwiązywania
      problemów pojawiających się w fazie projektowania 
    * Wzorce zwykle odnoszą się do sytuacji, w których w danym oprogramowaniu
      muszą zostać dokonane określone zmiany - umożliwiają hermetyzację
      elementów wykazujących się częstą zmiennością 
    * Większość wzorców umożliwia modyfikowanie pewnych fragmentów systemu
      całkowicie niezależnie od pozostałych elementów systemu 
    * Wzorce zapewniają rodzaj wspólnego, jednolitego języka, który może
      maksymalizować efektywność komunikacji pomiędzy poszczególnymi członkami
      zespołu 
 
**Wzorzec projektowy**

    * Wzorzec dostarcza abstrakcyjnego opisu problemu projektowego i tego jak
      ogólny układ elementów (klas i obiektów) rozwiązuje ten problem. 
    * Wzorzec projektowy ma cztery zasadnicze elementy: 

         1. Nazwa wzorca - skrót, którego można użyć do zwięzłego określenia
            problemu projektowego, jego rozwiązania i konsekwencji. Umożliwia
            projektowanie na wyższym poziomie abstrakcji. 
         2. Problem - określa, kiedy stosować dany wzorzec. 
         3. Rozwiązanie - opis elementów składających się na rozwiązanie
            zdefiniowanego problemu, ich związki, zobowiązania i współpraca.
            Nie opisuje konkretnego projektu lub implementacji.  
         4. Konsekwencje - zalety oraz wady zastosowania wzorca. 
 
Atrybuty wzorca
---------------

 Opis wzorców projektowych
    * Nazwa wzorca i jego kategoria 

          - Odzwierciedla problem, rozwiązanie i konsekwencje danego wzorca 

    * Kontekst/Problem 

          - Kontekst - powtarzająca się sytuacja, w której można zastosować wzorzec  
          - Problem - cel, który chcemy osiągnąć w tym kontekście 

    * Rozwiązanie - Struktura/Uczestnicy/Współpraca 

          - Opisuje uniwersalne rozwiązanie problemu - elementy tworzące projekt, ich relacje, odpowiedzialności oraz współpracę

    * Konsekwencje 

          - Rezultaty zastosowania wzorca - rachunek korzyści i strat  stosowania wzorca 

    * Implementacja
     
          - Przykład implementacji wzorca 
          - Pułapki/wskazówki/techniki implementacyjne wzorca 

    * Wzorce pokrewne 

          - Lista wzorców projektowych, które są związane z opisywanym wzorcem 
 
Klasyfikacja wzorców wg GOF
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Kreacyjne (*Creational*)
    Dotyczą procesu tworzenia obiektu 

Strukturalne (*Structural*) 
    Dotyczą struktury klas lub obiektów 

Czynnościowe (*Behavioral*) 
    Charakteryzują sposób, w jaki klasy lub obiekty oddziałują między sobą i dzielą odpowiedzialności 
 
Projektowanie pod kątem zmian

* Projekt, w którym nie bierze się pod uwagę możliwości dokonywania zmian,
  może wymagać w przyszłości całkowitego przeprojektowania 
* Zmiany mogą wiązać się z koniecznością przedefiniowywania klas i ich
  powtórną implementację, modyfikację klientów i ponowne testowanie 
* Wzorce projektowe gwarantują, że system może się zmieniać w określony
  sposób - każdy wzorzec projektowy dopuszcza niezależne zmiany pewnych
  aspektów struktury systemu 

Katalog wzorców projektowych
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 
* Tworzenie obiektów przez jawne podanie klasy 

      - Factory Method 
      - Abstract Method 
      - Prototype 

* Zależność od specyficznych operacji 

      - Command 
      - Chain of Responsibility 

* Zależność od platformy sprzętowej lub programowej 

      - Abstract Factory 
      - Bridge 
 
* Zależność od reprezentacji obiektów lub ich implementacji 

      - Abstract Factory 
      - Bridge 
      - Memento 
      - Proxy 

* Zależność od algorytmu 

      - Builder 
      - Iterator 
      - Template Method 
      - Strategy 
      - Visitor 
 
*  Ścisłe powiązanie 

      - Abstract Factory 
      - Facade 
      - Chain of Responsibility 
      - Mediator 
      - Bridge 
      - Observer 
      - Command 

* Rozszerzanie funkcjonalności klas 

      - Decorator 
      - Composite 
      - Strategy 
 
