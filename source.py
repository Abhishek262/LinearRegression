''' Algorithm for simple linear regression.
Takes in random parts of the dataset as Training and Testing databases
and outputs the RMSE
                                                                         '''
#imports
import math,random,csv
import numpy as np


class line :
    def __init__(self,m,c) :
        self.m = m
        self.c = c

    def val(self,x) :
        y = self.m*x + self.c
        return y

#class for Training set, Test set
class dataSet :
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

        
#takes training data set and returns the value of 'c' for it - or the intercept of the best fit line
def cFinder(trainsetobj) :

    c = (((trainsetobj.meanx*trainsetobj.meanxy) - (trainsetobj.meany*trainsetobj.sqmeanx))/((trainsetobj.meanx**2) - (trainsetobj.n*trainsetobj.sqmeanx)))
    return c
#For m
def mFinder(trainsetobj) :
    m = (((trainsetobj.meanx*trainsetobj.meany) - (trainsetobj.n*trainsetobj.meanxy))/((trainsetobj.meanx**2) - (trainsetobj.n*trainsetobj.sqmeanx)))
    return m


#Collects data and divides it into 2 sets from the Swedish Auto Insurance Database . foo- file object
def read(foo):

    fil = csv.reader(foo,  delimiter = ',')
    line_count = 0
    data = []
    Traindata = []
    Testdata = []
    
    for row in fil :
        if line_count == 0 :
            line_count +=1
            continue
        else :
            temp = []
            temp.append(float(row[0]))
            temp.append(float(row[1]))
            line_count +=1
            data.append(temp)

    line_count = line_count -1
    start = random.randrange(10,line_count/2)
    end=  random.randrange(line_count/2,line_count)
    for i  in range(start,end) :
        Traindata.append(data[i])
    
    for i in range(0,start) :
        Testdata.append(data[i])
    for i in range(end,line_count) :
        Testdata.append(data[i])
    

    return Traindata, Testdata

#Outputs the rmse and gets the values of predicted y for the test data, takes a line and Dataset object as an argument
def LinearRegression(line,Testdataset)  :
    y = []
    predictedy = []
    Testset = Testdataset.arr
    for element in  Testset :
        y.append(element[1])

    for element in Testset :
        predictedy.append(line.val(element[0]))

    sumy = 0

    for i in range(0,len(y)) :
        sumy += (y[i]-predictedy[i])**2
        
    #uses the rmse formula            
    rmse = math.sqrt(sumy/Testdataset.n)

    return rmse

#Just a function to init the program
def start()  :
    readFile = file('Datasets\Insurance_claims.csv','rb')
    #Assigns data to training and test databases
    Tr_set , Ts_set = read(readFile)
    #creates dataset objects using the assigned data above
    Trainset = dataSet(Tr_set)
    Testset = dataSet(Ts_set)

    #Using tbe Traindataset, get the values of m and c adn hence a best fit line corresponding to the Traindataset
    best_fit_line = line(mFinder(Trainset),cFinder(Trainset))

    print("The RMSE score is  : ",LinearRegression(best_fit_line,Testset))

start()
while True :
    x = int(input("Try again?(0/1) : "))

    if x == 0 :
        break

    elif x==1 :
        start()
    else :
        print("Enter 0 or 1")
    







    
