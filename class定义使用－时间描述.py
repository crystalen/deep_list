import time
class Clock(object):
    def __init__(self,hour=0,min=0,sec=0):
        self.hour=hour
        self.min=min
        self.sec=sec
    
    @classmethod
    def now(cls):
        ctime=time.localtime(time.time())
        return cls(ctime.tm_hour,ctime.tm_min,ctime.tm_sec)


    def run(self):
        self.sec+=1
        if self.sec==60:
            self.min+=1
            self.sec=0
            if self.min==60:
                self.hour+=1
                self.min=0
                if self.hour==24:
                    self.hour=0
    
    def show(self):
        return '%02d:%02d:%02d' % (self.hour,self.min,self.sec)

def main():
    clock=Clock.now()
    while True:
        print(clock.show())
        time.sleep(1)
        clock.run()
main()
    
