***************
Testowanie kodu
***************

Testy jednostkowe
=================

Testy jednostkowe
    Służą do sprawdzania zachowania się fragmentu kodu (klasy bądź funkcji).

Testy automatyczne
    Napisane przez programistę, uruchamiane są automatycznie.
    Raportują o statusie wykonania.

Test zwykle składa się z czterech części:

 - Arrange: Set up the object to be tested & collaborators.
 - Act: Exercise functionality on the object.
 - Assert: Make claims about the object & its collaborators
 - Cleanup: Release resources, restore to original state

Istnieje kilka stylów pracy z wykorzystaniem testów jednostkowych:

* Test First
* Test Last
* Test Driven



``doctest``
-----------

Jest to najprostsze rozwiązanie, moduł znajduje się w bibliotece standardowej.
Wystarczy zamieścić w *docstring* fragmenty z sesji interaktywnej

.. code-block:: python

    def tested_fun(n=3):
        """creates n x n semi-matrix
        
        >>> tested_fun(3)
        [[], [1], [1, 1]]
        """
        
        a = []
        for i in range(n):
            a.append([1]*i)
        return a   

Wystarczy teraz wywołać:

.. code-block:: bash

    python3 -m doctest test1.py

Ewentualnie można wywołać test z poziomu modułu:

.. code-block:: python

    if __name__ == "__main__":
        import doctest
        doctest.testmod()

Zalety:

 - bardzo proste tworzenie testów
 - łatwe wyłapywanie "regresji" w kodzie

Wady:

 - problematyczna obsługa typów innych niż stałe ciągi znaków

``unittest``
------------

Biblioteka bazująca na JUnit/xUnit. Standard - nie tylko w języku Python.

Biblioteka :mod:`unittest` została zainspirowana przez JUnit, dzięki czemu ma podobne zachowanie do bibliotek używanych przez inne języki prgramowania.
Wspiera automatyzację testów, tworzenie kodu wspólnego dla testów i grupowanie testów w kolekcjach.

:mod:`unittest` wspiera najważniejsze koncepcje tworzenia testów:

test fixture
   reprezentuje część kodu odpowiedzialną za przygotowanie jednego lub większej liczby testów.
   Umożliwia też definiowanie akcji odpowiedzialnej za "sprzątanie".

test case
   Pojedyncza jednostka testu. Sprawdza odpowiedź na zadane parametry.
   :mod:`unittest` dostarcza klasy bazowej - :class:`TestCase`, której można użyć do tworzenia zestawu testów (*test suite*).

test suite
   Jest zbiorem testów, służy do zebrania razem powiązanych ze sobą testów.

test runner
   Element systemu odpowiedzialny za wykonywanie testów i zwracanie wyników użytkownikowi.

* Tworzymy klasę testującą:

.. code-block:: python

    import unittest 
    
    def euler(n=10):
        return sum(x for x in xrange(1,n) 
                     if x % 5 == 0 or x % 3 == 0)
     
    class MatrixCase(unittest.TestCase): 
        def setUp(self):
            self.factor = 2
        
        def testNumber(self):
            self.assertTrue(euler(10) == 23)
    
    if __name__ == "__main__":
        unittest.main()

* Możemy testować wyjątki

.. code-block:: python

    import unittest 
    
    def euler(n=10):
        return sum(x for x in xrange(1,n) 
                     if x % 5 == 0 or x % 3 == 0)
     
    class MatrixCase(unittest.TestCase): 
        def setUp(self):
            self.factor = 2
            
        def testInvalidType(self): 
            self.assertRaises(TypeError, euler, 'ala') 
    
    if __name__ == "__main__":
        unittest.main()



Klasa ``TestCase`` wspiera szereg metod służących do testowania, takich jak:

+-----------------------------------------+-----------------------------+---------------+
| Method                                  | Checks that                 | New in        |
+=========================================+=============================+===============+
| :meth:`assertEqual(a, b)                | ``a == b``                  |               |
| <TestCase.assertEqual>`                 |                             |               |
+-----------------------------------------+-----------------------------+---------------+
| :meth:`assertNotEqual(a, b)             | ``a != b``                  |               |
| <TestCase.assertNotEqual>`              |                             |               |
+-----------------------------------------+-----------------------------+---------------+
| :meth:`assertTrue(x)                    | ``bool(x) is True``         |               |
| <TestCase.assertTrue>`                  |                             |               |
+-----------------------------------------+-----------------------------+---------------+
| :meth:`assertFalse(x)                   | ``bool(x) is False``        |               |
| <TestCase.assertFalse>`                 |                             |               |
+-----------------------------------------+-----------------------------+---------------+
| :meth:`assertIs(a, b)                   | ``a is b``                  | 3.1           |
| <TestCase.assertIs>`                    |                             |               |
+-----------------------------------------+-----------------------------+---------------+
| :meth:`assertIsNot(a, b)                | ``a is not b``              | 3.1           |
| <TestCase.assertIsNot>`                 |                             |               |
+-----------------------------------------+-----------------------------+---------------+
| :meth:`assertIsNone(x)                  | ``x is None``               | 3.1           |
| <TestCase.assertIsNone>`                |                             |               |
+-----------------------------------------+-----------------------------+---------------+
| :meth:`assertIsNotNone(x)               | ``x is not None``           | 3.1           |
| <TestCase.assertIsNotNone>`             |                             |               |
+-----------------------------------------+-----------------------------+---------------+
| :meth:`assertIn(a, b)                   | ``a in b``                  | 3.1           |
| <TestCase.assertIn>`                    |                             |               |
+-----------------------------------------+-----------------------------+---------------+
| :meth:`assertNotIn(a, b)                | ``a not in b``              | 3.1           |
| <TestCase.assertNotIn>`                 |                             |               |
+-----------------------------------------+-----------------------------+---------------+
| :meth:`assertIsInstance(a, b)           | ``isinstance(a, b)``        | 3.2           |
| <TestCase.assertIsInstance>`            |                             |               |
+-----------------------------------------+-----------------------------+---------------+
| :meth:`assertNotIsInstance(a, b)        | ``not isinstance(a, b)``    | 3.2           |
| <TestCase.assertNotIsInstance>`         |                             |               |
+-----------------------------------------+-----------------------------+---------------+


``pytest``
----------

Pytest
   biblioteka używana przez np. PyPy. Umożliwia przeprowadzenie

* testów jednostkowych
* testów funkcjonalnych
* testów integracyjnych


Najpierw instalacja:

.. code-block:: bash

    pip install -U pytest

Przykład ``pytest``
^^^^^^^^^^^^^^^^^^^

Plik ``test.py``

.. code-block:: python

    def func(x):
        return x+1
        
    def test_answer():
        assert func(3) == 5
        
        
Uruchommy testy:

.. code-block:: bash

    py.test test.py

.. code-block:: c

    =====================================
    _____________________________________
    
        def test_answer():
    >       assert func(3) == 5
    E       assert 4 == 5
    E        +  where 4 = func(3)
    
    test.py:5: AssertionError


Przykład ``pytest``
^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    def test_listcmp():
        l1 = [0,1,2,3,4,5,6,8,9,10]
        l2 = range(10)
        assert l1 == l2
    

Rezultat:

.. code-block:: C
    
    _________________________________________________
    
        def test_listcmp():
            l1 = [0,1,2,3,4,5,6,8,9,10]
            l2 = range(10)
    >       assert l1 == l2
    E       assert [0, 1, 2, 3, 4, 5, ...] == [0, 1,
    E         At index 7 diff: 8 != 7
    
    test.py:10: AssertionError
    =================================================

Parametryzacja testu
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    import pytest
    
    @pytest.mark.parametrize("num", range(10))
    def test_func(num):
        assert num < 9

.. code-block:: C

    _________________________________________________
    
    num = 9
    
        @pytest.mark.parametrize("num", range(10))
        def test_func(num):
    >       assert num < 9
    E       assert 9 < 9
    
    test.py:21: AssertionError
    =================================================

Test double
===========

Podobnie jak kaskader (*stunt double*) podstawiana jest zamiast istniejących klas

klasa używająca *test double* nie wie że nie używa prawdziwej klasy.

Pozwala śledzić zachowanie klasy niezależnie od środowiska.

Można dokonać podziału typowych klas *test double*:

- dummy object - to obiekt używany gdy interfejs wymaga argumentu.
- test stub - zwraca z góry określoną odpowiedź na zapytanie. Nie zawiera żadnej logiki.
- test spy - pozwala na późniejsze zapytania odnośnie tego co się działo.
- mock object - podobny do Stub, ale dodatkowo zawiera pewne weryfikacje.
- fake object - rzeczywista implementacja, ale prostsza od obiektu który podstawia.

http://xunitpatterns.com
https://en.wikipedia.org/wiki/Test_Double

