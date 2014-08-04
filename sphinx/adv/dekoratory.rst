Dekoratory
##########

Po co nam dekoratory
********************

Dektoratory są często spotykaną w języku Python techniką programistyczną.
Ich zalety to:

1. Redukcja ilości kodu
2. Kontrola funkcji:

 - danych wejściowych
 - wywołania
 - wartości zwracanych

Domknięcie (*closure*)
======================

Domknięcie
  w metodach realizacji języków programowania jest to obiekt
  **wiążący funkcję oraz środowisko**, w jakim ta funkcja ma działać.
  Środowisko przechowuje wszystkie obiekty wykorzystywane przez funkcję,
  niedostępne w globalnym zakresie widoczności. Realizacja domknięcia jest
  zdeterminowana przez język, jak również przez kompilator.

Domknięcia występują głównie w językach funkcyjnych, w których funkcje mogą
zwracać inne funkcje, wykorzystujące zmienne utworzone lokalnie.

*definicja z wikipedii*

W praktyce
  Domknięcia są użyteczne jako generatory funkcji:

- adapter pattern (wspólny interfejs)
- opóźnienie wykonania funkcji

**Przykład**

.. code-block:: python

   def makeInc(x):
     def inc(y):
        # x jest "zamknięte" w definicji
        return y + x
   return inc

   inc5 = makeInc(5)
   inc10 = makeInc(10)

   inc5 (5) # returns 10
   inc10(5) # returns 15

Co to są dekoratory
*******************

Dekorator
  wzorzec projektowy, pozwalający na nadanie nowej funkcjonanalności
  dynamicznie, w trakcie działania programu

W języku Python
  jest to metoda modyfikacji obiektu wywoływalnego (funkcji, metod klasy,
  klas), za pomocą domknięć.

Prosty dekorator
================

.. code-block:: python

   def shouter(func):
       def wrapper():
           print "Before", func.__name__
           result = func()
           print "After", func.__name__
           return result
       return wrapper

**Użycie**

Można tak zdefiniowanej funkcji użyć do "nadpisania" istniejącej już funkcji
(tak naprawdę do zmiany tego, na co wskazuje zmienna)

.. code-block:: python

   def hellome():
       print "Leszek"

   hellome = shouter(hellome)
   hellome()

Prostsze (dostępne od Pythona 2.4) jest użycie specjalnej składni:

.. code-block:: python

   @shouter
   def hellome():
       print "Leszek"

   hellome()

Problem
-------

Co z funkcjami wymagającymi argumentów:

.. code-block:: python

   @shouter
   def add(x, y)
      reutrn x + y

   add(3, 4)
   Traceback (most recent call last):
   TypeError: wrapper() takes no arguments (2 given)

Rozwiązanie
-----------

Musimy użyć parametrów zmiennych:

.. code-block:: python

   def shouter2(func):
       def wrapper(*args, **kwargs):
           print "Before", func.__name__
           result = func(*args, **kwargs)
           print "After", func.__name__
           return result
       wrapper.__name__ = func.__name__
       wrapper.__doc__ = func.__doc__
       return wrapper

**Udoskonalanie pomysłu**

Pakiet ``functools`` zawiera kilka ciekawych funkcji pomocniczych:

.. code-block:: python

   import functools

   def decor(func):
       @functools.wraps(func)
       def wrapper(*args, **kwargs):
           print "Before", func.__name__
           result = func(*args, **kwargs)
           print "After", func.__name__
           return result
       return wrapper

Dekoratory parametryzowane
**************************

Jak to zostało zrobione? Aby otrzymać parametryzowany dekorator, musimy go
"owinąć" w kolejną funkcję (domknięcie)

.. code-block:: python

   def tag(tagname):
       def decor(fun):
           def wrapper(*args, **kwargs):
               out = "<{0}>".format(tagname)
               out += fun(*args, **kwargs)
               out += "</{0}>".format(tagname)
               return out
           return wrapper
       return decor

   @tag("b")
   def output(data):
       return data

Co jest po prostu odpowiednikiem:

.. code-block:: python

   fun = tag(b)(fun)

Wiele dekoratorów
*****************

Funkcję można owijać w wiele dekoratorów, należy pamiętać że kolejność jest istotna.

.. code-block:: python

   @shouter
   @tag(b)
   def my_func():
      pass

co odpowiada:

.. code-block:: python

   my_func = shouter(tag(b)(my_func))

Dekoratory klas
***************

Od Pythona 2.6 można używać dekoratorów klas,
uzyskuje się działanie podobne jak przy dziedziczeniu.

.. code-block:: python

   def addID(original_class):
       orig_init = original_class.__init__
       def __init__(self, *args, **kws):
           print "addID init"
           self.__id = 123
           orig_init(self, *args, **kws)

       original_class.__init__ = __init__
       return original_class

   @addID
   class Foo(object):
       def __init__(self): print "Foo class init"

Klasy jako dekoratory
*********************

Bardzo ciekawym zastosowaniem jest użycie klasy jako dekoratora.
Wystarczy zdefinować w klasie metodę specjalną ``__call__``.
Instancja klasy (uzyskana przecież za pomocą operatora ()) staje się wtedy obiektem, który można wywołać.

.. code-block:: python

   class shout(object):
       def __init__(self, f):
           print "inside decorator's __init__()"
           self.f = f

       def __call__(self):
           print "before call"
           self.f()
           print "after call"

   @shout
   def aFunction():
       print "inside aFunction()"