import numpy as np
import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt

class HSPPlotter:
    def __init__(self):
        self._caseList=[]
        self._compareItem=''

    #def loadDataFromFile(filePath):
    def generateData(self, nCase):
        self._caseList = []
        for i in range(nCase):
            self._caseList.append('case'+str(i))
            
        self._refItem = 100.0 + np.random.randn(nCase)
        self._tarItem = 110.0 + np.random.randn(nCase)

    def writeToFile(self, filePath):
        f = open(filePath,'w')
        for i in range(len(self._caseList)):
            line = self._caseList[i] + '\t' + str(self._refItem[i]) + '\t' + str(self._tarItem[i])+'\n'
            f.write(line)
    def readFromFile(self, filePath):
        self._caseList = []
        self._refItem = []
        self._tarItem = []
        with open(filePath, 'r') as f:
            for line in f:
                items = line.split()
                self._caseList.append(items[0])
                self._refItem.append(float(items[1]))
                self._tarItem.append(float(items[2]))
        self._refItem = np.array(self._refItem)
        self._tarItem = np.array(self._tarItem)

    def plotDiff(self, diffType='/'):
        if diffType=='/':
            diff = self._tarItem / self._refItem * 100.0
            xlabel='Change(%)'
        elif diffType=='-':
            diff = self._tarItem - self._refItem
            xlabel='Increase'
        else:
            raise "Invalid diff type"
        ylabel='Count Frequence'
        num_bins = 50
        n, bins, patches = plt.hist(diff, num_bins, normed=1, facecolor='green', alpha=0.5)
        plt.subplots_adjust(left=0.15)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        
        
        plt.show()
        picPath0 = '/static/images/tmp0.svg'
        picPath = 'runresult' + picPath0
        plt.savefig(picPath)
        return picPath0
        
    def generatePics(self):
        self.generateData(50)
        self.writeToFile('test1.txt')
        self.readFromFile('test1.txt')
        picPath = self.plotDiff('/')
        return [picPath]
    
    def plotHist(self, data, title):
        #get diff
        diff = []
        for item in data:
            diff.append(item.value)
        
        diff = np.array(diff)
        ylabel='Count Cases'
        xlabel='Relative Difference(%)'
        num_bins = 10
        plt.clf()#clear config
        plt.subplot(1, 1, 1)
        n, bins, patches = plt.hist(diff, num_bins, normed=0, facecolor='green', alpha=0.5)
        #plt.subplots_adjust(left=0.15)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.suptitle(title+": Histogram of Relative Difference")
        #set ylabel integer
        [xmin, xmax, ymin, ymax] = plt.axis()
        yint = range(0, int(ymax)+2)
        plt.yticks(yint)
        #save fig
        picPath0 = '/static/images/DiffHist.svg'
        picPath = 'runresult' + picPath0
        plt.savefig(picPath)
        return picPath0
    
    def plotBar(self, data, title):
        diff = []
        name = []
        for item in data:
            diff.append(item.value)
            name.append(item.case)
        name = tuple(name)    
        
        diff = np.array(diff)
        x = np.arange(len(data))
        plt.clf()
        plt.subplot(1,1,1)
        plt.bar(x,diff)
        plt.xlabel("Case Index")
        plt.ylabel("Relative Difference(%)")
        plt.suptitle(title+" : Difference for All Cases")
        #plt.xticks(x+0.5, name)
        #plt.show()
        #save fig
        picPath0 = '/static/images/DiffBar.svg'
        picPath = 'runresult' + picPath0
        plt.savefig(picPath)
        return picPath0
        
    def generatePics(self, data, title):
        
        picPath=[]
        if(len(data)==0):
            return picPath
        picPath.append(self.plotBar(data,title) )
        picPath.append(self.plotHist(data, title) )
        return picPath


if __name__=="__main__":
    hspPlotter = HSPPlotter()
    hspPlotter.generateData(200)
    hspPlotter.writeToFile('pics/tmp.txt')
    hspPlotter.readFromFile('pics/tmp.txt')
    hspPlotter.plotChange('/')
