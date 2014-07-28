************************
Python - tips and tricks
************************

Iteracje
========

Nadużywanie funkcji ``range``
-----------------------------

Programiści o nawykach wywodzący się z języków C/C++ mają tendencje do stosowania pętli ``for`` z użyciem indeksowania:

.. code-block:: python

    for i in range(len(alist)):
        print alist[i]

Python posługuje się *iteracją* po elementach, która zapewnia większą odporność na błędy, jak również jest bardziej czytelna. Poprawną konstrukcją jest

.. code-block:: python

    for item in alist:
        print item

Usprawiedliwieniem konstrukcji z ``range`` bywają następujące argumenty:

- Potrzeba użycia wartości indeksu - poprawnym rozwiązaniem jest:

  .. code-block:: python

      for index, value in enumerate(alist):
          print index, value


- Iteracja po dwóch obiektach, pracując na tych samych indeksach:

  .. code-block:: python

      for word, number in zip(words, numbers):
          print word, number


- Iteracja po fragmencie sekwencji - można użyć wycinków (*slices*):

  .. code-block:: python

      for word in words[1:]: # Exclude the first word
          print word

  Mogą pojawić się problemy z wydajnością. Wycinki list tworzą kopie.


Poprawne użycie funkcji ``range`` to głównie sytuacje gdy potrzebujemy liczb całkowitych - a nie indeksów.

.. code-block:: python

    # Print foo(x) for 0<=x<5
    for x in range(5):
        print foo(x)


Właściwe użycie wyrażeń listowych
---------------------------------

Pętle tworzące listy prawie zawsze można zastąpić wyrażeniami listowymi (albo jeszcze lepiej - generatorowymi)

.. code-block:: python

    # Powolne i nieczytelne
    words = ['her', 'name', 'is', 'rio']
    alist = []
    for word in words:
        alist.append(foo(word))

Zamiast tego:

.. code-block:: python

    words = ['her', 'name', 'is', 'rio']
    alist = [foo(word) for word in words]

Kod staje się prostszy w utrzymaniu i bardziej czytelny. Dodatkowo - przeważnie jest też szybszy.

Inne typowe przypadki

- Podwójnie zagnieżdżona pętla ``for``

  .. code-block:: python

      words = ['her', 'name', 'is', 'rio']
      letters = []
      for word in words:
          for letter in word:
              letters.append(letter)


  a można:

  .. code-block:: python

      words = ['her', 'name', 'is', 'rio']
      letters = [letter for word in words
                        for letter in word]


- Wewnątrz pęli for znajduje się warunek - można go też stosować w wyrażeniach listowych:

  .. code-block:: python

      words = ['her', 'name', 'is', 'rio', '1', '2', '3']
      alpha_words = [word for word in words if isalpha(word)]

Niestety - w wyrażeniach listowych nie można wyłapywać wyjątków. Ale można wtedy stosować np. *funkcje generatorowe*.

Wydajność
=========

Sprawdzanie list w czasie O(1)
------------------------------

Sprawdzanie czy element znajduje się w kontenerze (operator ``in``) ma różną wydajność dla różnych typów danych:

.. code-block:: python

    lyrics_list = ['her', 'name', 'is', 'rio']

    # Unikajmy
    words = make_wordlist() # Pretend this returns many words that we want to test
    for word in words:
        if word in lyrics_list: # Linear time
            print word, "is in the lyrics"

    # Zbiory mają szybkie wyszukiwanie
    lyrics_set = set(lyrics_list) # Linear time set construction
    words = make_wordlist() # Pretend this returns many words that we want to test
    for word in words:
        if word in lyrics_set: # Constant time
            print word, "is in the lyrics"


Wbudowane algorytmy - lista
^^^^^^^^^^^^^^^^^^^^^^^^^^^

+---------------+-------------------+---------------------------+
|   Operation   |   Average Case    |   Amortized Worst Case    |
+===============+===================+===========================+
|   Copy        |   O(n)            |   O(n)                    |
+---------------+-------------------+---------------------------+
|   Append[1]   |   O(1)            |   O(1)                    |
+---------------+-------------------+---------------------------+
|   Insert      |   O(n)            |   O(n)                    |
+---------------+-------------------+---------------------------+
|   Get Item    |   O(1)            |   O(1)                    |
+---------------+-------------------+---------------------------+
|   Set Item    |   O(1)            |   O(1)                    |
+---------------+-------------------+---------------------------+
|  Delete Item  |   O(n)            |   O(n)                    |
+---------------+-------------------+---------------------------+
|  Iteration    |   O(n)            |   O(n)                    |
+---------------+-------------------+---------------------------+
|   Get Slice   |   O(k)            |   O(k)                    |
+---------------+-------------------+---------------------------+
|   Del Slice   |   O(n)            |   O(n)                    |
+---------------+-------------------+---------------------------+
|   Set Slice   |   O(k+n)          |   O(k+n)                  |
+---------------+-------------------+---------------------------+
|   Extend[1]   |   O(k)            |   O(k)                    |
+---------------+-------------------+---------------------------+
|   Sort        |   O(n log n)      |   O(n log n)              |
+---------------+-------------------+---------------------------+
|   Multiply    |   O(nk)           |   O(nk)                   |
+---------------+-------------------+---------------------------+
|   x in s      |   O(n)            |                           |
+---------------+-------------------+---------------------------+
|min(s), max(s) |   O(n)            |                           |
+---------------+-------------------+---------------------------+
|   Get Length  |   O(1)            |   O(1)                    |
+---------------+-------------------+---------------------------+

Wbudowane algorytmy - słownik
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+---------------+-------------------+---------------------------+
|   Operation   |   Average Case    |   Amortized Worst Case    |
+===============+===================+===========================+
|   Copy[2]     |   O(n)            |   O(n)                    |
+---------------+-------------------+---------------------------+
|   Get Item    |   O(1)            |   O(n)                    |
+---------------+-------------------+---------------------------+
|   Set Item[1] |   O(1)            |   O(n)                    |
+---------------+-------------------+---------------------------+
|   Delete Item |   O(1)            |   O(n)                    |
+---------------+-------------------+---------------------------+
|  Iteration[2] |   O(n)            |   O(n)                    |
+---------------+-------------------+---------------------------+

Uwagi:

[1] = Pojedyncza operacja może trwać długo, w zależności od poprzednich
wartości słownika

[2] = Dla tych operacji n oznacza największą pojemość jaką kiedykolwiek
osiągnął słownik, a nie bieżącą.

Wbudowane algorytmy - zbiór
^^^^^^^^^^^^^^^^^^^^^^^^^^^

+------------------------+-----------------------+--------------------+
|   Operation            |   Average Cas    e    |Amortized Worst Case|
+========================+=======================+====================+
|   x in s               |   O(1)                |   O(n)             |
+------------------------+-----------------------+--------------------+
|   Union s|t            |  O(len(s)+len(t))     |                    |
+------------------------+-----------------------+--------------------+
| Intersection s&t       | O(min(len(s), len(t)) | O(len(s) * len(t)) |
+------------------------+-----------------------+--------------------+
| Difference s-t         |   O(len(s))           |                    |
+------------------------+-----------------------+--------------------+
| s.difference_update(t) |  O(len(t))            |                    |
+------------------------+-----------------------+--------------------+

Konkatenacja ciągów
===================

Najlepszym rozwiązaniem od Pythona 2.6 jest:

.. code-block:: python

    s = ""
    for substring in list:
        s += substring

można również użyć:

.. code-block:: python

    s = ''.join(list)

Co jeśli generujemy elementy ciągu?:

.. code-block:: python

    s = ""
    for x in range(...):
        s += some_function(x)

przeważnie lepiej użyć wyrażenia listowego:

.. code-block:: python

    slist = [some_function(elt) for elt in somelist]
    s = "".join(slist)


dobrze:

.. code-block:: python

    head = "www.site.pl"
    query = "&q=costam"
    tail = "&u=ktos"
    out = "http://" + head + query + tail + "/"

lepiej:

.. code-block:: python

    out = "http://{}{}{}/".format(head, query, tail)

czytelniej:

.. code-block:: python

    out = "http://{head}{query}{tail}/".format(**locals())

Zakres zmiennych
================

Pętla ``for``
-------------

W języku Python pętla *wypuszcza* zmienne poza swój zakres!.

.. code-block:: python

    for idx, value in enumerate(y):
        if value > max_value:
            break

    processList(y, idx)

Powyższy kod zadziała, jeśli tylko ``y`` nie jest puste.

Aby temu zaradzić wystarczy użyć:

.. code-block:: python

    def find_item(item, alist):
        result = None
        for idx, other_item in enumerate(alist):
            if other_item == item:
                result = idx
                break

        return result

Zmienne globalne
----------------

Należy uważać z przykrywaniem się zmiennych z zakresu globlanego (outer scope).

.. code-block:: python

    # Gdzie jest blad
    def print_file(filenam):
        """Print every line of a file."""
        with open(filename) as input_file:
            for line in input_file:
                print line.strip()

    if __name__ == "__main__":
        filename = sys.argv[1]
        print_file(filename)

Lokalne vs. globalne
^^^^^^^^^^^^^^^^^^^^

Czas dostępu do zmiennych lokalnych jest o wiele krótszy:

.. code-block:: python

    def func():
        upper = str.upper
        newlist = []
        append = newlist.append
        for word in oldlist:
            append(upper(word))
        return newlist

Ostrzeżenie - kod zaczyna być nieczytelny.

Sloty
=====

``__slots__``
    Każdy obiekt pythona posiada ``__dict__`` - słownik atrybutów.
    Jeśli nasza klasa nie będzie korzystała z dynamicznej natury takiego słownika,
    to można użyć metody ``__slots__`` do utworzenia struktury w stylu C.

.. code-block:: python

    class Point(object):
        __slots__=["x","y"]

.. code-block:: pycon

    >>> p = Point()
    >>> p.x = 10
    >>> p.y = 20
    >>> p.z = 30
    Traceback (most recent call last):
      File "<pyshell#54>", line 1, in <module>
        p.z = 30
    AttributeError: 'Point' object has no attribute 'z'


Strategie
=========

.. epigraph::

    We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil

    -- Donald Knuth, 1974

Co jeśli nasz kod jest powolny?

Krok po kroku:

1. Przeanalizować podejście (algorytm)
2. Przeprowadzić analizę
3. Poprawić kod
4. Spróbować
    - ``Pypy`` (wbudowany JIT)
    - przepisać krytyczny kod w C/C++
    - podejście "równoległe"

Referencje
^^^^^^^^^^

- ``http://lignos.org/py_antipatterns/``