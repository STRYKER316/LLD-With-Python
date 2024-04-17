from threading import Thread, get_native_id
import os


# Custom Thread class
class MyThread(Thread):
    # method to be executed by thread
    def run(self):
        print("Hello from a thread")
        print(f"Process id is: {os.getpid()}")
        print(f"Thread id is: {get_native_id()}")


if __name__ == '__main__':
    thread1 = MyThread()
    thread2 = MyThread()

    thread1.start()
    thread2.start()
