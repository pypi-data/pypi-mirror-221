from keystackEnv import keystackObj
import time, sys

keystackObj.logInfo('Running Sample Module Demo/bgp.py')

# Create a failure
keystackObj.logFailed('Failed: No BGP routes discovered')

time.sleep(0)

import threading

def print_cube(num):
    # function to print cube of given num
    keystackObj.logInfo("Cube: {}" .format(num * num * num))

def print_square(num):
    # function to print square of given num
    keystackObj.logInfo("Square: {}" .format(num * num))

t1 = threading.Thread(target=print_square, args=(10,))
t2 = threading.Thread(target=print_cube, args=(10,))

# starting thread 1
t1.start()
# starting thread 2
t2.start()

# wait until thread 1 is completely executed
t1.join()
# wait until thread 2 is completely executed
t2.join()

# both threads completely executed
keystackObj.logInfo("Done!")

