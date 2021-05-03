# Simple implementation of a queue class
import time
from collections import deque


class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def front(self):
        return self.buffer[-1]


# Data structure tutorial exercise: Queue
# For all exercises use Queue class implemented in main tutorial.
#
# Design a food ordering system where your python program will run two threads,
#
# Place Order: This thread will be placing an order and inserting that into a queue.
# This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
# Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it.
# This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.
# Use this video to get yourself familiar with multithreading in python
#
# Pass following list as an argument to place order thread,
#
# orders = ['pizza','samosa','pasta','biryani','burger']
# This problem is a producer,consumer problem where place_order thread is producing orders whereas server_order thread
# is consuming the food orders. Use Queue class implemented in a video tutorial.
#
# Solution
#
# Write a program to print binary numbers from 1 to 10 using Queue. Use Queue class implemented in main tutorial.
# Binary sequence should look like,
#     1
#     10
#     11
#     100
#     101
#     110
#     111
#     1000
#     1001
#     1010
# Hint: Notice a pattern above. After 1 second and third number is 1+0 and 1+1.
# 4th and 5th number are second number (i.e. 10) + 0 and second number (i.e. 10) + 1.
#
# You also need to add front() function in queue class that can return the front element in the queue.

import threading
from time import sleep


def place_order(orders):
    for order in orders:
        queue.enqueue(order)
        print("New Order:", order)
        sleep(.5)


def serve_order():
    while not queue.is_empty():
        print("Order up", queue.dequeue())
        sleep(2)


queue = Queue()
orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']

t1 = threading.Thread(target=place_order, args=(orders,))
t2 = threading.Thread(target=serve_order)

t1.start()
sleep(1)
t2.start()

t1.join()
t2.join()

def produce_binary_numbers(n):
    numbers_queue = Queue()
    numbers_queue.enqueue("1")

    for i in range(n):
        front = numbers_queue.front()
        print("   ", front)
        numbers_queue.enqueue(front + "0")
        numbers_queue.enqueue(front + "1")

        numbers_queue.dequeue()

produce_binary_numbers(10)