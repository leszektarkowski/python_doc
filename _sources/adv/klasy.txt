Klasy i obiekty
###############

Klasy - przypomnienie
*********************

 * Definiowanie
 * Właściwości
 * Sloty
 * Metody statyczne
 * Metody klasy

Definiowanie klasy
==================

Klasę definiujemy za pomocą słowa kluczowego ``class``:

.. code-block:: python

    class MyClass(parents):
        def method(self, ...):
            pass

Tworzony jest *obiekt klasy*:

.. code-block:: pycon

    >>> MyClass
    <class '__main__.MyClass'>
    >>> type(MyClass)
    <type 'type'>

Konsekwencje bycia obiektem
---------------------------

Obiekt klasy może być modyfikowany już po jego utworzeniu:

.. code-block:: pycon

    >>> MyClass.bar = "foo"
    >>> instance = MyClass()
    >>> instance.bar
    'foo'
    >>> MyClass.foo = "bar"
    >>> instance.foo
    'bar'
    >>>

Jak widać ma to wpływ na wszystkie instancje!

Method Resolution Order (MRO)
=============================

Atrybuty są wewnętrznie przechowywane jako słowniki.

.. code-block:: pycon

    >>> class MyClass(object):
    ...     foo = 'bar'
    ...     def func(self):  pass

    >>> MyClass.__dict__
    <dictproxy object at 0x02A085F0>
    >>> print(MyClass.__dict__)

Python przeszukuje przestrzenie nazw w poszukiwaniu żądanego
atrybutu zgodnie z ustaloną kolejnością, zwaną MRO.

.. code-block:: pycon

    >>> MyClass.__mro__
    (<class '__main__.MyClass'>, <type 'object'>)

Składowe prywatne
*****************

Wszystkie atrybuty i metody zdefiniowane w klasie są publiczne

Aby ukryć atrybut lub metodę przed dostępem spoza klasy
(składowa *private*) należy jej nazwę poprzedzid dwoma podkreślnikami
(np.  ``__atrybut``)

.. code-block:: python

    class BankAccount:

        def __init__(self, owner, balance=0):
            self.owner = owner
            self.__balance = balance

        def withdraw(self, amount):
            self.__balance -= amount

        def deposit(self, amount):
            self.__balance += amount

        def info(self):
            print "owner:", self.owner, "; balance:", self.__balance

    jk = BankAccount("Kowalski", 1000)
    print(jk.balance) # błąd!
    print(jk._BankAccount__balance) # ok

Składowe statyczne
******************

Składowe statyczne są wspólne dla wszystkich instancji klasy

.. code-block:: python

    class CountedObject(object):
        __count = 0   # statyczna skladowa
        def __init__(self):
            CountedObject.__count += 1

        @staticmethod
        def staticGetCount():
            return CountedObject.__count

        @classmethod
        def classGetCount(cls):
            print "classGetCount invoked for instance of", cls
            return cls.__count

.. code-block:: python

    print("Number of objects: %s" % CountedObject.staticGetCount())
    print("Creating objects...")
    c1 = CountedObject()
    c2 = CountedObject()
    cs = [CountedObject(), CountedObject()]
    print("Number of objects: %s" % CountedObject.staticGetCount())
    print("Number of objects: %s" % CountedObject.classGetCount())

.. code-block:: pycon

    Number of objects: 0
    Creating objects...
    Number of objects: 4
    classGetCount invoked for instance of <class '__main__.CountedObject'>

Oprócz składowych statycznych mamy dwa specjalne rodzaje metod:

* metody statyczne
* metody klasy

staticmethod vs. classmethod
============================

.. code-block:: python

    print(CountedObject.staticGetCount)
    printCountedObject.classGetCount)

.. code-block:: pycon

    <function staticGetCount at 0x022B20B0>
    <bound method type.classGetCount of <class '__main__.CountedObject'>>

Metoda statyczna
   to po prostu funkcja w przestrzeni nazw klasy.

Metoda klasy
   ma dostęp do klasy, z której została wywołana, lub do **klasy instacji**,
   z której została wywołana. Przydatne przy dziedziczeniu.

Właściwości - *Properties*
**************************

Umożliwiają enkapsulację obiektu za pomocą metod dostępowych.

.. code-block:: python

    class Rectangle(object):
        def __init__(self):
            self.width = 0
            self.height = 0

        def setSize(self, size):
            self.width, self.height = size

        def getSize(self):
            return self.width, self.height

        size = property(getSize, setSize)

.. code-block:: pycon

    >>> r = Rectangle()
    >>> r.width = 10
    >>> r.height = 20
    >>> r.size
    (10, 20)
    >>> r.size = 150, 100

Atrybuty tylko do odczytu
=========================

Dzięki właściwościom istnieje możliwość definiowania atrybutów typu "read-only".

.. code-block:: python

    class BankAccount:

        counter = 0

        def __init__(self, owner, balance=0):
            self.owner = owner
            self.__balance = balance
            BankAccount.counter += 1

        def __getBalance(self):
            return self.__balance

        balance = property(__getBalance)

.. code-block:: pycon

    >>> ba = BankAccount("jk", 100)
    >>> ba.balance
    100
    >>> ba.balance = 100 # błąd!

Atrybuty specjalne
******************

Instancje klas posiadają specjalne atrybuty, które opisują obiekty

.. code-block:: pycon

    >>> ba = BankAccount("Kowalski", 1000)
    >>> ba.__dict__  #user defined attributes
    {'owner': 'Kowalski', '_BankAccount__balance': 1000}
    >>> ba.__class__.__name__  # nazwa klasy
    'BankAccount'
    >>> ba.withdraw.__name__  # nazwa metody
    'withdraw'
    >>> [attrib for attrib in dir(ba) if not attrib.startswith('_')]
    ['counter', 'deposit', 'info', 'owner', 'withdraw']

Metody specjalne
****************

.. py:function:: __new__(cls[, ...])

    Stworzenie nowej instancji klasy

.. py:function:: __init__(self[, ...])

    Konstruktor

.. py:function:: __del__(self)

    Destruktor

.. py:function:: __repr__(self)

    Wywoływana przez funkcję *repr()* i konwersję do ciągów znaków

.. py:function:: __str__(self)

    Wywoływana przez funkcję *str()* i *print*

.. py:function:: __lt__(self, other), __le__, __eq__, __ne__, __gt__, __ge__

    operatory porównania

.. py:function:: __hash__(self)

    Wywoływana przez funkcję *hash()*, używana w kolekcjach

.. py:function:: __bool__(self)

    Wywoływana w trakcie sprawdzania wartości ``bool`` - Python 3.x

.. py:function:: __nonzero__(self)

    Wywoływana w trakcie sprawdzania wartości ``bool`` - Python 2.x


Metody specjalne - Dostęp do atrybutów
======================================

.. py:function:: __getattr__(self, name)

    Wywoływana, gdy wyszukiwanie atrubutów nic nie znalazło

.. py:function:: __setattr__(self, name, value)

    Wywoływana podczas przypisywania atrybutów

.. py:function:: __delattr__(self, name)

    Wywoływana przy usuwaniu atrubutu - *del class_instance.attr*

.. py:function:: __getattribute__(self, name)

    Wywoływana bezwarunkowo przy dostępie do atrybutów klasy

.. code-block:: python

    class MyClass(object):
        def __init__(self):
            self.test=20
        def __getattribute__(self,name):
            print(name)
            return object.__getattribute__(self, name)

    a = MyClass()
    a.test
    a.nothing

Deskryptory
***********

Deskryptory są stosowane tylko gdy klasa zawierająca te metody
pojawia się jako atrybut w klasie "własiciciela"

.. py:function:: __get__(self, instance, owner)

    Wywoływana do pobrania atrybutu z klasy "właściciela"

.. py:function:: __set__(self, instance, value)

    Wywoływana do ustawienia atrybutu z klasy "właściciela"

.. py:function::  __delete__(self, instance)

    Wywoływana w czasie usuwania atrybutu w klasie "właściciela"

.. code-block:: python

    class Die(object):
        def __init__(self, sides=6):
            self.sides = sides

        def __get__(self, instance, owner):
            return int(random.random() * self.sides) + 1

    class Game(object):
        d6 = Die()
        d10 = Die(sides=10)
        d20 = Die(sides=20)

.. code-block:: pycon

    >>> Game.d6
    5
    >>> Game.d10
    8
    >>> Game.d20
    19
    >>> game = Game()
    >>> game.d20
    12

Sloty
*****

.. py:function:: __slots__

    Każdy obiekt pythona posiada __dict__ - słownik atrybutów.
    Powoduje to spory narzut na pamięć. Jeśli nasza klasa nie będzie
    korzystała z dynamicznej natury takiego słownika, to można użyć metody
    ``__slots__`` do utworzenia struktury w stylu C.

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

Wywoływanie instancji - ``__call__``
************************************

.. py:function:: __call__(self, args)

    Wywoływana przez operator nawiasów (). Pozwala na użycie instancji klasy tak jak funkcji.

.. code-block:: python

    class Factorial:
        def __init__( self ):
            self.cache= {1:1}
        def __call__( self, n ):
            if n not in self.cache:
                self.cache[n] = n*self(n-1)
            return self.cache[n]

    fact = Factorial()
    print(fact(2))

Dziedziczenie
*************
Dziedziczenie definiowane jest za pomocą składni:

.. code-block:: python

    class Base:
        pass
    class Derived(Base):
        pass

Przykład

.. code-block:: python

    class CheckedAccount(BankAccount):
        def __init__(self, owner, balance = 0, limit = 0):
            # base constructor call
            BankAccount.__init__(self, owner, balance)
            self.limit = limit
        def withdraw(self, amount):
            if (self.balance-amount) < -self.limit:
            print("Brak środków na koncie")
        else:
            # Base class method!
            BankAccount.withdraw(self, amount)

Wielokrotne dziedziczenie
=========================

Klasy mogą dziedziczyć po kilku klasach bazowych

.. code-block:: python

    class Base1:
        def __init__(self):
            super().__init__()
            self.a = "Base1.a"

    class Base2:
        def __init__(self):
            super().__init__()
            self.b = "Base2.b"

    class Derived(Base2, Base1):
        def __init__(self):
            super().__init__()

.. code-block:: pycon

    >>> d = Derived()
    >>> d.a
    'Base1.a'
    >>> d.b
    'Base2.a'


``super``
=========

.. py:function::  super()

    Funkcja ``super()`` zwraca obiekt proxy służący do wywoływania metod rodzica.
    Obiekt jest wybierany zgodnie z MRO.

.. code-block:: python

    class Derived(Base2, Base1):
        def __init__(self):
            super().__init__()

W Pythonie 2 trzeba pamiętać, że działa tylko dla klas nowego typu.


Problemy z super
----------------

.. code-block:: pycon

    >>> class A(object):
    ...     def __init__(self):
    ...         print("A")
    ...         super().__init__()
    ...
    >>> class B(object):
    ...     def __init__(self):
    ...         print("B")
    ...         super().__init__()
    ...
    >>> class C(A,B):
    ...     def __init__(self):
    ...         print("C")
    ...         A.__init__(self)
    ...         B.__init__(self)
    ...
    >>> print "MRO:", [x.__name__ for x in C.__mro__]
    MRO: ['C', 'A', 'B', 'object']
    >>> C()
    C A B B

Dziedziczenie po typach wbudowanych
===================================

Od Pythona 2.2 można dziedziczyć po wszystkich typach wbudowanych.

.. code-block:: python

    class CountDict(dict):

        def __getitem__(self, key):
            if key in self:
                return super(CountDict, self).__getitem__(key)
            else:
                return 0

    import random

    stats = CountDict()

    for i in range(1000000):
        stats[int(random.random() * 10)] += 1

    print(stats)

.. code-block:: python

    {0: 100336, 1: 100135, 2: 100122, 3: 99501, 4: 99745,
     5: 100019, 6: 100391, 7: 99924, 8: 100140, 9: 99687}

Dziedziczenie po typach niezmiennych
====================================

Dla typów niezmiennych *(immutable)* nie działa przeciążanie konstruktora.
Po utworzeniu obiektu jest już za późno na jakąkolwiek modyfikację.

.. code-block:: python

    class AlmostMetaString(str):
        def __init__(self, value, info):
            str.__init__(self, value)
            self.meta = info

.. code-block:: pycon

    >>> C("a", "B")
    Traceback (most recent call last):...

Można zmienić obiekt klasy, za pomocą operatora *__new__*

.. code-block:: python

    class MetaString(str):
        def __new__(cls, value, info):
            obj = str.__new__(cls, value)
            obj.meta = info
            return obj

    metastring = MetaString("Hello World","D. Richie")
    print(metastring, metastring.meta)
