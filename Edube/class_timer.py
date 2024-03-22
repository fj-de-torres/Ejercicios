from os import system
import time
def clear():
    system("cls || clear")

class MyTimer:
    def __init__(self, seconds):
        self.seconds = int(seconds)

    def __iter__(self):
        self.seconds += 1
        return self

    def __next__(self):
        
        if self.seconds <= 0:
            raise StopIteration
        else:
            self.seconds -= 1
        return self.seconds

stopwatch_5 = MyTimer(5)
clear()
for second in stopwatch_5:
    if second > 0:
        print(second)
        time.sleep(1.1)
    else:
        print("The End")
