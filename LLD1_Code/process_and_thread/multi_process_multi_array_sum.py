from multiprocessing import Process, Queue
from typing import List


def calculate_sum(nums: List[int], result_queue: Queue):
    return result_queue.put(sum(nums))


if __name__ == "__main__":
    nums_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    result_queue = Queue()

    # Create a list of processes for each array of numbers
    sum_calculation_processes = []
    for nums in nums_list:
        process = Process(target=calculate_sum, args=(nums, result_queue))
        sum_calculation_processes.append(process)
        process.start()

    # Wait for each process to finish
    for process in sum_calculation_processes:
        process.join()

    # Accumulate the results of the individual processes
    total_sum = 0
    while not result_queue.empty():
        total_sum += result_queue.get()

    # Print the total sum
    print(f"Total sum: {total_sum}")
