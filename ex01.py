import threading
import time

def processo(id):
    time.sleep(0.5)
    print("Thread " + str(id))

def main():
    threads = []
    for i in range(5):
        t = threading.Thread(target=processo, args=(i,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

if __name__ == '__main__':
    main()