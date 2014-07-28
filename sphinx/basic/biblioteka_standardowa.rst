**********************
Biblioteka standardowa
**********************

Operacje plikowe
================

.. index:: pliki

Otwieranie plików
-----------------

.. py:function:: open(path [, mode [, buffersize]])

    otwieranie pliku zarówno do odczytu, jak i zapisywania

    * ``path`` – łańcuch znaków określający ścieżkę, wskazujący na dany plik
    * ``mode`` – tryb otwarcia pliku
    * ``buffersize`` – argument opcjonalny, określa, jaki tryb buforowania powinien być stosowany, kiedy uzyskuje się dostęp do pliku

.. code-block:: python

    file = open(inPath, 'rU')
    file = open(outPath, 'wb')

Tryby plików
^^^^^^^^^^^^

``r``
    Otwiera istniejący plik do odczytu
``w``
    Otwiera plik do zapisu. Jeśli plik już istnieje, jego zawartość jest kasowana. Jeśli plik jeszcze nie istnieje, tworzony jest nowy.
``a``
    Otwiera istniejący plik do uaktualnienia, zachowując istniejącą część bez zmian i dodając do niej nową treść.
``r+``
    Otwiera plik zarówno do odczytu, jak i zapisu. Istniejąca treść pozostaje bez zmian.
``w+``
    Otwiera plik zarówno do zapisu, jak i odczytu. Istniejąca treść jest kasowana.
``a+``
    Otwiera plik zarówno do odczytu, jak i zapisu. Istniejąca treść pozostaje bez zmian, a nowa treść jest dodawana do istniejącej.
``b``
    Stosowany w dodatku do jednego z ww. trybów odczytu, zapisu lub dodawania. Otwiera plik w trybie binarnym.
``U``
    Stosowany w dodatku do jednego z ww. trybów odczytu, zapisu lub dodawania. Stosuje uniwersalny translator nowych wierszy do otwieranego pliku.

Tryb buforowania
^^^^^^^^^^^^^^^^

``0``
    Plik nie powinien być buforowany
``1``
    Buforowanie wierszy (line-buffering)
inna liczba dodatnia
    Wskazuje konkretny rozmiar bufora, który ma być wykorzystywany w dostępie
brak argumentu lub liczba ujemna
    Wykorzystywany jest domyślny rozmiar bufora systemu

Otwieranie i zamykanie plików
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. py:function:: close()

    metoda zamykająca plik

Przykład:

.. code-block:: python

    inPath = "input.txt"
    outPath = "output.txt"

    #  Otwarcie pliku do odczytu
    file = open(inPath, 'rU')
    if file:
        #  Tutaj następuje odczytywanie zawartości pliku
        file.close()
    else:
        print( "Przy otwieraniu pliku nastąpił błąd." )

    # Otwarcie pliku do zapisu
    file = open(outPath, 'wb')
    if file:
        # Tutaj następuje zapisywanie czegoś do pliku
        file.close()
    else:
        print( "Przy otwieraniu pliku nastąpił błąd." )

Od Pythona w wersji 2.5 można używać wyrażenia ``with``, tzw. menedżera kontekstu.
Gwarantuje on poprawne zamknięcie pliku nawet w sytuacji wystąpienia wyjątku.

Przykład:

.. code-block:: python

    with open("input.txt", 'r') as f:
        # Operacje na obiekcie pliku
        f.read()

    # zamknięcie pliku

Menedżer kontekstu odpowiada następującej obsłudze wyjątków:

.. code-block:: python

    try:
        f = open("input.txt", 'r')
        f.read()
    finally:
        f.close()

Wyrażenie ``with`` upraszcza pisanie kodu odpornego na wyjątki.

Odczyt
------

.. index::
    double: odczyt pliku; plik odczyt

Odczytywanie całej zawartości pliku
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. py:function:: read()

    wczytuje pełną zawartość pliku aż do napotkania znacznika EOF, a następnie zwraca zawartość pliku w formie łańcucha znaków.

.. py:function:: readlines()

    wczytuje całą zawartość pliku, oddzielając każdy wiersz jako osobny łańcuch znaków, aż do napotkania znacznika EOF i zwraca listę łańcuchów znaków reprezentujących pojedyncze wiersze.

.. py:function:: read(bytes)

    wczytuje określoną liczbę bajtów z pliku i zwraca je w postaci łańcucha znaków. Jeśli pierwszy odczytany znak jest znacznikiem EOF, zwracany jest null.

Przykład:

.. code-block:: python

    filePath = "input.txt"

    # Wczytanie całego pliku do bufora
    buffer = "Bufor całego pliku:\n"
    buffer += open(filePath, 'rU').read()
    print( buffer )

    # Wczytanie wierszy do bufora
    buffer = "Bufor wszystkich wierszy z pliku:\n"
    inList = open(filePath, 'rU').readlines()
    print( inList )
    for line in inList:
        buffer += line
    print( buffer )

    # Wczytanie bajtów do bufora
    buffer = "Bufor odczytu:\n"
    file = open(filePath, 'rU')
    while True:
        bytes = file.read(5)
        if bytes:
            buffer += bytes
        else:
            break
    print( buffer )

::

    Bufor całego pliku:
    Wiersz 1
    Wiersz 2
    Wiersz 3
    Wiersz 4
    ['Wiersz 1\n', 'Wiersz 2\n', 'Wiersz 3\n', 'Wiersz 4\n']
    Bufor wszystkich wierszy z pliku:
    Wiersz 1
    Wiersz 2
    Wiersz 3
    Wiersz 4
    Bufor odczytu:
    Wiersz 1
    Wiersz 2
    Wiersz 3
    Wiersz 4
     

Dostęp do każdego słowa w pliku
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Słowa mogą być przetwarzane pojedynczo poprzez:
 * otwarcie pliku
 * wczytanie każdego wiersza do łańcucha znaków
 * podzielenie łańcuchów na znaki za pomocą funkcji ``split()``

Przykład:

.. code-block:: python

    filePath = "input.txt"
    wordList = []
    wordCount = 0

    # Wczytanie wierszy do pliku
    file = open(filePath, 'rU')
    for line in file:
        for word in line.split():
            wordList.append(word)
            wordCount += 1

    print( wordList )
    print( "Całkowita liczba słów {}".format(wordCount) )

::

    ['Wiersz', '1', 'Wiersz', '2', 'Wiersz', '3', 'Wiersz', '4']
    Całkowita liczba słów = 8

Ustalenie liczby wierszy w pliku
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. py:function:: readlines()

    generowanie listy wierszy. Dla dużych plików używanie readlines() może być niepraktyczne ze względu na ilość pamięci i czas niezbędny do przetwarzania.

.. py:function:: len()

    ustalenie liczby wierszy w liście.

Przykład:

.. code-block:: python

    filePath = "input.txt"
    lineCount = len(open(filePath, 'rU').readlines())
    print( "Liczba wierszy w {} wynosi {}".format(filePath, lineCount) )

::

    Liczba wierszy w pliku input.txt wynosi 4

Zapisywanie do pliku
--------------------

Metody zapisywania danych do pliku:

.. py:function:: write(string)

    zapisuje argument string do pliku w miejscu, w którym aktualnie znajduje się wskaźnik pliku

.. py:function:: writelines(sequence)

    funkcja zazwyczaj przyjmuje listę łańcuchów znaków sequence i zapisuje te łańcuchy do pliku

Można również przekierować funkcję ``print`` do pliku za pomocą argumentu ``file``

Przykład:

.. code-block:: python

    wordList = ["Czerwony", "Niebieski", "Zielony"]
    filePath = "output.txt"
    # Zapisanie listy do pliku
    fileOut = open(filePath, 'w')
    fileOut.writelines(wordList)

    # Zapisanie łańcucha znaków do pliku
    fileOut.write("\n\nSformatowany tekst:\n")

    # Zapisanie listy do pliku
    fileOut = open(filePath, 'w')
    fileOut.writelines(wordList)

    # Zapisanie łańcucha znaków do pliku
    fileOut.write("\n\nSformatowany tekst:\n")

    # Drukowanie bezpośrednio do pliku
    for word in wordList:
        print("\tKontrola koloru: {}".format(word), file=fileOut)
    fileOut.close()

::

    CzerwonyNiebieskiZielony
    Sformatowany tekst:
        Kontrola koloru: Czerwony
        Kontrola koloru: Niebieski
        Kontrola koloru: Zielony


 
Przechodzenie drzewa katalogów
------------------------------

.. py:function:: os.walk(path)

    przechodzi drzewo katalogów i tworzy dla każdego z nich krotkę składającą się ze: ścieżki katalogu, listy nazw katalogów oraz listy nazw plików.

Po utworzeniu krotek mogą być one pojedynczo przetwarzane jako elementy listy z użyciem indeksów

 * 0 – dostęp do reprezentowanej bezpośrednio ścieżki katalogu
 * 1 – dostęp do listy podkatalogów
 * 2 – dostęp do plików zawartych w katalogu

Przykład:

.. code-block:: python

    import os
    path = "/books/python"

    def printFiles(dirList, spaceCount):
        for file in dirList:
            print( "/".rjust(spaceCount+1) + file )

    def printDirectory(dirEntry):
        print dirEntry[0] + "/"
        printFiles(dirEntry[2], len(dirEntry[0]))

    tree = os.walk(path)
    for directory in tree:
        printDirectory(directory)

::

    /books/python/
                 /Python Proposal.doc
            /Python_Phrasebook_TOC.doc
            /python_schedule.xls
            /template.doc
            /TOC_Notes.doc
    /books/python/CH2/
                     /CH2.doc
    /books/python/CH2/code/
                  /comp_str.py
                  /end_str.py
                  /eval_str.py
                  /format_str.py
                  /join_str.py
    /books/python/CH3/
                /CH3.doc

 
Zmiana nazwy pliku
------------------

.. py:function:: os.remove(file)

    wykrycie, czy plik o danej nazwie już istnieje, a następnie ewentualne usunięcie

.. py:function:: os.rename(oldFile, newFile)

    zmiana nazwy pliku

::

    os.remove(newFileName)
    os.rename(oldFileName, newFileName)

Przykład:

.. code-block:: python

    import os
    oldFileName = "/books/python/CH4/code/output.txt"
    newFileName = "/books/python/CH4/code/output.old"

    # Nowy listing
    for file in os.listdir("/books/python/CH4/code/"):
        if file.startswith("output"):
           print( file )
    # Usunięcie pliku, jeśli nowa nazwa już istnieje
    if os.access(newFileName, os.X_OK):
        print( "Usuwanie " + newFileName )
        os.remove(newFileName)
    # Zmiana nazwy pliku
    os.rename(oldFileName, newFileName)
    # Stary listing
    for file in os.listdir("/books/python/CH4/code/"):
        if file.startswith("output"):
           print( file )

::

    output.old
    output.txt
    Usuwanie /books/python/CH4/code/output.old
    output.old


Rekurencyjne kasowanie plików i podkatalogów
--------------------------------------------

Funkcja ``os.walk(path)`` automatycznie tworzy listę krotek, reprezentujących katalogi, które mają być usunięte.
Aby rekurencyjnie skasować drzewo, należy przejść przez listę katalogów i usunąć każdy plik zawarty w liście plików (trzeci element krotki).
Najpierw należy usunąć pliki, a następnie same katalogi w odwrotnej kolejności, rozpoczynając od najgłębiej zagnieżdżonych.

Przykład:

.. code-block:: python

    import os
    emptyDirs = []
    path = "/trash/deleted_files"

    def deleteFiles(dirList, dirPath):
        for file in dirList:
            print( "Usuwanie " + file )
            os.remove(dirPath + "/" + file)

    def removeDirectory(dirEntry):
        print( "Usuwanie plików z " + dirEntry[0] )
        deleteFiles(dirEntry[2], dirEntry[0])
        emptyDirs.insert(0, dirEntry[0])

    # Sporządzenie listy wpisów w drzewie katalogów
    tree = os.walk(path)
    for directory in tree:
        removeDirectory(directory)
    # Usunięcie pustych katalogów
    for dir in emptyDirs:
        print( "Usuwanie " + dir )
        os.rmdir(dir)

::

    Usuwanie plików z /trash/deleted_files
    Usuwanie 102.ini
    Usuwanie 103.ini
    Usuwanie 104.ini
    Usuwanie 105.ini
    Usuwanie 106.ini
    Usuwanie plików z /trash/deleted_files\Test
    Usuwanie 111.ini
    Usuwanie 114.ini
    Usuwanie 115.ini
    Usuwanie plików z /trash/deleted_files\Test\Test2
    Usuwanie 112.ini
    Usuwanie 113.ini
    Usuwanie plików z /trash/deleted_files\Test\Test2
    Usuwanie plików z /trash/deleted_files\Test
    Usuwanie plików z /trash/deleted_files

 
Wyszukiwanie plików w oparciu o rozszerzenie
--------------------------------------------

Tworzymy listę rozszerzeń plików poprzez podzielenie łańcucha znaków wzorca za pomocą funkcji ``split()``.
Sprawdzamy, czy rozszerzenie pliku odpowiada rozszerzeniu znajdującemu się na liście używając funkcji ``endswith(string)`` na nazwie pliku.

Przykład:

.. code-block:: python

    import os
    path = "/books/python"
    pattern = "*.py;*.doc"

    # Wydrukowanie plików, które odpowiadają wybranym rozszerzeniom
    def printFiles(dirList, spaceCount, typeList):
        for file in dirList:
            for ext in typeList:
                if file.endswith(ext):
                    print( "/".rjust(spaceCount+1) + file )
                    break

    # Wydrukowanie każdego podkatalogu
    def printDirectory(dirEntry, typeList):
        print( dirEntry[0] + "/" )
        printFiles(dirEntry[2], len(dirEntry[0]), typeList)

    # Konwersja łańcucha znaków wzorca na listę rozszerzeń plików
    extList = []
    for ext in pattern.split(";"):
        extList.append(ext.lstrip("*"))

    # Przejście drzewa katalogów w celu wydrukowania plików
    for directory in os.walk(path):
        printDirectory(directory, extList)

::

    /books/python/
              /Python Proposal.doc
              /Python_Phrasebook_TOC.doc
              /python_schedule.xls
              /template.doc
              /TOC_Notes.doc
    /books/python/CH2/
                     /CH2.doc
    /books/python/CH2/code/
                          /comp_str.py
                          /end_str.py
                          /eval_str.py
                          /format_str.py
                          /join_str.py
    /books/python/CH3/
                     /CH3.doc


Serializacja i trwałość obiektów
================================

.. index:: serializacja

Moduł ``pickle``
----------------

.. index::
    double: pickle ; moduł pickle

Serializacja i trwałość obiektów może zostać zrealizowana przy pomocy wbudowanych narzędzi Pythona.
Moduły ``pickle`` i ``cPickle`` serializują obiekty do i z plików.

.. code-block:: python

    import pickle
    p = pickle.Pickler(file)    # file to otwarty obiekt pliku
    p.dump(obj)                 # Zrzut obiektu

Aby odserializować obiekt, używamy funkcji unpickle.

.. code-block:: python

    p = pickle.Unpickler(file)  # file to otwarty obiekt pliku
    obj = p.load()          # Ładowanie obiektu

Serializacja - wskazówki
^^^^^^^^^^^^^^^^^^^^^^^^

1.  Większość typów wbudowanych można poddać serializacji.
2.  Można dokonać serializacji obiektu klasy. Klasa musi być dostępna w momencie odtwarzania obiektu. Sam kod klasy nie jest serializowany. Python automatycznie importuje moduł zawierający odtwarzaną klasę.
3.  Pewne typy obiektów nie mogą być serializowane np. sockety, pliki.
4.  Dowolny obiekt zapewniający metody write(), read() i readline() może być używany jako plik.
5.  Obiekty rekursywne można poddać serializacji. 
6.  Dane po serializacji można przenosić między różnymi systemami operacyjnymi i architekturami sprzętowymi.
7.  Serializacja obiektów zastosowana w Pythonie nie jest dostępna z poziomu programów napisanych w innych językach programowania.

Moduł ``marshal``
-----------------

.. index::
    double: marshal ; moduł marshal

Moduł ``marshal``
    używany do szybkiej serializacji i deserializacji prostych obiektów. Nie obsługuje obiektów rekursywnych i instancji klas. Dane przechowywane w niezależnym formacie binarnym.

.. code-block:: python

    import marshal
    marshal.dump(obj,file) # Zapis obiektu obj do pliku file

    obj = marshal.load(file)

Moduł ``shelve``
----------------

.. index::
    double: shelve ; moduł shelve

Moduł ``shelve`` umożliwia prosty zapis serializowanych danych do pliku z wykorzystaniem składni słownika.

- Klucze muszą być ciągami znaków.
- Wartościami mogą być dowolne obiekty Pythona dla których działa moduł ``pickle``.

.. code-block:: python

    import shelve
    d = shelve.open("data")
    d['foo'] = 42       # Zapis danych do pliku
    x = d['bar']        # Odczyt danych z pliku

+--------------------+--------------------------------+
| **Operacja**       | **Opis**                       |
+====================+================================+
| ``d[key] = obj``   | Zapisuje obiekt                |
+--------------------+--------------------------------+
| ``obj = d[key]``   | Odczytuje obiekt               |
+--------------------+--------------------------------+
| ``del d[key]``     | Usuwa obiekt                   |
+--------------------+--------------------------------+
| ``d.has_key(key)`` | Sprawdza, czy klucz istnieje   |
+--------------------+--------------------------------+
| ``d.keys()``       | Zwraca listę wszystkich kluczy |
+--------------------+--------------------------------+
| ``d.close()``      | Zamyka plik shelve             |
+--------------------+--------------------------------+

Współpraca z systemem operacyjnym
=================================

.. index:: system operacyjny

Moduł ``os``
------------

.. index::
    double: os ; moduł os

Moduł ``os`` udostępnia przenośny, niezależny od platformy interfejs dla dostępu do usług operacyjnych.
Pozwala to na dodanie do programów obsługi na poziomie systemu operacyjnego.

.. py:function:: os.path.abspath(path)

    zwraca bezwzględną ścieżkę w formie łańcucha znaków.

.. code-block:: pycon

    >>> import os
    >>> print os.path.abspath(".")
    /home/my_user/code/Python
    >>> print os.path.abspath("..")
    /home/my_user/code

.. py:function:: os.exists(path)
.. py:function:: os.isdir(path)
.. py:function:: os.isfile(path)

    funkcje sprawdzają istnienie plików i katalogów.

.. code-block:: pycon

    >>> os.path.exists("/home/InfoTraining")
    True
    >>> os.path.isdir("/home/InfoTrainingSzkolenia")
    True
    >>> os.path.isfile ("/home/InfoTrainingSzkolenia/doc1.txt")
    True

.. py:function:: os.chdir(path)

    umożliwia zmianę bieżącego katalogu roboczego dla programu.

.. code-block:: pycon

    >>> os.chdir("/home/user/books/python/ch1/code")
    >>> os.path.abspath(".")
    /home/user/books/python/ch1/code

``os.environ``
    słownik zmiennych środowiskowych.

.. code-block:: pycon

    >>> os.environ['PATH']
    '/usr/sbin:/sbin:/usr/local/bin:/usr/bin'

Moduł ``subprocess``
--------------------

.. index::
    double: subprocess ; moduł subprocess

.. py:function:: subprocess.Popen(command, stdin=None, stdout=None)

    wykona funkcję systemową ``command`` tak, jakby znajdowała się ona w podpowłoce.

.. code-block:: python

    import subprocess
    p = subprocess.Popen("make",stdout=subprocess.PIPE)
    result = p.communicate()
    print result

Moduł ``sys``
-------------

.. index::
    double: sys ; moduł sys

Moduł ``sys`` udostępnia interfejs dostępu do środowiska interpretera Pythona.

.. code-block:: pycon

    >>> import sys
    >>> sys.argv
    ['/home/my_user/code/print_it.py', 'text']
    >>> sys.argv[1]
    'text'

Atrybut ``argv`` modułu ``sys`` jest listą.
Pierwszy element na liście ``argv`` jest ścieżką do modułu.
Reszta listy składa się z argumentów, które zostały przekazane do modułu na początku wykonania.

Atrybut ``stdin`` modułu ``sys`` jest obiektem pliku, który zostaje utworzony na początku wykonywania kodu.

.. code-block:: pycon

    >>> text = sys.stdin.readline()
    Dane wejściowe
    >>> print text
    Dane wejściowe

Atrybuty ``stdout`` i ``stderr`` wskazują na pliki używane jako standardowe wyjście oraz standardowe wyjście błędów.
Pliki te domyślnie są związane z ekranem.

.. code-block:: pycon

    >>> sOUT = sys.stdout
    >>> sERR = sys.stderr
    >>> sys.stdout = open("output.txt", "w")
    >>> sys.stderr = sys.stdout
    >>> sys.stdout = sOUT
    >>> sys.stderr = sERR

Moduł ``platform``
------------------

.. index::
    double: platform ; moduł platform

Moduł ``platform`` udostępnia przenośny interfejs do informacji o platformie, na której uruchamiany jest program.

.. py:function:: platform.architecture()

    zwraca krotkę (bits, linkage)
     * bits – liczba bitów wielkości słowa w systemie
     * linkage – powiązane informacje o pliku wykonywalnym Pythona

::

    >>> import platform
    >>> platform.architecture()
    ('64bit', 'ELF')

.. py:function:: platform.python_version()

    zwraca wersję pliku wykonywalnego Pythona dla celów zgodności.

::

    >>> platform.python_version()
    '3.3.2'

.. py:function:: platform.uname()

    zwraca obiekt zawierający informację w formie (system, node, release, version, machine, processor)

     * system – aktualnie działający system operacyjny
     * node – nazwa hosta danej maszyny
     * release – główna wersja systemu operacyjnego
     * version – informacja o wydaniu systemu operacyjnego w formie łańcucha znaków
     * machine, processor – informacje sprzętowe danej platformy

.. code-block:: pycon

    >>> platform.uname()
    uname_result(system='Linux', node='tpad', release='3.2.0-4-amd64',
    version='#1 SMP Debian 3.2.46-1+deb7u1', machine='x86_64', processor='')
 
Moduł ``time``
--------------

.. index::
    double: time ; moduł time

Moduł ``time`` udostępnia przenośny interfejs do funkcji związanych z czasem w systemie, na którym program jest wykonywany.

``time.time()``
    Zwraca bieżący czas systemowy jako liczbę sekund, które upłynęły od 1.01.1970 zgodnie z UTC (Coordinated Universal Time)
``time.localtime(secs)``
    Zwraca czas w sekundach od 1.01.1970 w formie krotki (year, month, day, hour, second, day of week, day of year, daylight savings)
``time.ctime(secs)``
    Zwraca czas, określony w sekundach od 1.01.1970, w formie sformatowanego łańcucha znaków, nadającego się do wydruku
``time.clock()``
    Zwraca aktualny czas procesora w postaci liczby zmiennoprzecinkowej, która może być używana w funkcjach mierzących czas
``time.sleep(secs)``
    Zmusza bieżący proces do uśpienia przez liczbę sekund określoną przez liczbę zmiennoprzecinkową secs

Wyrażenia regularne
===================

.. index:: wyrażenia regularne
.. index:: regex

Wyrażenie regularne (``regex``) definiuje prosty analizator, który sprawdza dopasowanie tekstu do danego wzorca.

Powody używania wyrażeń regularnych:
 * Przetwarzanie: identyfikacja i wyodrębniane fragmentów tekstu, które spełniają określone kryteria. Wyrażenia regularne są używane w celu tworzenia doraźnych analizatorów składni oraz przez zwykłe narzędzia analizatorów składni.
 * Wyszukiwanie: odnajdywanie łańcuchów znaków, które mogą mieć więcej niż jedną formę, na przykład znalezienie dowolnego z plików auto.png, auto.jpg lub auto.svg, ale unikanie pliku autobus.png.
 * Wyszukiwanie i zastępowanie: zastępowanie każdego łańcucha znaków dopasowanego przez wyrażenie regularne, na przykład wyszukanie "motor" lub "pojazd jednośladowy" i zastąpienie słowem "motocykl".
 * Dzielenie łańcuchów znaków: podzielenie łańcucha znaków w każdym miejscu dopasowanym przez wyrażenie regularne, na przykład podział w każdym miejscu występowania dwukropka lub znaku równości.
 * Sprawdzanie poprawności: weryfikacja, czy dany fragment tekstu spełnia pewne kryteria, na przykład zawiera cyfry, a po nich symbol waluty.

::

    foo.* # Dopasowuje string rozpoczynający od foo
    \d* # Dopasowuje dowolny ciąg znaków złożony z cyfr
    [a-zA-Z]+ # Dopasowuje sekwencję jednej lub więcej liter

.. index::
    double: re ; moduł re

Moduł re
---------

Moduł ``re`` umożliwia korzystanie z wyrażeń regularnych w Pythonie.

Znaki specjalne
^^^^^^^^^^^^^^^

Większość znaków może być używana jako literały.
Istnieją jednak znaki specjalne, które muszą być poprzedzone ukośnikiem (\), aby można ich było używać jako literałów.
Wspomniane znaki specjalne to ``\ . ^ $ ? + * {} [] () |``.

Klasy znaków
^^^^^^^^^^^^^^^

Jeśli zamiast jednego określonego znaku chcemy dopasować jeden z zestawów znaków, używamy klasy znaków.
Klasa znaków to jeden lub większa liczba znaków ujętych w nawiasy kwadratowe.
Klasa znaków jest wyrażeniem, więc jeśli nie jest wyraźnie podany kwantyfikator, to zostanie dopasowany dokładnie jeden znak (dowolny ze znaków zdefiniowanych w klasie znaków).

Dla często używanych klas znaków dostępne są formy skrótowe.

+--------+------------------------------------------------------+
| ``.``  | Dopasowuje dowolny znak oprócz znaku nowej linii     |
+--------+------------------------------------------------------+
| ``\d`` | Dopasowuje dowolną cyfrę                             |
+--------+------------------------------------------------------+
| ``\D`` | Dopasowuje dowolny znak nie będący cyfrą             |
+--------+------------------------------------------------------+
| ``\s`` | Dopasowuje dowolny biały znak                        |
+--------+------------------------------------------------------+
| ``\S`` | Dopasowuje dowolny znak nie będący białym znakiem    |
+--------+------------------------------------------------------+
| ``\w`` | Dopasowuje dowolny znak alfanumeryczny               |
+--------+------------------------------------------------------+
| ``\W`` | Dopasowuje znaki nie będące znakami alfanumerycznymi |
+--------+------------------------------------------------------+

Kwantyfikatory wyrażeń regularnych
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Kwantyfikatory służą do określania powtórzeń znaków lub sekwencji we wzorcach.

Domyślnie wyrażenia regularne realizują tzw. zachłanne dopasowanie.
Każdy podciąg we wzorcu wyrażenia regularnego jest dopasowywany do największej możliwej liczby znaków w ciągu.
Dopiero potem następuje przejście do kolejnej części wyrażenia. 

+------------+---------------------------------------------------+
| ``*``      | Dopasowuje 0 lub więcej wystąpień                 |
+------------+---------------------------------------------------+
| ``+``      | Dopasowuje 1 lub więcej wystąpień                 |
+------------+---------------------------------------------------+
| ``?``      | Dopasowuje 0 lub 1 wystąpienie                    |
+------------+---------------------------------------------------+
| ``{m,n}``  | Dopasowuje m do n wystąpień                       |
+------------+---------------------------------------------------+
| ``[...]``  | Dopasowuje zbiór znaków                           |
+------------+---------------------------------------------------+
| ``[^...]`` | Dopasowuje znaki, które nie występują w zbiorze   |
+------------+---------------------------------------------------+
| ``A | B``  | Dopasowuje A lub B                                |
+------------+---------------------------------------------------+
| ``(...)``  | Dopasowuje wyrażenie podane w nawiasie jako grupę |
+------------+---------------------------------------------------+

Dodanie znaku zapytania po kwantyfikatorze powoduje przekształcenie go w tzw. kwantyfikator leniwy.
Kwantyfikator leniwy pobiera znak po znaku szukając dopasowania.
Ewentualna próba dopasowanie całego tekstu następuje na samym końcu.

+------------+-----------------------------------------------+
| ``??``     | Dopasowuje 0 lub 1 wystąpienie, wersja leniwa |
+------------+-----------------------------------------------+
| ``*?``     | Dopasowuje 0 lub więcej, wersja leniwa        |
+------------+-----------------------------------------------+
| ``+?``     | Dopasowuje 1 lub więcej, wersja leniwa        |
+------------+-----------------------------------------------+
| ``{m,n}?`` | Dopasowuje m do n wystąpień, wersja leniwa    |
+------------+-----------------------------------------------+

Asercje wyrażeń regularnych
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Asercja pozwala wyznaczyć miejsce w tekście, w którym musi pojawić się dopasowanie.

+--------+-----------------------------------------------------------------------------------------------------------+
| ``^``  | Dopasowuje początek stringa, także po każdym znaku nowego wiersza, jeśli włączono opcję re.MULTILINE      |
+--------+-----------------------------------------------------------------------------------------------------------+
| ``$``  | Dopasowuje koniec stringa, , także przed każdym znakiem nowego wiersza, jeśli włączono opcję re.MULTILINE |
+--------+-----------------------------------------------------------------------------------------------------------+
| ``\A`` | Dopasowuje początek stringa                                                                               |
+--------+-----------------------------------------------------------------------------------------------------------+
| ``\b`` | Dopasowuje pusty string na początku lub na końcu słowa                                                    |
+--------+-----------------------------------------------------------------------------------------------------------+
| ``\B`` | Dopasowuje pusty string, lecz nie na początku lub na końcu słowa                                          |
+--------+-----------------------------------------------------------------------------------------------------------+
| ``\Z`` | Dopasowuje na końcu stringa                                                                               |
+--------+-----------------------------------------------------------------------------------------------------------+

Surowe ciągi znaków
^^^^^^^^^^^^^^^^^^^

Surowe ciągi znaków (raw strings) ułatwiają pisanie wyrażeń regularnych w Pythonie.
Ciąg poprzedza się literą ``r``, która wyłącza specjalne znaczenie backslash'a w kolejnym ciągu znaków.

.. code-block:: python

    expr = r'(\d+)\.(\d*)' # Dopasowuje liczby jak 3.4772


opis modułu ``re``
^^^^^^^^^^^^^^^^^^

 * Wyrażenia regularne są definiowane z użyciem opisanej składni
 * Kompilowany do wyrażenia regularnego "obiekt"
 * Używany do wykonywania operacji dopasowywania i zastępowania

.. code-block:: python

    import re
    pattern = r'(\d+)\.(\d*)'       # Mój wzór
    r = re.compile(pattern)         # Kompilacja
    m = r.match(s)                  # Sprawdzam
    if m:
        print( "pasuje" )
    else:
        print( "nie pasuje" )

Obiekty wyrażeń regularnych
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Obiekty wyrażeń regularnych stworzone przez ``re.compile()`` posiadają następujące metody:

``r.search(s [,pos [,endpos]])``
    Szuka dopasowania
``r.match(s [,pos [,endpos]])``
    Sprawdza dopasowanie stringu
``r.split(s)``
    Dzieli według dopasowania regex
``r.findall(s)``
    Znajduje wszystkie dopasowania
``r.sub(repl,s)``
    Zamienia wszystkie dopasowania na repl

 * Jeśli znaleziono dopasowanie, zwracany jest obiekt dopasowania ’MatchObject’, który zawiera informację, gdzie znaleziono dopasowanie oraz o grupie
 * Metoda search szuka dopasowania w dowolnym miejscu stringa
 * Metoda match szuka dopasowania zaczynając od pierwszego znaku
 * Parametry pos i endpos określają początkową i końcową pozycję do wyszukania/dopasowania

Obiekty dopasowania
^^^^^^^^^^^^^^^^^^^

Obiekty dopasowania zawierają informację o samym dopasowaniu.
Oparte są na pojęciu grup i stosują reguły grupowania.

Wyrażenie regularne ``(\d+)\.(\d*)`` ma 3 grupy:
 * Grupa 0 : całe wyrażenie regularne
 * Grupa 1 : część ``(\d+)``
 * Grupa 2 : część ``(\d*)``

Numerowanie grup we wzorcu przebiega od lewej do prawej.

Uzyskiwanie informacji o dopasowaniu::

    m.group(n)  # Zwraca tekst dopasowany dla grupy n
    m.start(n)  # Zwraca indeks początkowy dla grupy n
    m.end(n)    # Zwraca indeks końcowy dla grupy n

Przykłady dopasowania
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    import re
    r = re.compile(r'(\d+)\.(\d*)')
    m = r.match("42.37")
    a = m.group(0)  # Zwraca ’42.37’
    b = m.group(1)  # Zwraca ’42’
    c = m.group(2)  # Zwraca ’37’
    print( m.start(2) )    # Drukuje 3

.. code-block:: python

    # Zastępowanie URL (np.: http://www.python.org) hiperłączem
    pat = r'(http://[\w-]+(\.[\w-]+)*((/[\w-~]*)?))'
    r = re.compile(pat)
    r.sub('<a href="\\1">\\1</a>',s) # Zastępowanie w stringu