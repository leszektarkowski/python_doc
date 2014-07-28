**********
Metaklasy
**********

Wprowadzenie
============

Metaklasa
    jest to po prostu obiekt (najczęściej klasa) generująca klasy.

---------------

.. epigraph::

    Metaclasses are deeper magic than 99% of users should ever worry about. If you wonder whether you need them, you don't

    -- Python Guru Tim Peters*

Klasy jako obiekty
==================

Podobnie jak w przypadku funkcji, klasy są obiektami.
Służą do tworzenia nowych obiektów (instancji).

.. code-block:: pycon

    >>> class Creator(object):
    ...     pass

Nowy obiekt jest tworzony przy pomocy operatora (). Jego typ to nazwa klasy

.. code-block:: pycon

    >>> a = Creator()
    >>> type(a)
    <class '__main__.Creator'>


Jakiego typu jest obiekt klasy?

.. code-block:: pycon

    >>> type(Creator)
    <type 'type'>

Dynamiczne tworzenie klas
=========================

Skoro są obiektami typu ``type``, to możemy je dynamicznie tworzyć:

.. code-block:: pycon

    >>> def choose_class(name):
    ...     if name == 'foo':
    ...         class Foo(object):
    ...             pass
    ...         return Foo
    ...     else:
    ...         class Bar(object):
    ...             pass
    ...         return Bar
    >>> a = choose_class("foo")
    >>> a
    <class '__main__.Foo'>

Skoro klasa jest typu *type* to może można użyć go tak jak klasy?

type
    (nazwa klasy,

    krotka z rodzicami klasy,

    słownik zawierający nazwy atrybutów i ich wartości)

.. code-block:: pycon

    >>> attr = {'foo': "foovalue", 'bar': 123}
    >>> MyClass = type("MyClass", (), attr)
    >>> inst = MyClass()
    >>> inst.bar
    123

Dziedziczenie z użyciem ``type``
--------------------------------

.. code-block:: pycon

    >>> class MyClassChild(MyClass):
    ...     bar = 1234
    >>> a = MyClassChild()
    >>> a.bar, a.foo
    (1234, 'foovalue')

oraz z użyciem *type*:

.. code-block:: pycon

    >>> MCC = type('MCC2', (MyClass,), {'bar': 1234})
    >>> b = MyClassChild2
    >>> b.bar, b.foo
    (1234, 'foovalue')

Metody klasy
------------

Oczywiście metody też mogą stanowić część słownika
przekazywaną do ``type``

.. code-block:: pycon

    >>> def echo(self):
    ...     print(self.foo)

    >>> MCC3 = type('MCC3',
    ...             (MyClass,),
    ...             {'bar': 1234, 'echo': echo})
    >>> c = MCC3()
    >>> c.echo()
    foovalue

Metaklasy
=========

``type`` jest więc wbudowaną w Pythona metaklasą.
Jednakże istnieje możliwość stworzenia własnych metaklas.

W Pythonie 3 słowo ``metaclass`` wskazuje na obiekt, który należy użyc **zamiast** ``type`` do utworzenia obiektu klasy:

.. code-block:: python

    class MyClass(metaclass=class_creator)
        pass
        ...

W Pythonie 2 należy użyć specjalnego atrybutu klasy o nazwie ``__metaclass__``:

.. code-block:: python

    class MyClass(object):
        __metaclass__ = class_creator
        ...

Przykład metaklasy (metafunkcji)
--------------------------------

.. code-block:: python

    def upper_attr(cls, parents, attrs):
        _attrs = ((name.upper(), value)
                   for name, value in attrs.items())
        attrs_upper = dict(_attrs)
        return type(cls, parents, attrs_upper)

    class Foo(object):
        __metaclass__ = upper_attr
        bar = 'foo'

    print(Foo().BAR)

Przykład metaklasy (klasa)
--------------------------

.. code-block:: python

    class UpperAttr(type):
        def __new__(cls, name,
                    parents, attrs):
            _attrs = ((name.upper(), value)
                   for name, value in attrs.items())
            attrs_upper = dict(_attrs)
            return type(name, parents, attrs_upper)

    class Boo(object):
        __metaclass__ = UpperAttr
        foo = 'bar'

    print(Boo().FOO)

Metoda specjalna ``__new__``
----------------------------

.. py:function:: __new__(cls, ...)

    jest metodą wywoływaną, **aby utworzyć** nową instancję
    obiektu. Przekazywany jest do niej *obiekt klasy*,
    oraz argumenty konstruktora

.. py:function:: __init__(self, ...)

    konstruktor, jest wykonywany, **gdy tworzony** jest obiekt (instancja),
    przekazywany jest do niego *obiekt instancji*.

Szablon metaklasy
=================

Ponieważ metaklasy są tak naprawdę zwykłymi klasam, to mogą podlegać
regułom OOP (dziedziczenie). Zatem aby zapewnić bezproblemowe dziedziczenie:

.. code-block:: python

    class UpperAttr2(type):
        def __new__(cls, name,
                    parents, attrs):
            _attrs = ((name.upper(), value)
                   for name, value in attrs.items())
            attrs_upper = dict(_attrs)
            return super(UpperAttr2, cls).__new__(
                  cls, name, parents, attrs_upper)

``__call__`` metaklasy
----------------------

Ciekawym aspektem jest użycie metody ``__call__``.
Jest ona wywoływana dla gotowego obiektu klasy, wtedy gdy używamy "wywołania" (operatora ())

.. code-block:: python

    class Meta(type):
        def __call__(cls, *args, **kwds):
            print('__call__ of ', str(cls))
            print('__call__ *args=', str(args))
            return type.__call__(cls, *args, **kwds)


.. code-block:: pycon

    >>> a = MyClass(1,2)
    __call__ of  <class '__main__.MyClass'>
    __call__ *args= (1, 2)
    MyClass object with a=1, b=2


Zastosowanie metaklas
=====================

Metaklasy są nazywane "rozwiązaniem szukającym problemu".

Praktyczne zastosowanie:

  - tworzenie API (np. Django, Twisted)
  - wzorce projektowe (Singleton)
