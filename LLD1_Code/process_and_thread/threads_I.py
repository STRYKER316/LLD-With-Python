from threading import Thread, get_native_id
import os


# Function to be run by a thread
def print_numbers():
    for i in range(1, 6):
        print(i, end=' ')

    print(f"Process id: {os.getpid()}")
    print(f"Thread id: {get_native_id()}")


if __name__ == "__main__":
    print_numbers()
    another_thread = Thread(target=print_numbers)
    another_thread.start()
