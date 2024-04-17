import multiprocessing
import os


def print_process_id():
    # Both of the following lines will print the same process ID
    print(f"Process ID: {multiprocessing.current_process().pid}")
    print(f"Process ID: {os.getpid()}")


if __name__ == "__main__":
    print_process_id()
    another_process = multiprocessing.Process(target=print_process_id)
    another_process.start()
