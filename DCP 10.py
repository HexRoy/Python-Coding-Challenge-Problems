#Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

import time

def job_scheduler(f, n):
    print("start")
    time.sleep(n/1000)
    f()

def my_function():
    print("my_functon just ran")


delay = 1000
job_scheduler(my_function, delay)