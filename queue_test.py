import queue
import time
import threading
from get_video import get_video

def work(i):
    while True:
        num = q.get()
        if num is None:
            print("Number of task for thread is none")
            break
        print("Thread %s is processing on %s's task" %(i,num))

        q.task_done()

if __name__=='__main__':
    foldername = ['blakelively','sehun','baekhyun','evanlin','chanyeol','EXO']
    keyword = ['blakelively','sehun','baekhyun','evanlin','chanyeol','EXO']
    source = (('blakelively','blakelively'),('sehun','sehun'),('baekhyun','baekhyun'),('evanlin','evanlin'),('chanyeol','chanyeol'),('EXO','EXO'))
    num_of_threads = 3
    q = queue.Queue()
    threads = []
    for i in range(1, num_of_threads+1):
        t = threading.Thread(target = work, args = (i,))
        threads.append(t)
        t.start()

    for name in foldername:
        time.sleep(1)
        q.put(name)

    q.join()
    print('All searches done.')

    for i in range(num_of_threads):
        q.put(None)
    for t in threads:
        t.join()
    print(threads)


