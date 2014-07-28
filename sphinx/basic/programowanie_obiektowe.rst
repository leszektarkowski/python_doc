********************************
Funkcje, klasy, obiekty i moduły
********************************

Obiekty w Pythonie
==================

Python jest zbudowany wokół koncepcji "obiektu". Każdy fragment danych (listy, słowniki, funkcje, moduły, itp.) przechowywany i wykorzystywany przez Pythona jest obiektem.

Każdy obiekt posiada:
    * Tożsamość *(identity)* – wskazuje na lokalizację obiektu w pamięci
    * Typ *(type)* – opisuje reprezentację obiektu dla Pythona
    * Wartość *(value)* – dane przechowywane w obiekcie

::

    >>> lst = [1, 2, 3]
    >>> id(lst)
    30098576
    >>> type(lst)
    <type 'list'>
    >>> lst
    [1, 2, 3]

Po utworzeniu obiektu jego tożsamość i typ nie mogą być zmienione.
Jeśli wartość obiektu się zmienia, jest to obiekt zmienny *(mutable)*.
Jeśli nie może ulec zmianie – obiekt niezmienny *(immutable)*.
Na przykład, typy ``str`` i ``tuple`` są niezmienne.

::

    >>> t = (1, 2, 3)
    >>> t[0] = 2
    Traceback (most recent call last):
        t[0] = 2
    TypeError: 'tuple' object does not support item assignment

Niektóre obiekty posiadają:
    * Atrybuty – wartości powiązane z obiektem
    * Metody – wywoływalne funkcje, które operują na obiekcie

Dostęp do atrybutów i metod uzyskuje się poprzez wykorzystanie składni z kropkami (.) ::

    >>> f = open(r"c:\\Training\\test.txt", "w")
    >>> print f.closed
    False
    >>> f.close()
    >>> print f.closed
    True

Funkcje
=======

.. index::
   single: funkcje

Definicja i użycie funkcji

.. code-block:: python

    def reminder(a, b):
        """Zwraca reszte z dzielenia a/b"""
        q = a // b
        r = a - q*b
        return r

::

    >>> # Użycie funkcji
    >>> a = reminder(42, 5)  # a = 2
    >>> print a
    2
    >>> print reminder.__doc__
    Zwraca resztę z dzielenia a/b

Funkcje mogą zwracać wiele wartości. Wartości zwracane pakowane są do krotki.

.. code-block:: python

    def divide(a, b):
        q = a/b
        r = a - q*b
        return q, r

    x, y = divide(42,5)  # x = 8, y = 2

Definiowanie parametrów funkcji i sposoby wywoływania:

.. code-block:: python

    def fun(name, location, year=2009):
        print( "{} / {} / {}".format(name, location, year) )

::

    >>> fun("Robert", "Kraków")
    Robert / Kraków / 2009
    >>> fun(location="Berlin", year=2004, name="Anna")
    Anna / Berlin / 2004
    >>> fun("Artur", year=2005, location="Toronto")
    Artur / Toronto / 2005

Parametry mogą być przekazywane również jako:
    * Krotka – przy pomocy składni z *
    * Słownik – przy pomocy składni z **

::

    >>> tuple = ("Edward", "Kolonia", 2003)
    >>> fun(*tuple)
    Edward/Kolonia/2003
    >>> dictionary = { "name": "Zenon", "location": "Gdynia", "year": 1999 }
    >>> fun(**dictionary)
    Zenon/Gdynia/1999

Operator ``lambda``
-------------------

.. index::
   double: operator lambda ; lambda

Operator lambda umożliwia tworzenie funkcji anonimowych.

Składnia: ``lambda <args> : <expression>``

::

    >>> bigger = lambda a, b : a > b
    >>> bigger(1, 2)
    False
    >>> bigger(2, 1)
    True

Klasy
=====

.. index::
   double: klasa ; class

Klasy są zbiorami atrybutów oraz metod.

Klasy umożliwiają:
    * Tworzenie nowych typów danych definiowanych przez użytkownika
    * Rozszerzanie możliwości istniejących typów danych

Definicja klasy
---------------

.. code-block:: python

    class BankAccount:
        def __init__(self, owner, balance=0):
            self.owner = owner
            self.balance = balance

        def withdraw(self, amount):
            self.balance -= amount

        def deposit(self, amount):
            self.balance += amount

        def info(self):
            print( "owner:", self.owner, "; balance:", self.balance )

.. warning::
    W wesji Pythona 2.x definicja klasy powinna zawierać rodzica ``class BankAccount(object):``.
    W przeciwnym razie zostanie wygenerowana klasa tzw. "starego typu".
    Wszyskie klasy w Pythonie 3.x są "nowego typu".

Tworzenie obiektów
------------------

Aby utworzyć obiekt danej klasy należy wywołać klasę przy pomocy operatora ().

Przykład:

.. code-block:: python

    jk = BankAccount("Jan Kowalski", 1000)
    jk.info()
    jk.deposit(2000)
    jk.withdraw(2500)
    jk.info()
    jk.balance = 0  # Dostęp do składowej balance
    jk.info()

::

    owner: Jan Kowalski ; balance: 1000
    owner: Jan Kowalski ; balance: 500
    owner: Jan Kowalski ; balance: 0

Składowe prywatne klasy
-----------------------

.. index::
   single: składowe prywatne

Wszystkie atrybuty i metody zdefiniowane w klasie są publiczne.
Aby ukryć atrybut lub metodę przed dostępem spoza klasy (składowa private) należy jej nazwę poprzedzić dwoma podkreślnikami (np.  ``__atrybut``).

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
    print( jk.balance )               # Błąd!
    print( jk._BankAccount__balance ) # OK
 
Składowe statyczne
------------------

.. index::
   single: składowe statyczne

Składowe statyczne są wspólne dla wszystkich instancji klasy.

.. code-block:: python

    class CountedObject:
        __count = 0   # Statyczna skladowa

        def __init__(self):
            CountedObject.__count += 1


        @staticmethod
        def staticGetCount():
            return CountedObject.__count

        @classmethod
        def classGetCount(cls):
            print "classGetCount invoked for instance of", cls
            return cls.__count

    print "Number of objects: %s" % CountedObject.staticGetCount()
    print "Creating objects..."

    c1 = CountedObject()
    c2 = CountedObject()
    cs = [CountedObject(), CountedObject()]

    print "Number of objects: %s" % CountedObject.staticGetCount()
    print "Number of objects: %s" % CountedObject.classGetCount()

::

    Number of objects: 0
    Creating objects...
    Number of objects: 4
    classGetCount invoked for instance of <class '__main__.CountedObject'>

Właściwości
-----------

.. index::
   double: właściwości ; properties

Właściwości umożliwiają enkapsulację obiektu.
Są odpowiednikiem metod dostępowych.

.. code-block:: python

    class Rectangle:
        def __init__(self):
            self.width = 0
            self.height = 0
        def setSize(self, size):
            self.width, self.height = size
        def getSize(self):
            return self.width, self.height
        size = property(getSize, setSize)

::

    >>> r = Rectangle()
    >>> r.width = 10
    >>> r.height = 20
    >>> r.size
    (10, 20)
    >>> r.size = 150, 100
    >>> r.height
    100

Istnieje możliwość definiowania właściwości typu "read-only".

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

::

    >>> ba = BankAccount("jk", 100)
    >>> ba.balance
    100
    >>> ba.balance = 100 # Błąd!

 
Specjalne atrybuty
------------------

.. index::
   single: specjalne atrybuty

Instancje klas posiadają specjalne atrybuty, które opisują obiekty. ::

    >>> ba = BankAccount("Kowalski", 1000)
    >>> ba.__dict__  # Słownik zdefiniowanych przez użytkownika atrybutów
    {'owner': 'Kowalski', '_BankAccount__balance': 1000}
    >>> ba.__class__.__name__  # Nazwa klasy
    'BankAccount'
    >>> ba.withdraw.__name__  # Nazwa metody
    'withdraw'
    >>> [attrib for attrib in dir(ba) if not attrib.startswith('_')] # Interfejs
    ['counter', 'deposit', 'info', 'owner', 'withdraw']

Metody specjalne
----------------

.. index::
   single: metody specjalne

Klasy umożliwiają przeładowywanie operatorów (podobnie jak w C++).
Jest to możliwe dzięki specjalnym metodom, które można zaimplementować w klasie.

.. code-block:: python

    class Special:
        def __init__(self, *args, **kwargs):
            pass
            # konstruktor

        def __del__(self):
            pass
            # Destruktor – rzadko wykorzystywany

        def __str__(self):
            pass
            # Reprezentacja znakowa; wywoływana przez print i str

        def __repr__(self):
            pass
            # Reprezentacja znakowa; wywoływana przez repr
            # eval(repr(a)) powinno być równe a

        def __getitem__(self, i):
            pass
            # Indeksacja dla obiektu: b = a[i]

        def __setitem__(self, i, v):
            pass
            # Przypisanie z wykorzystaniem indeksacji: a[i] = v

        def __len__(self):
            pass
            # Wywoływane przez len(a);  Funkcja powinna zwrócić
            # długość obiektu (o ile ma to uzasadnienie)

        def __eq__(self, x):
            pass
            # Test self == x; zwraca True lub False

        def __add__(self, b):
            pass
            # Definiuje self + b

        def __sub__(self, b):
            pass
            # Definiuje self – b

        def __mul__(self, b):
            pass
            # Definiuje self * b

        def __div__(self, b):
            pass
            # Definiuje self / b

        def __pow__(self, b):
            pass
            # Definiuje self ** b

 
Dziedziczenie
=============

.. index::
   single: dziedziczenie

Dziedziczenie – umożliwia tworzenie nowych klas, które przejmują formę i funkcjonalność klas bazowych.

Dziedziczenie definiowane jest za pomocą składni:

.. code-block:: python

    class Base:
        pass
    class Derived(Base):
        pass

Przykład:

.. code-block:: python

    class CheckedAccount(BankAccount):
        def __init__(self, owner, balance = 0, limit = 0):
            BankAccount.__init__(self, owner, balance)
            self.limit = limit

        def withdraw(self, amount):
            if (self.balance-amount) < -self.limit:
                print( "Brak srodkow na koncie" )
            else:
                BankAccount.withdraw(self, amount)

Aby wywołać konstruktor klasy bazowej można użyć metody ``super()`` zwracającej objekt *proxy* rodzica.

.. code-block:: python

    def __init__(self, owner, balance = 0, limit = 0):
        super().__init__(owner, balance)
        self.limit = limit


Wielokrotne dziedziczenie
-------------------------

.. index::
   single: dziedziczenie wielokrotne

Dziedziczenie wielokrotne – klasy mogą dziedziczyć po kilku klasach bazowych.

.. code-block:: python

    class Base1(object):
      def __init__(self):
        super().__init__()
        self.a = "Base1.a"
      def fa(self):
        print "a:", self.a
    class Base2(object):
      def __init__(self):
        super().__init__()
        self.b = "Base2.b"
      def fb(self):
        print "b:", self.b

    class Derived(Base2, Base1):
        def __init__(self):
            super().__init__()

::

    >>> d = Derived()
    >>> d.a
    'Base1.a'
    >>> d.b
    'Base2.a'
    >>> d.fa()
    a: Base1.a
    >>> d.fb()
    b: Base2.b

Interfejsy i introspekcja
=========================

Istnieje możliwość sprawdzania charakterystyk klas i obiektów w trakcie działania programu.

::

    >>> issubclass(Derived, Base1)
    True
    >>> issubclass(Base2, Derived)
    False
    >>> Derived.__bases__
    (<class '__main__.Base2'>, <class '__main__.Base1'>)
    >>> d = Derived()
    >>> isinstance(d, Base1)
    True
    >>> hasattr(d, "fa")
    True
    >>> callable(getattr(d, "fa", None))
    True


Moduły
======

.. index::
   single: moduły

Moduł
    plik źródłowy z rozszerzeniem ``.py`` zawierający kod Pythona. Może zawierać definicje funkcji, klas, a także niezależny od nich kod. Moduł może zawierać dokumentację informującą o sposobie jego działania i zastosowaniach.

Wewnątrz modułu jego nazwa (nazwa pliku bez rozszerzenia .py) jest dostępna pod globalną zmienną ``__name__``
 
Plik: fibo.py

.. code-block:: python

    def fib(n):
        """wypisuje wartości ciągu Fibonacciego od 0 do n"""
        a, b = 0, 1
        while b < n:
            print( b, end='')
            a, b = b, a+b

    def fib2(n):
        """zwraca wartość ciągu Fibonacciego dla n"""
        result = []
        a, b = 0, 1
        while b < n:
            result.append(b)
            a, b = b, a+b
            return result

Import modułów
--------------

Przed użyciem modułu należy go zaimportować.

Pierwszy sposób importu::

    >>> import fibo
    >>> fibo.fib(1000)
    1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 98
    >>> fibo.__name__
    'fibo'

Drugi sposób  importu::

    >>> from fibo import fib, fib2
    >>> fib(500)
    1 1 2 3 5 8 13 21 34 55 89 144 233 377

Trzeci sposób importu – ryzyko wystąpienia konfliktu nazw::

    >>> from fibo import *
    >>> fib2(500)
    [1 1 2 3 5 8 13 21 34 55 89 144 233 377]


Ze względu na potencjalny konflikt nazw wywoływany przez składnię ``import *`` zaleca się stosowanie dwóch pierwszych sposobów importu.

Lokalizacja modułów – PYTHONPATH
--------------------------------

.. index::
   single: PYTHONPATH

Kiedy moduł o nazwie ``name`` jest importowany, interpreter przeszukuje:
    * bieżący katalog
    * listę katalogów znajdującą się w zmiennej systemowej ``PYTHONPATH``
    * domyślną ścieżkę instalacji (np. */usr/local/lib/python*)

``sys.path``
    lista katalogów przeglądanych przez interpreter w trakcie wykonywania instrukcji import.

::

    >>> import sys
    >>> sys.path
    ['',
    '/opt/python3.3/lib/python3.3',
     ...]
    >>> sys.path.append("/home/myuser/mypath/python")

Uruchamianie modułów jako skrypt
--------------------------------

Gdy uruchamiany jest moduł Pythona poleceniem::

    python fibo.py 100

Kod w module jest wykonywany, tak jak przy imporcie, ale zmienna globalna modułu ``__name__`` jest ustawiana na ``"__main__"``.

Aby moduł działał jak skrypt należy umieścić na końcu modułu kod sprawdzający, czy ``__name__ == "__main__"``:

.. code-block:: python

    if __name__ == "__main__":
        import sys
        fib(int(sys.argv[1]))

::

    python fibo.py 50
    1 1 2 3 5 8 13 21 34

