# -+- coding: utf-8 -*-

import threading,time,datetime
import numpy as np


class TestThreadClass():

    """docstring for TestThread"""

    def __init__(self):
        self.size = 6
        self.n = 5
        self.calCountSub = [500000,1000000,1500000,5000000,10000000,15000000]
        self.dic = {}
        self.flag = []

    def run(self):

        for x in xrange(self.size):
            self.flag.append(1)
            th_name = "th_me"+str(x)
            th_me = threading.Thread(target=self.dummy, name=th_name, args=(th_name, x, self.n, self.calCountSub[x]))
            th_me.start()

        while np.sum(self.flag) > 0: 
            time.sleep(1)
            print self.flag

        return self.dic


    def dummy(self, th_name, x, n, calCountSub):

        #dummy calculatoin
        for i in range(n):
            i = 0
            for c in xrange(calCountSub):
                i += 1
            print " [%s] Sub thread (method) : " % threading.currentThread().getName() + str(datetime.datetime.today()) +"  "+  str(calCountSub)

        # end
        
        self.flag[x] = 0
        self.dic.update({th_name:calCountSub})


if __name__ == '__main__':
    # multithreading

    Threading = TestThreadClass()
    dic = Threading.run()

    print " === start main thread (main) === "
    print dic
    print " == end main thread === "