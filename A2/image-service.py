from time import sleep
from threading import Timer

def read_image_service():
    file2 = open("/Users/jonnawaage/Documents/GitHub/CS361/A2/image-service.txt", "r")
    image_set = (["0001.png", "0002.png", "0003.png", "0004.png","0005.png","0006.png", "0007.png", 
                  "0008.png","0009.png", "0010.png"])
    contents = file2.read()
    if (contents > '0010.png'):
        num = int(contents)
        num = num % 10
        file1 = open("/Users/jonnawaage/Documents/GitHub/CS361/A2/image-service.txt","w+")
        file1.write(image_set[num])
        file1.close()
    file2.close()


class Repeat(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)

t = Repeat(3.0, lambda: read_image_service())
t.start()

