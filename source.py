''' Algorithm for simple linear regression
                                        '''

import math,random
import numpy as np

class line :
    def __init__(self,m,c) :
        self.m = m
        self.c = c

    def val(self,x) :
        y = self.m*x + self.c
        return y

class trainSet :
    def __init__(self,arr) :
        self.arr = arr
        self.meanx = 0
        self.meany = 0
        self.meanxy = 0
        self.sqmeanx = 0
        self.n =len(self.arr)
        self.mean_x()
        self.mean_y()
        self.mean_xy()
        self.sq_meanx()

    def mean_x(self) :
        lx = []
        for pairs in self.arr :
            lx.append(pairs[0])

        self.meanx = np.mean(lx)

    def mean_y(self) :
        ly = []
        for pairs in self.arr :
            ly.append(pairs[0])

        self.meany = np.mean(ly)
    
    def mean_xy(self) :
        lxy = []
        for pairs in self.arr :
            lxy.append((pairs[0]*pairs[1]))
        self.meanxy = np.mean(lxy)

    def sq_meanx(self) :
        ls = []
        for pairs in self.arr :
            ls.append((pairs[0]**2))

        self.sqmeanx = np.mean(ls)

        

def dataCollector(foo) :
    pass


def cFinder(trainsetobj) :

    c = (((trainsetobj.meanx*trainsetobj.meanxy) - (trainsetobj.meany*trainsetobj.sqmeanx))/((trainsetobj.meanx**2) - (trainsetobj.n*trainsetobj.sqmeanx)))
    return c

def mFinder(trainsetobj) :
    m = (((trainsetobj.meanx*trainsetobj.meany) - (trainsetobj.n*trainsetobj.meanxy))/((trainsetobj.meanx**2) - (trainsetobj.n*trainsetobj.sqmeanx)))
    return m



