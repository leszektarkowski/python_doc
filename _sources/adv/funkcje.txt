Funkcje w języku Python
#######################

Przypomnijmy sobie podstawowe pojęcia dotyczące obiektów w Pythonie

Obiekty w Pythonie
******************

Python jest językiem w pełni obiektowym: **wszystko jest obiektem**

.. code-block:: pycon

   >>> (5).__add__(3)
   0: 8

Dynamiczne typowanie
====================

Python jest językiem z **dynamicznym typowaniem**
 - zmienne przechowują referencję do obiektu
 - to obiekty posiadają typ

Zmienne w języku Python są pewnego rodzaju **referencjami**, nazywanymi czasem *shared references*

.. code-block:: pycon

   >>> var = 'text'
   >>> var
   'text'
   >>> var = 1
   >>> var
   1

Tożsamość, typ i wartość
========================

**Każdy obiekt posiada**

tożsamość (identity)
  wskazuje na lokalizację obiektu w pamięci
typ (type)
  opisuje reprezentację obiektu dla Pythona
wartość (value)
  dane przechowywane w obiekcie


.. code-block:: pycon

   >>> lst = [1,2,3]
   >>> print(id(lst))
   41729040
   >>> print(type(lst))
   <type 'list'>
   >>> print(lst)
   [1, 2, 3]

Funkcje w Pythonie
******************

.. code-block:: python

    def func_name(input_1, input_2):
        #fancy input
        #processing
        return output

Funkcja:
  Jest to obiekt pierwszoklasowy *("first-class")*, który może być dynamicznie
  tworzony, przekazywany do funkcji, oraz zwracany.

Funkcje jako obiekty
====================

.. code-block:: python

   >>> def foo():
   ...     print("foo is happening")
   >>> foo()
   foo is happening
   >>> type(foo)
   2: <type 'function'>
   >>> bar = foo
   >>> id(foo)
   3: 43146864
   >>> id(bar)
   4: 43146864
   >>> print(foo)
   <function foo at 0x02925E70>
   >>> print(bar)
   <function foo at 0x02925E70>

Wywoływanie funkcji
===================

callable
  Funkcje można *wywołać*

.. code-block:: pycon

   >>> callable(foo)
   True

W Pythonie 3.0 i 3.1 zlikwidowano funckję *callable*, przywrócono ją w późniejszych wersjach.

.. code-block:: pycon

   >>> hasattr(foo, '__call__')
   True
   >>> import collections
   >>> isinstance(foo, collections.Callable)
   True

Na marginesie
-------------
Klasy też można wywoływać:

.. code-block:: pycon

   >>> class Call:
   ...     def __call__(self):
   ...         print("Call me, call me any, anytime")
   >>> c = Call()
   >>> c()
   Call me, call me any, anytime

Atrybuty funkcji
================

Wszystkie funkcje są instancjami *function*, więc:

.. code-block:: pycon

   >>> dir(foo)
   ...
   >>> foo.__name__
   'foo'
   >>> boo = foo
   >>> boo.__name__
   'foo'

Ale funkcje mogą też zawierać własne atrybuty. Szczegóły w http://www.python.org/dev/peps/pep-0232/

.. code-block:: python

    def a():
        return "Message to be printed"

    a.publish = True

    if a.publish:
        print( a() )

Umożliwia to tworzenie zmiennych "statycznych" dla funkcji.
Jeśli weźniemy przykładowy kod w języku C:

.. code-block:: c

    int fn(int i)
    {
        static f = 1;
        f += i;
        return f;
    }

To jego odpowiednikiem w Pythonie może być:

.. code-block:: python

    def fn(i):
        fn.f += i
        return fn.f
    fn.f = 1

Zagnieżdżanie funkcji
=====================

.. code-block:: python

   def fun_gen():
      def addon(a, b)
         return a+b
      return addon

.. code-block:: pycon

   >>> fun1 = fun_gen()
   >>> type(fun1)
   <type 'function'>
   >>> fun1.__name__
   ...


Parametry kontra argumenty
**************************

.. code-block:: python

   def add(a, b):
      return a+b

   x = 3
   y = 2
   print add(x, y)

a, b
   parametry funkcji

x, y
   argumenty funkcji

Parametry funkcji
=================

W Pythonie rozróżniamy cztery różne typy parametrów:

normalne (*normal parameters*)
   mają nazwę i pozycję

nazwane (*keyword parameters*)
   mają nazwę

zmiennie (*variable parameters*)
   poprzedzone gwiazdką \*, mają pozycję

zmienne nazwane (*variable keyword parameters*)
   poprzedzone \**, mają nazwę

Parametry normalne
==================

.. code-block:: python

   def funny(person, year=2000, place="Paris"):
      print(person, year, place)

   funny("Ola", 1995, "Wrocław")
   funny("Ala")
   funny("Olek", place="New York")
   funny("Alek", year=2010)

Pułapki domyślnego atrybutu
===========================

.. code-block:: pycon

   >>> def itsatrap(item, seq=[]):
   ...     seq.append(item)
   ...     return seq
   >>> itsatrap.__defaults__
   ([],)
   >>> itsatrap(1)
   [1]
   >>> itsatrap(1)
   [1, 1]
   >>> itsatrap.__defaults__
   ([1, 1],)

Parametry zmienne
=================

Operator ``*`` służy do stworzenia funkcji akceptujących dowolną liczbę argumentów:

.. code-block:: pycon

   >>> def multiargs(first, *args):
   ...   print(first, args)
   >>> multiargs(1, range(2,4))
   1 ([2, 3],)

Parametry zmienne nazwane
=========================

Operator
** służy do stworzenia funkcji akceptujących dowolną liczbę argumentów nazwanych:

.. code-block:: pycon

   >>> def multikwargs(**kwargs):
   ...     print(kwargs)
   >>> multikwargs(ala="1999", ola="2000")
   {'ola': '2000', 'ala': '1999'}


Parametry zmienne razem
-----------------------

.. code-block:: pycon

   >>> def multi2(first, *args, **kwargs):
   ...     print(first)
   ...     print(args)
   ...     print(kwargs)
   >>> multi2(1, 2, 3, 4, 5, ala="1999", ola="2000")
   1
   (2, 3, 4, 5)
   {'ola': '2000', 'ala': '1999'}

Ograniczeniem w Pythonie serii 2.x była konieczność występowania zmiennych parametrów **na końcu** deklaracji.

Keyword-only arguments
----------------------

Python 3.x zniósł to ograniczenie (PEP-3102) wprowadzając argumenty wywołania które musimy podać za pomocą słów kluczowych.

Python 2.x

.. code-block:: python

    def foo(a, special=None, *args): print [a, special, args]

    foo(1, 2, 3, 4)
    ## [1, 2, (3, 4, )]  # special == 2
    foo(1, 2, 3, 4, special=True)
    ## TypeError

Python 3.x *(keyword-only arguments)*

.. code-block:: python

    def foo(a, *args, special=None): print([a, special, args])

    foo(1, 2, 3, 4)
    ## [1, None, (2, 3, 4)]  # special is None
    foo(1, 2, 3, 4, special=True)
    ## [1, True, (2, 3, 4)]


Zmienne lokalne i globalne
**************************

Zmienne globalne wewnątrz funkcji dostępne są tylko do odczytu.
Jeśli chcemy je modyfikować, musimy zadeklarować je z użyciem słowa kluczowego ``global``.

.. code-block:: python

   x = 2
   y = 3
   def wrap():
        def inner():
            global x
            x = -5
            y = -3
            print("inner", x, y)
        inner()
        print("wrap", x, y)

Ale co jeśli chcelibyśmy modyfikować zmienną wewnątrz funkcji ``wrap``?
Możemy to zrobić używając słowa kluczowego ``nonlocal`` (PEP-3104, Python 3.x):

.. code-block:: python

    def wrap():
        count = 0
        def counter():
            nonlocal count
            count += 1
            return count
        return counter

Locals i globals
================

Python umożliwia również dostęp do zmiennych lokalnych i globalnych przy pomocy specjalnych słowników:

.. code-block:: pycon

   >>> def foo(a):
   ...     print(a)
   >>> foo(5)
   5
   >>> globals()["foo"].__call__(5)
   5

Przykład użycia zmiennych lokalnych:

.. code-block:: python

   def fun():
       a = 5
       b = 10
       print(locals())
       print("{a} {b}".format(**locals()))

.. code-block:: pycon

    >>> fun()
    {'b': 10, 'a': 5}
    5 10