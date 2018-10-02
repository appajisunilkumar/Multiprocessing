
import time
import Queue
import threading as th
import multiprocessing as mp

## function for Prime numbers
def isprime(n):
    for i in range(2, int(n**(0.5))+1):
        if n%i == 0:
            return False
    return True

##  function for Nth postion of prime number
def prime(Nth, q=None):
    n_found = 0
    i = 0
    while n_found<Nth:
        i += 1
        n_found = n_found + int(isprime(i))
    if q: #queue, for returning value from different processes
        q.put(i)
    return i
start = 100000



if __name__ == '__main__':
    t1 = time.time()
    print prime(start), prime(start+1), prime(start+2), prime(start+3)
    print 'Serial test took ', time.time()-t1, 'seconds' ## time serial segment
 
    t2 = time.time()
    q = Queue.Queue()
    jobs = [th.Thread(target=prime, args=(start,q))\
            ,th.Thread(target=prime, args=(start+1, q))\
            ,th.Thread(target=prime, args=(start+2, q))\
            ,th.Thread(target=prime, args=(start+3, q))]
 
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    print 'MultiThreading test took', time.time()-t2, 'seconds' ## time multi threading segment
 
    q = mp.Queue()
    t3 = time.time()
    jobs = [mp.Process(target=prime, args=(start, q))\
            ,mp.Process(target=prime, args=(start+1,q))\
            ,mp.Process(target=prime, args=(start+2, q))\
            ,mp.Process(target=prime, args=(start+3, q))]
 
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    print 'MultiProcessing test took', time.time()-t3, 'seconds' ## time multi processing threading
 
 
    """
        multiprocessing.Pool() provides a map like interface with automatic
        parallelization among Pool of workers
    """
    #t4 = time.time()
    #pool = mp.Pool(processes=4)
    #result = pool.map(prime, range(start, start+4))
    #print result
    #print 'Pool test took', time.time()-t4, 'seconds'