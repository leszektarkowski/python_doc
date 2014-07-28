**********************************
Elementy programowania funkcyjnego
**********************************

Programowanie funkcyjne to rodzaj podejścia do programowania, w którym obliczenia są przeprowadzane poprzez łączenie funkcji, które nie modyfikują swoich argumentów oraz nie odwołują się do stanu programu ani go nie zmieniają, a wyniki dostarczają jako wartości zwrotne.
Jedną z zalet takiego podejścia jest łatwiejsze tworzenie odseparowanych funkcji i usuwanie błędów z programów funkcyjnych.
W programach funkcyjnych nie występują zmiany stanu, więc ich funkcje można analizować w sposób matematyczny.

Z programowaniem funkcyjnym ściśle związane są trzy koncepcje:

* Mapowanie
* Filtrowanie
* Redukowanie

Funkcja ``map``
=================

Mapowanie polega na pobraniu funkcji oraz obiektu pozwalającego na iterację i wygenerowanie nowego obiektu iterowanego (lub listy), w którym każdy element będzie wynikiem wywołania funkcji względem odpowiadającego mu elementu w początkowym obiekcie pozwalającym na iterację.

.. py:function:: map(function, sequence)

    wywołuje ``function(item)`` dla każdego elementu sekwencji sequence i zwraca iterator po elementach wynikowych.

::

    >>> def cube(x): return x*x*x ...
    >>> list(map(cube, range(1, 11)))
    [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

Funkcji map może być przekazana więcej niż jedna sekwencja. Funkcja przetwarzająca musi wówczas przyjmować dwa argumenty. Jeśli któraś z sekwencji jest krótsza, odpowiedni argument funkcji otrzyma wartość ``None``.::

    >>> seq = range(8)
    >>> def add(x, y): return x+y
    ...
    >>> list(map(add, seq, seq))
    [0, 2, 4, 6, 8, 10, 12, 14]

Funkcja ``filter``
===================

Filtrowanie obejmuje pobranie funkcji oraz obiektu pozwalającego na iterację i wygenerowanie nowego iteratora, w którym każdy element pochodzi z początkowego iteratora pod warunkiem, że funkcja wywołana względem tego elementu zwróciła wartość ``True``.

.. py:function:: filter(function, sequence)

    zwraca sekwencję tych elementów sekwencji przekazanej jako argument, które spełniają predykat ``function``.

::

    >>> def f(x): return x % 2 != 0 and x % 3 != 0
    ...
    >>> list(filter(f, range(2, 25)))
    [5, 7, 11, 13, 17, 19, 23]

Funkcja reduce
==============

Redukcja polega na pobraniu funkcji i obiektu pozwalającego na iterację, a następnie wygenerowaniu pojedynczej wartości zwrotnej.

.. py:function:: reduce(function, sequence)

    pobiera elementy sekwencji i wykonuje funkcję function na jej dwóch pierwszych elementach. Następnie używa wyniku tej operacji oraz kolejnego elementu do obliczenia następnej wartości. Cały proces jest powtarzany aż do przetworzenia listy. Jeśli sekwencja liczy tylko jeden element, zwrócona jest jego wartość. Jeśli sekwencja jest pusta, zgłaszany jest wyjątek.

::

    >>> def add(x,y): return x+y
    ...
    >>> reduce(add, range(1, 11))
    55

``reduce`` może otrzymać opcjonalnie trzeci argument oznaczający wartość początkową.
Jeśli sekwencja liczy tylko jeden element, zwrócona jest wartość otrzymana przez wywołanie funkcji function dla argumentu i elementu sekwencji.
Jeśli sekwencja jest pusta, zwracana jest wartość argumentu.::

    >>> def sum(seq):
    ... def add(x,y): return x+y
    ... return reduce(add, seq, 0)
    ...
    >>> sum(range(1, 11))
    55
    >>> sum([])


Funkcje ``map``, ``filter``, ``reduce`` i operator ``lambda``
==============================================================

Funkcje map, filter i reduce mogą korzystać z funkcji anonimowych definiowanych
operatorem lambda.::

    >>> numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> list(map(lambda x: x * x, numbers))
    [1, 4, 9, 16, 25, 36, 49, 64, 81]
    >>> list(filter(lambda x: x%2 == 0, numbers))
    [2, 4, 6, 8]
    >>> reduce(lambda x,y: x+y, numbers)
    45

Wyrażenia listowe
==================

.. index::
   double: wyrażenia listowe; list comprehension

Wyrażenia listowe (*list comprehensions*) pozwalają w zwięzły sposób odwzorować listę na inną, wykonując na każdym jej elemencie pewne operacje.
Pozwalają otrzymywać przekształcone listy bez odwoływania się do funkcji  ``map`` i ``filter``.::

    >>> freshfruit = [' banana', ' loganberry ', 'passion fruit ']
    >>> [weapon.strip() for weapon in freshfruit]
    ['banana', 'loganberry', 'passion fruit']
    >>> vec = [2, 4, 6]
    >>> [3*x for x in vec]
    [6, 12, 18]
    >>> [3*x for x in vec if x > 3]
    [12, 18]
    >>> [3*x for x in vec if x < 2]
    []

Jeśli wynikiem wyrażenia ma być krotka, wyrażenie musi zostać ujęte w nawiasy ()::

    >>> [[x,x**2] for x in vec]
    [[2, 4], [4, 16], [6, 36]]
    >>> [x, x**2 for x in vec] # error - parens required for tuples
    File "<stdin>", line 1, in ? [x, x**2 for x in vec] ^
    SyntaxError: invalid syntax
    >>> [(x, x**2) for x in vec]
    [(2, 4), (4, 16), (6, 36)]

Wyrażenia listowe mogą działać na wielu listach.::

    >>> vec1 = [2, 4, 6]
    >>> vec2 = [4, 3, -9]
    >>> [x*y for x in vec1 for y in vec2]
    [8, 6, -18, 16, 12, -36, 24, 18, -54]
    >>> [x+y for x in vec1 for y in vec2]
    [6, 5, -7, 8, 7, -5, 10, 9, -3]
    >>> [vec1[i]*vec2[i] for i in range(len(vec1))]
    [8, 12, -54]

Zagnieżdżone wyrażenia listowe
===============================

Wyrażenia listowe mogą być zagnieżdżane.

Przykład: macierz 3x3::

    >>> mat = [
    ... [1, 2, 3],
    ... [4, 5, 6],
    ... [7, 8, 9],
    ... ]

Zamiana wierszy z kolumnami::

    >>> print [[row[i] for row in mat] for i in [0, 1, 2]] [[1, 4, 7], [2, 5, 8],
    [3, 6, 9]]

Odpowiednik przy użyciu iteracji::

    for i in [0, 1, 2]:
       for row in mat:
          print( row[i], end='' )
       print ()

Iteratory
=========

.. index::
   single: iteratory
   single: __iter__

Obiekty iterowalne posiadają metodę ``__iter__`` zwracającą obiekt iteratora

    * Iterator posiada metodę ``__next()__``, która zwraca kolejny element z iterowanej sekwencji
    * Jeśli iteracja dobiegła końca (brak kolejnych elementów) zgłaszany jest wyjątek ``StopIteration``
    * Iterator jest zwracany przez funkcję ``iter()``

::

    >>> s = 'ab'
    >>> it = iter(s)
    >>> it.__next__()
    'a'
    >>> it.__next__()
    'b'
    >>> it.__next__()
    Traceback (most recent call last):
    StopIteration

Przykład::

    class Fibs:
        def __init__(self, limit):
            self.a = 0
            self.b = 1
            self.limit = limit

        def __next__(self):
            self.a, self.b = self.b, self.a + self.b
            if self.a > self.limit:
                raise StopIteration
            return self.a

        def __iter__(self):
            return self

::

    >>> list(Fibs(100))
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

Generatory
==========

.. index::
   single: yield
   single: generatory

Generatory są iteratorami definiowanymi przy pomocy składni normalnej funkcji.
Instrukcja ``yield`` zwraca kolejną wartość z funkcji generatora. ::

    def reverse(data):
        for index in range(len(data)-1, -1, -1):
            yield data[index]

::

    >>> for char in reverse('golf'):
    ...     print( char )
    f
    l
    o
    g

