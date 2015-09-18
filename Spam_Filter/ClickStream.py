import math


dictFeatureIndex = {}
dictRow = {}
dictFeatureEntropy = {}
dictFeatureYes = {}
totalYes = 0
totalRowsInTrainingSet = 0
finished = [0]
localDictRow = {}


def openFile():
    
    with open("featnames.txt", 'rb') as feat:
        cc = 0
        for line in feat.readlines():
            dictFeatureIndex.update({cc:0})
            cc = cc + 1

    dictRow = dict(dictFeatureIndex)
    putRowIntoDict()
    
def putRowIntoDict():
    global totalRowsInTrainingSet
    with open("trainfeat.txt", 'rb') as csvfile:
        count = 0
        for line in csvfile.readlines():
            dictRow[count]= line
            count = count + 1
        totalRowsInTrainingSet = count
        

def featureSplit(localDictRow,dictFeatureIndex):
    for y in dictFeatureIndex.keys():
        for k in localDictRow.keys():
            strn = localDictRow[k].split(" ")
            c = 0
            if int(strn[y]) <=1 :
                c = c +1 
            dictFeatureYes.update({y:c})
    ck = 0
    for k in dictFeatureYes.keys():   
        if float(dictFeatureYes[k]) / totalRowsInTrainingSet == 0 or totalRowsInTrainingSet - float(dictFeatureYes[k]) / totalRowsInTrainingSet == 0:
            ck = ck + 1   
    if ck == k:
        return True
    else:
        return False
    
        

def calculateEntropy():
    for k in dictFeatureYes.keys():
        entropy = - (float(dictFeatureYes[k]) / totalRowsInTrainingSet) * math.log(float(dictFeatureYes[k]) / totalRowsInTrainingSet, 2) - (totalRowsInTrainingSet - float(dictFeatureYes[k]) / totalRowsInTrainingSet) * math.log(totalRowsInTrainingSet - float(dictFeatureYes[k]) / totalRowsInTrainingSet, 2)
        entropy = entropy * (-1)
        print entropy
        dictFeatureEntropy.update({k:entropy})
    c = 0
    for k in dictFeatureEntropy.keys():
        s = 0
        if dictFeatureEntropy[k] > s:
            c = k
    print c
            

def main():
    openFile()
    
    
    """for fc in dictRow.keys():
        print dictRow[fc]"""
    
class Node:
    def __init__(self, val):
        self.left_child = None
        self.right_child = None
        self.data = val
        
def node_insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left_child == None:
                root.left_child = node
            else:
                node_insert(root.left_child, node)
        else:
            if root.right_child == None:
                root.right_child = node
            else:
                node_insert(root.right_child, node)
                
def condition_satisfy(localDictRow,dictFeatureIndex):
    
    
def createDecisionTree(localDictRow,dictFeatureIndex):
    print "createDecisionTree"
    if featureSplit(localDictRow,dictFeatureIndex) == True:
        node_insert()
        calculateEntropy()

main()