***************
Biblioteka lxml
***************

``lxml`` - wygodna biblioteka do obsługi XML w Pythonie opakowująca biblioteki libxml2 i libxslt.
Kompatybilna z ElementTree API.

Do pobrania ze strony http://codespeak.net/lxml/

Podstawy ``ElementTree API``
============================

Element
    podstawowy obiekt kontenerowy umożliwiający przechowywanie danych w hierarchicznych strukturach danych (drzewach).

Właściwości obiektu typu Element:

* ``tag`` – string identyfikujący typ danych przechowywanych w elemencie
* ``attrib`` – słownik atrybutów elementu
* ``text``, ``tail`` – dane tekstowe przechowywane w elemencie
* sekwencja elementów podrzędnych

Import biblioteki

.. code-block:: python

    from lxml import etree

Tworzenie elementów drzewa
--------------------------

Tworzenie elementów drzewa odbywa się za pomocą fabryki Element lub SubElement.

.. code-block:: pycon

    >>> root = etree.Element("root")
    >>> root.append(etree.Element("child1"))
    >>> child2 = etree.SubElement(root, "child2")
    >>> child3 = etree.SubElement(root, "child3")
    >>> print( etree.tostring(root, pretty_print=True) )
    <root>
      <child1/>
      <child2/>
      <child3/>
    </root>

Dostęp do elementów drzewa
--------------------------

Dostęp do elementów podrzędnych w drzewie:

.. code-block:: pycon

    >>> child = root[0]
    >>> print child.tag
    child1

    >>> print len(root)
    3

    >>> children = list(root)

    >>> for child in root:
    ...     print( child.tag )
    child1
    child2
    child3

Dostęp do elementów nadrzędnych – metoda ``getparent()``

Dostęp do elementów z tego samego poziomu:

* ``getprevious()``
* ``getnext()``

.. code-block:: pycon

    # Dostęp do rodzica
    >>> root is root[0].getparent()
    True

    # Dostęp do rodzeństwa
    >>> print( root[1].getprevious().tag )
    child1
    >>> print( root[1].getnext().tag )
    child3

Atrybuty elementów
------------------

Atrybuty elementów można dodawać:

* z wykorzystaniem fabryki ``Element``
* metodami ``set()``
* przy pomocy słownika ``attrib`` elementu

Dane tekstowe
-------------

Elementy mogą przechowywać dane tekstowe w polach ``text`` lub ``tail``.

.. code-block:: pycon

    >>> root = etree.Element("root")
    >>> root.text = "TEXT"
    >>> print( etree.tostring(root) )
    <root>TEXT</root>

    # Zapis fragmentu <html><body>Hello<br/>World</body></html>
    >>> html = etree.Element("html")
    >>> body = etree.SubElement(html, "body")
    >>> body.text = "Hello"
    >>> br = etree.SubElement(body, "br")
    >>> br.tail = "World"
    >>> print( etree.tostring(html) )
    <html><body>Hello<br/>World</body></html>

Iteracja po drzewie elementów
=============================

Rekursywna iteracja
-------------------

Rekursywna iteracja po drzewach elementów – metoda ``iter()``

.. code-block:: pycon

    >>> root = etree.Element("root")
    >>> etree.SubElement(root, "child").text = "Child 1"
    >>> etree.SubElement(root, "child").text = "Child 2"
    >>> etree.SubElement(root, "another").text = "Child 3"
    <root>
      <child>Child 1</child>
      <child>Child 2</child>
      <another>Child 3</another>
    </root>
    >>> for element in root.iter():
    ...     print( "{} - {}".format(element.tag, element.text) )
    root - None
    child - Child 1
    child - Child 2
    another - Child 3

Iteracja po przefiltrowanych węzłach
------------------------------------

.. code-block:: pycon

    >>> for element in root.iter("child"):
    ...     print() "{} {}".format(element.tag, element.text))
    child - Child 1
    child - Child 2

Serializacja
============

* funkcja ``tostring()`` zwracająca string
* metoda ``ElementTree.write()`` - zapis do pliku, obiektu plikowego lub URL
* argumenty: ``pretty_print`` oraz ``encoding``

Klasa ElementTree
=================

ElementTree
    klasa opakowująca drzewo wraz z węzłem początkowym (``root``).
    Dostarcza szereg metod parsujących oraz serializujących dokument.

.. code-block:: pycon

    # Parsowanie dokumentu xml – zwraca obiekt ElementTree
    >>> tree = etree.parse(StringIO("""
    ... <?xml version="1.0"?>
    ... <!DOCTYPE root SYSTEM "test" [ <!ENTITY tasty "eggs"> ]>
    ... <root>
    ...  <a>&tasty;</a>
    ... </root>
    ... """))

.. code-block:: pycon

    # Zapis do pliku XML
    >>> tree.write("test.xml",
    ... pretty_print=True)
    <!DOCTYPE root SYSTEM "test"
    [<!ENTITY tasty "eggs">]>
    <root>
      <a>eggs</a>
    </root>


Parsowanie dokumentów XML
=========================

* parsowanie plików lub obiektów plikowych – funkcja ``parse()``

.. code-block:: pycon

    >>> some_file_like = StringIO("<root>data</root>")
    >>> tree = etree.parse(some_file_like)
    >>> etree.tostring(tree)
    '<root>data</root>'

* parsowanie stringów - funkcja ``fromstring()`` lub ``XML()``

.. code-block:: pycon

    >>> some_xml_data = "<root>data</root>"
    >>> root = etree.fromstring(some_xml_data)
    >>> print( etree.tostring(root) )
    <root>data</root>

    >>> root = etree.XML(some_xml_data)
    >>> print( root.text )
    data

ElementPath
===========

ElementPath
    język zapytań podobny do Xpath

Metody:

``iterfind()``
    iteruje po wszystkich elementach, które pasują do wyrażenia filtrującego

``findall()``
    zwraca listę pasujących elementów

``find()``
    zwraca pierwszy pasujący element

``findtext()``
    zwraca  zawartość .text pasującego elementu

.. code-block:: pycon

    >>> root = etree.XML("<root><a x='123'>aText<b/><c/><b/></a></root>")

    # Znajdź element podrzędny
    >>> print( root.find("b") )
    None
    >>> print( root.find("a").tag )
    a

    # Znajdź element w drzewie
    >>> print( root.find(".//b").tag )
    b
    >>> [b.tag for b in root.iterfind(".//b")]
    ['b', 'b']

    # Znajdź elementy z danym atrybutem
    >>> print( root.findall(".//a[@x]")[0].tag )
    a
    >>> print( root.findall(".//a[@y]") )
    []