import random
import sys
from time import sleep
from threading import Timer

def read_prng_service():
    file2 = open("/Users/jonnawaage/Documents/GitHub/CS361/A2/prng-service.txt", "r")
    contents = file2.read()
    if (contents == 'run'):
        num = str(generate_random_number())
        file1 = open("/Users/jonnawaage/Documents/GitHub/CS361/A2/prng-service.txt","w+")
        file1.write(num)
        file1.close()
        file2 = open("/Users/jonnawaage/Documents/GitHub/CS361/A2/image-service.txt","w+")
        file2.write(num)
        file2.close()
    file2.close()


def generate_random_number():
    return random.randint(0, sys.maxsize)


class Repeat(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)


t = Repeat(3.0, lambda: read_prng_service())
t.start()

