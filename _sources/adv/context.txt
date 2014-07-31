Menadżery kontekstu
###################

Wprowadzenie
************

Często spotykany w zarządzaniu zasobami jest następujący wzorzec:

.. code-block:: python

    do_setup()

    try :
        do_task()

    except SomeError :
        handle_the_error()

    finally :
        do_cleanup()

Wyrażenie ``with``
******************

Aby uprościć i uodpornić się na błędy programisty, od Pythona 2.5 wzwyż
dostępne jest wyrażenie *with*

Menedżer kontekstu (context manager)
    jest odpowiedzialny za zarządzanie zasobami wewnątrz bloku kodu.
    Najczęściej tworzy te zasoby na początku bloku, a zwalnia na końcu.
    Przykładowo - menadżer kontekstu dla plików upewnia się, że pliki
    zostały prawidłowo zamknięte po zakończenu bloku

.. code-block:: python

    with open('myfile.txt', 'wt') as f:
        f.write('foo bar')

Jak działa ``with``
===================

Odpowiednikiem bloku:

.. code-block:: python

    with VAR = EXPR:
        BLOCK

może być zapis:

.. code-block:: python

    VAR = EXPR
    VAR.__enter__()
    try:
        BLOCK
    finally:
        VAR.__exit__()

Jak napisać menadżera kontekstu?
================================

Menedżer kontekstu jest klasą posiadającą dwie metody specjalne:

__enter__
  metoda ta jest wywoływana na samym początku bloku wewnątrz *with*

__exit__
  metoda ta jest odpowiednikiem *finally:*, wywoływana jest po zakończeniu
  bloku *with*

.. code-block:: python

    class Context(object):

        def __init__(self):
            print '__init__()'
        def __enter__(self):
            print '__enter__()'
            return self
        def __exit__(self, exc_type, exc_val, exc_tb):
            print '__exit__()'

    with Context():
        print 'Doing work in the context'

Kontekst
========

Wartością zwracaną przez menadżera kontekstu w funkcji ``__enter__``
może być obiekt, który zostanie przypisany do zmiennej występującej po ``as``

.. code-block:: python

    class WithinContext(object):
        def do_something(self):
            print 'do_something()'

    class Context(object):
        def __enter__(self):
            print 'Context.__enter__()'
            return WithinContext(self)

    with Context() as c:
        c.do_something()

metoda ``__exit__``
===================

Do metody __exit__ trafia informacja o wyjątkach, jakie pojawiły się bloku
*with*. Jeśli metoda __exit__ zwróci *true* to znaczy że wyjątek został
obsłużony przez menadżera kontekstu. Jeśli zwrócona zostanie wartość *false*
to oznacza to że wyjątek propaguje się dalej.

.. code-block:: python

    def __exit__(self, exc_type, exc_val, exc_tb):
        print "Exception type: ", exc_type
        print "Exception value: ", exc_val
        print "Traceback object: ", exc_tb
        return true #or false

``contextlib``
**************

W prostych przypadkach zamiast tworzyć klasę, możemy skorzystać z gotowego
dekoratora zawartego w module *contextlib*, który konwertuje składnię funkcji
do postaci menadżera kontekstu:

.. code-block:: python

    @contextlib.contextmanager
    def make_context():
        try:
            prepare_resource()
            yield context_object
        except RuntimeError, err:
            handle_exception_here()
        finally:
            do_clean_up()

``contextlib.contextmanager``
=============================

.. code-block:: pycon

    >>> @contextmanager
    ... def MyContext():
    ...   print('going in')
    ...   yield
    ...   print('coming out')
    ...
    >>> with MyContext():
    ...   print('inside')
    going in
    inside
    coming out

Dodatkowo z obsługą wyjątków:

.. code-block:: pycon

    >>> @contextmanager
    ... def MyContext():
    ...   print('going in')
    ...   try:
    ...     yield
    ...   except Exception:
    ...     print('Error!')
    ...   else:
    ...     print('coming out')
    ...
    >>> with MyContext():
    ...   print(1/0)
    going in
    Error!
