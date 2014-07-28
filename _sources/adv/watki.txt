**************************
Programowanie wielowątkowe
**************************

Zarządzanie wątkami
===================

**Proces**
    egzemplarz wykonywanego programu. Może istnieć wiele różnych procesów wykonujących ten sam program. Każdemu procesowi przydzielane zostają zasoby, takie jak procesor, pamięć, dostęp do urządzeń wejścia-wyjścia, pliki. 

Za zarządzanie procesami odpowiada jądro systemu operacyjnego. System operacyjny zarządza priorytetami procesów.

W systemach wielozadaniowych procesy mogą być wykonywane współbieżnie:

 * Systemy wieloprocesorowe lub wielordzeniowe – współbieżność rzeczywista
 * Jednoprocesorowe – emulacja współbieżności
 * z wywłaszczaniem - pre-emptive multitasking 
 * bez wywłaszczania

**Wątek** (``thread``)
    jest innym rodzajem procesu, wykonywanego współbieżnie w obrębie jednego zadania (programu). Pojedynczy proces może tworzyć i zarządzać wieloma wątkami, które współdzielą się zasobami ( np. plikami, gniazdami, zmiennymi).

Wątki są udostępniane wprost przez system operacyjny:

* MS Windows – Win32 API
* Linux, BSD - pthread 

Problemy z wątkami
==================

**Szeregowanie**
    W systemie jednoprocesorowym jednocześnie można wykonywać tylko jeden wątek. System operacyjny korzysta z algorytmu szeregowania (thread scheduler), który bezustannie przełącza działające wątki, zezwalając na ich działanie przez określony, skończony przedział czasu (time-slice). Wątek jest wywłaszczony jeśli wyczerpie się jego przedział czasu – stan wątku (zmienne lokalne, itp.) jest zapamiętywany

**Współdzielenie zasobów**
    Wątki współdzielą pamięć i inne zasoby. Dwa lub więcej wątków może próbować uzyskać dostęp do tych samych danych w tym samym czasie, co może spowodować wyścig (race condition) i prowadzić do zakleszczenia systemu (deadlock)

Zarządzanie wątkami – synchronizacja
====================================

Wątki mogą być wykonywane równocześnie (współbieżnie). Równoczesny dostęp do wspólnych danych grozi jednak utratą spójności danych i w konsekwencji błędem działania programu. 

Do zapobiegania takim sytuacjom wykorzystuje się mechanizmy synchronizacji wątków, takie jaks semafory, muteksy oraz sekcje krytyczne

Moduł ``threading``
===================

``threading``
    umożliwia obsługę oraz synchronizację wątków.

Konstruktor klasy ``Thread`` umożliwia uruchomienie dowolnej funkcji w nowym wątku.
Utworzony obiekt wątku uruchamiamy za pomocą metody ``start()``.
Synchronizacja z wątkiem głównym odbywa się za pomocą metody ``join()``.
Metoda ``join()`` powróci dopiero w momencie zakończenia się wątku.

.. code-block:: python

    import threading
    import time

    def worker(delay, info):
        for i in range(10):
            time.sleep(delay)
            print(info)
            
    w1 = threading.Thread(target=worker, args=(0.5, "Worker 1"))
    w1.start()
    w1.join()


Tworzenie i wychodzenie z wątków
--------------------------------

Moduł ``threading`` wprowadza klasę ``Thread``, która reprezentuje osobny wątek wykonywania.
Aby zaimplementować nowy wątek za pomocą modułu threading, należy najpierw zdefiniować nową podklasę klasy ``Thread``.
Metoda ``__init__(self [, args])`` jest nadpisywana w celu dodania dodatkowych argumentów ``args``.
Następnie należy nadpisać metodę ``run(self [, args])`` w celu zaimplementowania tego, co wątek powinien robić po rozpoczęciu.
Po utworzeniu nowej podklasy ``Thread`` można utworzyć jej obiekt, a następnie rozpocząć nowy wątek poprzez wywołanie metody ``start()``.

Przykład:

.. code-block:: python

    import threading
    import time
    do_exit = False

    class newThread(threading.Thread):

        def __init__(self, threadID, name, counter):
            self.threadID = threadID 
            self.name = name 
            self.counter = counter 
            threading.Thread.__init__(self)

        def run(self):
            print("Rozpoczynam " + self.name)
            print_time(self.name, self.counter, 5)
            print("Kończę " + self.name)

        def print_time(threadName, delay, counter):
            while counter:
                if do_exit:
                   return
                time.sleep(delay)
                print("{}: {}".format(threadName, time.ctime(time.time())))
                counter -= 1

    # Utworzenie nowych wątków
    thread1 = newThread(1, "Wątek01", 1)
    thread2 = newThread(2, "Wątek02", 2)

    # Rozpoczęcie nowych wątków
    thread1.start()
    thread2.run()

    while thread2.is_alive():
        if not thread1.is_alive():
           do_exit = True
        pass
    print "Kończenie głównego wątku" 

.. code-block:: python

    Rozpoczynam Wątek01
    Rozpoczynam Wątek02
    Wątek01: Wed Jun 14 13:06:10 2008
    Wątek01: Wed Jun 14 13:06:11 2008
    Wątek02: Wed Jun 14 13:06:11 2008
    Wątek01: Wed Jun 14 13:06:12 2008
    Wątek01: Wed Jun 14 13:06:13 2008
    Wątek02: Wed Jun 14 13:06:13 2008
    Wątek01: Wed Jun 14 13:06:14 2008
    Kończę Wątek01
    Wątek02: Wed Jun 14 13:06:15 2008
    Kończenie głównego wątku

Synchronizacja wątków
---------------------

Moduł ``Threading`` biblioteki Pythona zawiera łatwy do zaimplementowania mechanizm blokowania, który pozwala na synchronizację wątków. Nowa blokada jest tworzona poprzez wywołanie metody ``Lock()`` zwracającej nową blokadę.

.. code-block:: python

    threadLock = threading.Lock()
    # ...
    threadLock.acquire()
    # Sekcja krytyczna
    threadLock.release() 

Po utworzeniu nowego obiektu blokady, można zmusić wątki do synchronicznego działania poprzez wywołanie metody ``acquire([blocking])``.

Opcjonalny argument blocking pozwala na kontrolowanie, czy wątek ma czekać na otrzymanie blokady:

 - ``0`` - metoda zakończy działanie zwracając 0, jeśli blokada nie może być uzyskana lub 1, jeśli zostanie uzyskana
 - ``1`` - wątek zostanie zablokowany i będzie oczekiwał na zwolnienie blokady

Kiedy blokada ma być zakończona, jest ona zwalniania poprzez wywołanie metody ``release()`` nowego obiektu blokady.

Przykład:

.. code-block:: python

    thread_lock = threading.Lock()

    ...

        def print_time(threadName, delay, counter):
            while counter:
                if do_exit:
                   return
                time.sleep(delay)
                thread_lock.acquire()
                print("{}: {}".format(threadName, time.ctime(time.time())))
                thread_lock.release()
                counter -= 1
    ...

    threads = []
    # Tworzenie nowych wątków
    thread1 = newThread(1, "Wątek01", 1)
    thread2 = newThread(2, "Wątek02", 2)
    # Rozpoczynanie nowych wątków
    thread1.start()
    thread2.start()
    # Dodawanie wątków do listy wątków
    threads.append(thread1)
    threads.append(thread2)
    # Czekanie na zakończenie wszystkich wątków
    for t in threads:
        t.join()
    print "Kończenie głównego wątku" 

.. code-block:: python

    Rozpoczynam Wątek01
    Rozpoczynam Wątek02
    Wątek01: Wed Jun 14 10:06:24 2008
    Wątek01: Wed Jun 14 10:06:25 2008
    Wątek01: Wed Jun 14 10:06:26 2008
    Wątek02: Wed Jun 14 10:06:28 2008
    Wątek02: Wed Jun 14 10:06:30 2008
    Wątek02: Wed Jun 14 10:06:32 2008
    Kończenie głównego wątku


Kolejny przykład - menadżer kontekstu:

.. code-block:: python

    import threading 
    import time

    thread_lock = threading.Lock()

    class newThread (threading.Thread):
        def __init__(self, threadID, name, counter):
            self.threadID = threadID 
            self.name = name 
            self.counter = counter 
            threading.Thread.__init__(self)

        def run(self):
            print "Rozpoczynam " + self.name 
            # Otrzymanie blokady w celu zsynchronizowania wątków
            with thread_lock:
                print_time(self.name, self.counter, 3)    

        def print_time(threadName, delay, counter):
            while counter:
                time.sleep(delay)
                print "%s: %s" % (threadName, time.ctime(time.time()))
                counter -= 1

Moduł ``queue``
===============

Moduł ``queue`` pozwala na tworzenie synchronizowanych obiektów kolejek, które będą przechowywać określoną liczbę elementów.
Obiekt Queue umożliwia bezpieczną wymianę danych między wątkami. Przydatny do implementacji wzorca *Producer/Consumer*.

Najważniejsze metody:

``__init__(maxsize)``
    Inicjalizacja kolejki. Jeśli maxsize > 0 wątek próbujący dodać element do kolejki zostanie zablokowany.

``qsize()``
    Zwraca bieżący rozmiar kolejki 

``empty()``
    Zwraca ``True`` jeśli kolejka jest pusta

``full()``
    Zwraca ``True`` jeśli kolejka jest pełna 

``put(item)``
    Włożenie elementu do kolejki 

``get()``
    Wyciągnięcie elementu z kolejki 

``put_nowait(item)``
    Nieblokująca wersja put(item). Zgłasza Queue.Full, jeśli kolejka jest pełna

``get_nowait()``
    Nieblokująca wersja get(). Zgłasza Queue.Empty 

*Producer/Consumer*:

.. code-block:: python

    import queue

    def worker():
        while True:
            item = q.get()
            do_work(item)
            q.task_done()

    q = queue.Queue()

    for i in range(num_worker_threads):
        t = Thread(target=worker)
        t.daemon = True
        t.start()
    
    for item in source():
        q.put(item)
    
    q.join() # czekanie na zakończenie wątku


Wątki z przerwaniem zegarowym
=============================

Wątki z przerwaniem zegarowym (*timer-interrupted*) służą do czyszczenia zasobów, dostarczania powiadomień oraz sprawdzania statusu.

Metoda ``Timer(interval, func [, args [, kwargs]])`` modułu ``Threading`` tworzy nowy obiekt wątku z przerwaniem zegarowym.

``interval``
    określa liczbę sekund, które należy odczekać przed wykonaniem funkcji określonej w argumencie ``func``.

Inicjalizacja wątku z przerwaniem zegarowym
-------------------------------------------

``start()``
    wątek odczeka określony interwał czasu, a następnie rozpocznie wykonywanie.

``cancel()``
    anulowanie wątku pod warunkiem, że funkcja nie została jeszcze wykonana.

Przykład:

.. code-block:: python

    import threading 
    import os

    def clean_queue (qPath):
        jobList = os.listdir(qPath)
        for j in jobList:
           delPath = "%s/%s" % (qPath, j)
           os.remove(delPath)
           print "Usuwanie " + delPath 

    qPath = "/print/queue01"
    waitTime = 600 #10 minut

    # Utworzenie wątku z przerwaniem zegarowym
    wakeCall = threading.Timer(waitTime, clean_queue, (qPath ,))

    # Rozpoczęcie wątku z przerwaniem zegarowym
    wakeCall.start()

.. code-block:: python

    Usuwanie /print/queue01/102.txt
    Usuwanie /print/queue01/103.txt
    Usuwanie /print/queue01/104.txt
    Usuwanie /print/queue01/105.txt
    Usuwanie /print/queue01/106.txt
    Usuwanie /print/queue01/107.txt

Moduł ``concurrent``
====================

Bardzo interesującą biblioteką wspierającą asynchroniczne wywołania jest ``concurrent.futures``, która jest częścią biblioteki standardowej od wersji 3.2. Istnieje też backport dla Pythona z serii 2.6-2.7

Moduł ma za zadanie uprościć zrównoleglanie prostych zadań.

Najprostszym sposobem jest użycie *ThreadPoolExecutor*

.. code-block:: python

    from concurrent import futures
    from time import sleep

    def worker(name="name", delay=1):
        for i in xrange(5):
            print name
            sleep(delay)
        return name + " has finished"
        
    with futures.ThreadPoolExecutor(max_workers=4) as e:
        futu1 = e.submit(worker, "worker 1", 1)
        futu2 = e.submit(worker, "worker 2", 0.35)

Wynikiem jest obiekt *Future*, który udostępnia metody:

``running()``
    sprawdza czy zadanie się wciąż wykonuje

``result()``
    zwraca wynik wygenerowany przez funkcję roboczą (działa podobnie do ``threading.Thread.join()``}


``futures.as_completed(futures_iterable)`` zwraca obiekty *Future* w kolejności ich wykonania.

.. code-block:: python

    from concurrent import futures
    from time import sleep
    from random import randint

    def worker(name="name"):
        sleep(randint(0,2)*0.01)
        return name + " has finished"
        
    names = ["Worker {0}".format(i) for i in range(1,10)]
        
    with futures.ThreadPoolExecutor(max_workers=4) as e:
        threadlist = [e.submit(worker, name) for name in names]
        
        for future in futures.as_completed(threadlist):
            print( future.result() )

*ThreadPoolExecutor* zawiera również asynchroniczne wersje wyrażeń funkcyjnych, ``map``:

.. code-block:: python

    with futures.ThreadPoolExecutor(max_workers=4) as e:
        results = e.map(worker, names)
        
        for res in results:
            print( res )
        #print( list(results) )


Moduł ``multiprocessing``
=========================

Aby obejść ograniczenia związane z istnieniem Global Interpreter Lock powstał moduł ``multiprocessing``
wykorzystujący API zbliżone do modułu ``threading``, ale tworzące procesy zamiast wątków.

Weźmy pod uwagę pierwszy program jaki testowaliśmy:

.. code-block:: python

    import multiprocessing
    import time

    def worker(delay, info):
        for i in range(10):
            time.sleep(delay)
            print(info)


    if __name__ == '__main__':
        w1 = multiprocessing.Process(target=worker, args=(0.5, "Worker 1"))
        w1.start()
        w1.join()

Należy pamiętać o utworzeniu nowego procesu wewnątrz ``if __name__ == '__main__':``

Moduł ``multiprocessing`` dostarcza reimplementacji takich klas jak ``Queue`` oraz ``Lock``.

Oprócz klas i funkcji kompatybilnych z ``threading`` dodane są też klasy specyficzne dla podprocesów

.. py:class:: Pipe

   Klasa opakowująca dwukierunkowe połączenia między procesami

Oraz klasy które pozwalają na przechowywanie struktur danych w tzw. pamięci współdzielonej:

.. py:class:: Value
.. py:class:: Array

Oraz własną implementację wzorca *Pool*:

.. code-block:: python

    from  multiprocessing import Pool
    import time

    def worker(delay, info):
        for i in range(10):
            time.sleep(delay)
            print(info)

    names = ["Worker {0}".format(i) for i in range(1,10)]

    if __name__ == '__main__':
        with Pool(processes=4) as pool:
            results = [pool.apply_async(worker, (0.5, name)) for name in names]
            for res in results:
                print(res.get())




