from math import expm1
import math
import os


repeatWords = {}
dict = {}
globalDictHam = {}
globalDictSpam = {}
globalDict = {}
totalHam = 0
totalSpam = 0
c =0
    
def splitEmail():
    lines = open("train").read().splitlines()
    for x in lines:
        featuresOfEmail(x)


def featuresOfEmail(lines):
    global totalHam
    global totalSpam
    features = lines.split(" ")
    for x in xrange(len(features)):
        if x==0:
            continue
        if x==1:
            if features[x] == "ham":
                totalHam = totalHam +1
            if features[x] == "spam":
                totalSpam = totalSpam + 1
            #repeatWords.update({features[x]:"type"})
            continue
        if features[x].isalpha():
            if features[x] not in repeatWords:
                repeatWords.update({features[x]:features[x+1]})
            else:
                temp = repeatWords[features[x]]
                repeatWords.update({features[x]:int(temp) + int(features[x+1])})
                
        if features[1] == "ham":
            if features[x].isalpha():
                if features[x] not in globalDictHam:
                    globalDictHam.update({features[x]:features[x+1]})
                else:
                    temp = globalDictHam[features[x]]
                    globalDictHam.update({features[x]:int(temp)+int(features[x+1])})
                    
        if features[1] == "spam":
            if features[x].isalpha():
                if features[x] not in globalDictSpam:
                    globalDictSpam.update({features[x]:features[x+1]})
                else:
                    temp = globalDictSpam[features[x]]
                    globalDictSpam.update({features[x]:int(temp)+int(features[x+1])})
                    
        if features[x].isalpha():
                if features[x] not in globalDict:
                    globalDict.update({features[x]:features[x+1]})
                else:
                    temp = globalDict[features[x]]
                    globalDict.update({features[x]:int(temp)+int(features[x+1])})
                
    dict.update({features[0]:repeatWords})
    
    """for x in dict.keys():
        for y in dict[x].keys():
            print y,
        print """""
    
    """for y in dict.keys():
        featureDictionary =  dict[y]
        print "========================================="
        print y
        print "========================================="
        for x in featureDictionary.keys():
            print x,featureDictionary[x]"""
    
    
    

def main():
    global c
    splitEmail()
    prob = 1
    ds = dh =0
    linesTest = open("test").read().splitlines()
    for z in linesTest:
        probListSpam = []
        probListHam = []
        featuresTest = z.split(" ")
        localDict = {}
        for y in xrange(len(featuresTest)):
            if y==0 or y ==1:
                continue
            if featuresTest[y].isalpha():
                if featuresTest[y] not in localDict:
                    localDict.update({featuresTest[y]:featuresTest[y+1]})
        for x in repeatWords.keys():
            if x in localDict.keys():
                if x in globalDictSpam.keys():
                    if x not in globalDictHam:
                        th = 0
                        ts = globalDictSpam[x]
                        probWordInSpam = float(ts)/float(repeatWords[x])
                        probWordInHam = 0
                    else:
                        th = globalDictHam[x]
                        ts = globalDictSpam[x]
                        probWordInSpam = float(ts)/float(repeatWords[x])
                        probWordInHam = float(th)/float(repeatWords[x])
                    finalProbSpam = probWordInSpam / ( probWordInSpam + probWordInHam)
                else:
                    finalProbSpam = 0
                if x in globalDictHam.keys():
                    if x not in globalDictSpam:
                        ts = 0
                        th = globalDictHam[x]
                        probWordInSpam = 0
                        probWordInHam = float(th)/float(repeatWords[x])
                    else:
                        th = globalDictHam[x]
                        ts = globalDictSpam[x]
                        probWordInSpam = float(ts)/float(repeatWords[x])
                        probWordInHam = float(th)/float(repeatWords[x])
                    finalProbHam = probWordInHam / ( probWordInSpam + probWordInHam)
                else:
                    finalProbHam = 0
            else:
                finalProbSpam = 0
                finalProbHam = 0
            
            smoothFinalProbSpam = ((3 * 0.5) + (finalProbSpam * float(globalDict[x])))/(3 + float(globalDict[x]))
            smoothFinalProbHam = ((3 * 0.5) + (finalProbHam * float(globalDict[x])))/(3 + float(globalDict[x]))
            
            probListSpam.append(smoothFinalProbSpam)
            #print "smoothFinalProbSpam",smoothFinalProbSpam
            probListHam.append(smoothFinalProbHam)
            #print "smoothFinalProbHam",smoothFinalProbHam
    
        """prod1 = 1.0
        for l in xrange(len(probListSpam)):
            prod1 = prod1 * float(probListSpam[l])
            
        print "prod1", prod1
            
        prod2 = 1.0
        for l in xrange(len(probListSpam)):
            prod2 = prod2 * (1 - float(probListSpam[l]))
            
        print "prod2", prod2
        
        
        decisionSpam = float(prod1) / ( prod1 + prod2 )
        
        print decisionSpam
        
        prodH1 = 1.0
        for l in xrange(len(probListHam)):
            prodH1 = prodH1 * float(probListHam[l])
            
        print "prodH1", prodH1
            
        prodH2 = 1.0
        for l in xrange(len(probListHam)):
            prodH2 = prodH2 * (1 - float(probListHam[l]))
        
        print "prodH2", prodH2
        
        decisionHam = float(prodH1) / ( prodH1 + prodH2 )
        
        print decisionHam"""
        
        sumSpam = 0
        for l in xrange(len(probListSpam)):
            sumSpam = sumSpam + math.log1p(1-probListSpam[l])-math.log1p(probListSpam[l])
            
        exponentialSpam = expm1(sumSpam)
        
        decisionSpam = 1.0 / (1.0 + float(exponentialSpam))
        
        #print decisionSpam
        
        sumHam = 0
        for l in xrange(len(probListHam)):
            sumHam = sumHam + math.log1p(1-probListHam[l])-math.log1p(probListHam[l])
            
        exponentialHam = expm1(sumHam)
        
        decisionHam = 1.0 / (1.0 + float(exponentialHam))
        
        #print decisionHam
        
        """print "Contents of globalDict"
        for s1 in globalDict.keys():
            print s1, globalDict[s1]
        print ""
            
        print "Contents of globalDictHam"
        for s2 in globalDictHam.keys():
            print s2, globalDictHam[s2]
        print " "
            
        print "Contents of globalDictSpam"
        for s3 in globalDictSpam.keys():
            print s3, globalDictSpam[s3]
        """
            
        
        if decisionSpam >= decisionHam:
            #print "spam"
            ds = ds + 1
            if featuresTest[1].strip()=="spam":
                c = c + 1
        else:
            dh = dh + 1
            print "ham",featuresTest[1]
            if featuresTest[1].strip()=="ham":
                c = c + 1
            
    ch = cs = 0
    for test in linesTest:
        testLine = test.split(" ")
        if testLine[1] == "ham":
            ch = ch + 1
            #print testLine[0]
        else:
            cs = cs + 1
            
    #print "ch",ch,"cs",cs
    #print "dh",dh,"ds",ds
    print "success Rate", math.ceil(float(c)*100/float((ch+cs)))

main() 