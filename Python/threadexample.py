#https://stackoverflow.com/questions/2846653/how-to-use-threading-in-python

import os
import sys
import math
import threading

class SummingThread(threading.Thread):
     def __init__(self,low,high):
         super(SummingThread, self).__init__()
         self.low=low
         self.high=high
         self.total=0

     def run(self):
         for i in range(self.low,self.high):
             self.total+=i
             print(self.total)


class Main_Thread(threading.Thread):
     result = 0
         
     def __init__(self,low,high):
         super(Main_Thread, self).__init__()
         self.low = low
         self.high  = high

     def run(self):
         thread1 = SummingThread(self.low,self.high)
         thread2 = SummingThread(self.high,(self.high*2)+1)
         thread1.start() # This actually causes the thread to run
         thread2.start()
         thread1.join()
         thread2.join()
         print(thread1.total,thread2.total)
         print("\n")
         # At this point, both threads have completed
         self.result = thread1.total + thread2.total
         
         

mt = Main_Thread(0,5)
mt.start()
print(mt.result)
mt.join()

    
