class Schedule:
    
    def __init__(self):
        self.className = None
        self.day = {}
        self.courseRecitation = {}
        self.courseDetailsNumber = 0
        self.courseDetailsAttend = "No"
        self.courseRequirement= []
        self.domainTA = []
        self.assignTA = []
        self.taRequiredNumber = 0
        self.closed = False
        self.prune = []

class TA:
    
    def __init__(self):
        self.TAName = None
        self.TAResponsibilities = {}
        self.TASkills = []
        self.assignClass = []
        self.contribution = 1
        self.contriList = {}
        
file_Course_Time = open("Sample", "r")

sequence = 0
classSchedule = file_Course_Time.read()
splitClassSchedule = []
extractLine = []
ScheduleArray = []
currentObject = Schedule
flag = False
checkFlag = []
store = []
NewScheduleArray = []
TAArray = []
DurTA = 90
DurClass = 90

splitClassSchedule = classSchedule.split("\n")
for cl in xrange(len(splitClassSchedule)):
    if splitClassSchedule[cl] == "" :
        sequence = sequence + 1
        continue
    if sequence ==0:
        extractLine = splitClassSchedule[cl].split(",")
        for x in xrange(len(ScheduleArray)):
            if ScheduleArray[x].className == extractLine[0]:
                flag = True
                currentObject = ScheduleArray[x]
                break
        if flag==True:
            newSchedule = currentObject
            count = 1
            for c1 in xrange(len(extractLine)):
                if count < len(extractLine):
                    newSchedule.day.update({extractLine[count]:extractLine[count+1]})
                    count = count + 2
            flag = False
        else:
            newSchedule = Schedule()
            newSchedule.className = extractLine[0]
            count = 1
            for c1 in xrange(len(extractLine)):
                if count < len(extractLine):
                    newSchedule.day.update({extractLine[count]:extractLine[count+1]})
                    count = count + 2
            ScheduleArray.append(newSchedule)
               
    if sequence == 1:
        extractLine = splitClassSchedule[cl].split(",")
        for x in xrange(len(ScheduleArray)):
            if ScheduleArray[x].className == extractLine[0]:
                flag = True
                currentObject = ScheduleArray[x]
                break
        if flag==True:
            newSchedule = currentObject
            count = 1
            for c1 in xrange(len(extractLine)):
                if count < len(extractLine):
                    newSchedule.courseRecitation.update({extractLine[count]:extractLine[count+1]})
                    count = count + 2
            flag = False       
        else:
            newSchedule = Schedule()
            newSchedule.className = extractLine[0]
            count = 1
            for c1 in xrange(len(extractLine)):
                if count < len(extractLine):
                    newSchedule.courseRecitation.update({extractLine[count]:extractLine[count+1]})
                    count = count + 2
            ScheduleArray.append(newSchedule)
            
    if sequence == 2:
        extractLine = splitClassSchedule[cl].split(",")
        for x in xrange(len(ScheduleArray)):
            if ScheduleArray[x].className == extractLine[0]:
                flag = True
                currentObject = ScheduleArray[x]
                break
        if flag==True:
            newSchedule = currentObject
            for c1 in xrange(1,len(extractLine)):
                if c1 ==1:
                    newSchedule.courseDetailsNumber = extractLine[c1]
                if c1==2:
                    newSchedule.courseDetailsAttend = extractLine[c1]
            flag = False       
        else:
            newSchedule = Schedule()
            newSchedule.className = extractLine[0]
            for c1 in xrange(1,len(extractLine)):
                if c1 ==1:
                    newSchedule.courseDetailsNumber = extractLine[c1]
                if c1==2:
                    newSchedule.courseDetailsAttend = extractLine[c1]
            ScheduleArray.append(newSchedule)
    
    if sequence == 3:
        extractLine = splitClassSchedule[cl].split(",")
        for x in xrange(len(ScheduleArray)):
            if ScheduleArray[x].className == extractLine[0]:
                flag = True
                currentObject = ScheduleArray[x]
                break
        if flag==True:
            newSchedule = currentObject
            for c1 in xrange(1,len(extractLine)):
                if extractLine[c1] not in newSchedule.courseRequirement:
                    newSchedule.courseRequirement.append(extractLine[c1])
            flag = False       
        else:
            newSchedule = Schedule()
            newSchedule.className = extractLine[0]
            for c1 in xrange(1,len(extractLine)):
                    newSchedule.courseRequirement.append(extractLine[c1])
            ScheduleArray.append(newSchedule)
     
    if sequence == 4:
        extractLine = splitClassSchedule[cl].split(",")
        for x in xrange(len(TAArray)):
            if TAArray[x].TAName == extractLine[0]:
                flag = True
                currentObject = TAArray[x]
                break
        if flag==True:
            newTA = currentObject
            for c1 in xrange(1,len(extractLine),2):
                    newTA.TAResponsibilities.update({extractLine[c1]:extractLine[c1+1]})
            flag = False       
        else:
            newTA = TA()
            newTA.TAName = extractLine[0]
            for c1 in xrange(1,len(extractLine),2):
                    newTA.TAResponsibilities.update({extractLine[c1]:extractLine[c1+1]})
            TAArray.append(newTA)
    
    if sequence == 5:
        extractLine = splitClassSchedule[cl].split(",")
        for x in xrange(len(TAArray)):
            if TAArray[x].TAName == extractLine[0]:
                flag = True
                currentObject = TAArray[x]
                break
        if flag==True:
            newTA = currentObject
            for c1 in xrange(1,len(extractLine)):
                if extractLine[c1] not in newTA.TASkills:
                    newTA.TASkills.append(extractLine[c1])
            flag = False       
        else:
            newTA = TA()
            newTA.TAName = extractLine[0]
            for c1 in xrange(1,len(extractLine)):
                    newTA.TASkills.append(extractLine[c1])
            TAArray.append(newTA)

file_Course_Time.close()

def checkClassCollision(sel,sel2):
    global checkFlag
    if sel.className != sel2.className:
        for x in sel.day.keys():
            if x in sel2.day.keys():
                if checkTimingClash(sel.day[x].strip(),sel2.day[x].strip()):
                    checkFlag.append(False)

def main():

    """BackTracking"""
    count = 0
    
    print "===========================================================================" 
    print "These are the list of classes who do not need any TAs"
    print "===========================================================================" 
    
    for sel in ScheduleArray:
        taRequiredNumberCheck(sel)
    
    for sel in ScheduleArray:
        if sel.taRequiredNumber == 0:
            print sel.className, "TA Not Required"
            sel.assignTA.append("TA Not Required")  
            
        
    for sel in ScheduleArray:
        if sel.taRequiredNumber != 0:
            NewScheduleArray.append(sel)
    
    print "===========================================================================" 
    print "These are the list of classes who do not have skills for any of the classes"        
    print "==========================================================================="
        
    for sel in NewScheduleArray:
        flagg = False
        for ta in TAArray:
            if not set(ta.TASkills).isdisjoint(sel.courseRequirement):
                flagg = True
        if flagg == False:
            print sel.className, "No TA has required skills for this class"
            NewScheduleArray.remove(sel)   
    
    
    print "==========================================================================="
    print "These show the list of classes and their TAs with the contribution"
    print "===========================================================================" 
    
    for sel in NewScheduleArray:
        global checkFlag
        for ta in TAArray:
            checkFlag = []
            checkTAResponsibilitiesClashWithClass(sel,ta)
            checkTASkillSetCommon(sel,ta)
            checkTAResponsibilitiesClashWithCourseRecitation(sel,ta)
            for key in ta.contriList.keys():
                checkClassCollision(sel,key)
            if False not in checkFlag:
                sel.domainTA.append(ta)
    
    check = checkTAClassesBalance()
    
    #NewScheduleArray.sort(key=lambda sel: sel.taRequiredNumber)
    
               
    performForwardChecking(NewScheduleArray,check)
    
    print "==========================================================================="
    print "List of class with the TAs"
    print "===========================================================================" 
                    
    for x in NewScheduleArray:
        print x.className ,  "----> ",
        for y in x.assignTA:
            print y.TAName,
        print ""
            
    print "==========================================================================="
    print "List of classes assigned with the TAs contribution for whom none of the TAs skills were matching"
    print "===========================================================================" 
    NoTAsSkillMatchClass = []
    for sel in ScheduleArray:
        flagg = False
        for ta in TAArray:
            if not set(ta.TASkills).isdisjoint(sel.courseRequirement):
                flagg = True
        if flagg == False and sel.taRequiredNumber != 0:
            NoTAsSkillMatchClass.append(sel) 
            
    for sel in NoTAsSkillMatchClass:
        for ta in TAArray:
            if ta.contribution !=0 and sel.taRequiredNumber!=0:
                assignTA(sel,ta)
    
    print "==========================================================================="
    print "List of class with the TAs for whom none of the TAs skills were matching"
    print "===========================================================================" 
    
    for x in NoTAsSkillMatchClass: 
        print x.className ,  "----> ",
        for y in x.assignTA:
            print y.TAName,
        print ""
                    
def checkTAClassesBalance():
    sumTA = 0
    sumClass = 0
    for sel in NewScheduleArray:
        taRequiredNumberCheck(sel)
    for sel in NewScheduleArray:
        sumClass = sumClass + sel.taRequiredNumber
    for ta in TAArray:
        sumTA = sumTA + ta.contribution
    return sumClass - sumTA



def checkSuccess():
    flag = False
    for sel in NewScheduleArray:
        if len(sel.assignTA)==0:
            flag = True
    if flag == False:
        return True
    else:
        return False
            
def performForwardChecking(NewScheduleArray,check):
    global checkFlag
    flag = False
    if checkSuccess():
        return "Success"
    unassignedClass = pickUnassignedClass(NewScheduleArray)
    #print unassignedClass.className
    taRequiredNumberCheck(unassignedClass)
    for ta in TAArray:
        if ta in unassignedClass.domainTA:
            assignTA(unassignedClass,ta)
            for sel in NewScheduleArray:
                if sel.className != unassignedClass.className:
                    sum = 0
                    for x in sel.domainTA:
                        sum = sum + x.contribution
                    if sum == 0 and not checkSuccess():
                        unassignedClass.closed = False
                        taRequiredNumberCheck(unassignedClass)
                        for ta in unassignedClass.assignTA:
                            ta.contribution = ta.contriList[unassignedClass]
                        del unassignedClass.assignTA[:]
                    elif unassignedClass.taRequiredNumber == 0:
                        unassignedClass.closed = True
                        keyword = performForwardChecking(NewScheduleArray,check)
                        if keyword.strip() == "Success":
                            return "Success"
                        if keyword.strip() == "Failed" and check > 0:
                            return "Failed"
                        unassignedClass.closed = False
                        taRequiredNumberCheck(unassignedClass)
                        for ta in unassignedClass.assignTA:
                            ta.contribution = ta.contriList[unassignedClass]
                        del unassignedClass.assignTA[:]
    unassignedClass.closed = False
    taRequiredNumberCheck(unassignedClass)
    for ta in unassignedClass.assignTA:
        ta.contribution = ta.contriList[unassignedClass]
    del unassignedClass.assignTA[:]
    return "Failed"


def taRequiredNumberCheck(unassignedClass):
    if float(unassignedClass.courseDetailsNumber) >=25 and float(unassignedClass.courseDetailsNumber) <40:
        unassignedClass.taRequiredNumber = 0.5
    if float(unassignedClass.courseDetailsNumber) >=40 and float(unassignedClass.courseDetailsNumber) <=60:
        unassignedClass.taRequiredNumber = 1.5
    if float(unassignedClass.courseDetailsNumber) >=60:
        unassignedClass.taRequiredNumber = 2  

def assignTA(unassignedClass,ta):
    if float(unassignedClass.taRequiredNumber) ==2:
        if float(ta.contribution) == 0.5:
            unassignedClass.taRequiredNumber = unassignedClass.taRequiredNumber - 0.5
            unassignedClass.assignTA.append(ta)
            ta.contriList.update({unassignedClass:0.5})
            print unassignedClass.className, ta.TAName, ta.contribution
            ta.contribution = 0
        if float(ta.contribution) == 1:
            unassignedClass.taRequiredNumber = unassignedClass.taRequiredNumber - 1
            unassignedClass.assignTA.append(ta)
            ta.contriList.update({unassignedClass:1})
            print unassignedClass.className, ta.TAName, ta.contribution
            ta.contribution = 0
    elif float(unassignedClass.taRequiredNumber) == 1.5:
        if float(ta.contribution) == 0.5:
            unassignedClass.taRequiredNumber = unassignedClass.taRequiredNumber - 0.5
            unassignedClass.assignTA.append(ta)
            ta.contriList.update({unassignedClass:0.5})
            print unassignedClass.className, ta.TAName, ta.contribution
            ta.contribution = 0
        if float(ta.contribution) == 1:
            unassignedClass.taRequiredNumber = unassignedClass.taRequiredNumber - 1
            unassignedClass.assignTA.append(ta)
            ta.contriList.update({unassignedClass:1})
            print unassignedClass.className, ta.TAName, ta.contribution
            ta.contribution = 0
    elif float(unassignedClass.taRequiredNumber) == 1:
        if float(ta.contribution) == 0.5:
            unassignedClass.taRequiredNumber = unassignedClass.taRequiredNumber - 0.5
            unassignedClass.assignTA.append(ta)
            ta.contriList.update({unassignedClass:0.5})
            print unassignedClass.className, ta.TAName, ta.contribution
            ta.contribution = 0
        if float(ta.contribution) == 1:
            unassignedClass.taRequiredNumber = unassignedClass.taRequiredNumber - 1
            unassignedClass.assignTA.append(ta)
            ta.contriList.update({unassignedClass:1})
            print unassignedClass.className, ta.TAName, ta.contribution
            ta.contribution = 0
    elif float(unassignedClass.taRequiredNumber) == 0.5:
        if float(ta.contribution) == 0.5:
            unassignedClass.taRequiredNumber = unassignedClass.taRequiredNumber - 0.5
            unassignedClass.assignTA.append(ta)
            ta.contriList.update({unassignedClass:0.5})
            print unassignedClass.className, ta.TAName, ta.contribution
            ta.contribution = 0
        if float(ta.contribution) == 1:
            unassignedClass.taRequiredNumber = unassignedClass.taRequiredNumber - 0.5
            unassignedClass.assignTA.append(ta)
            ta.contriList.update({unassignedClass:0.5})
            ta.contribution = 0.5
            print unassignedClass.className, ta.TAName, ta.contribution
    elif float(ta.contribution) > 0:
        unassignedClass.taRequiredNumber = unassignedClass.taRequiredNumber - 0.5
        unassignedClass.assignTA.append(ta)
        ta.contriList.update({unassignedClass:0.5})
        print unassignedClass.className, ta.TAName, 0.5
        ta.contribution = ta.contribution - 0.5
        
        

def pickUnassignedClass(NewScheduleArray):
    for sel in NewScheduleArray:
        if sel.taRequiredNumber > 0 and sel.closed == False:
            return sel
    
def checkTAResponsibilitiesClashWithClass(unassignedClass,ta):
    if unassignedClass.courseDetailsAttend.strip() == "yes":
        for k in ta.TAResponsibilities.keys():
            if k in unassignedClass.day:
                if checkTimingClash(ta.TAResponsibilities[k].strip(),unassignedClass.day[k].strip()):
                    checkFlag.append(False)
                else:
                    checkFlag.append(True)
            else:
                checkFlag.append(True)
    else:
        checkFlag.append(True)
        

def checkTASkillSetCommon(unassignedClass,ta):
    if not set(ta.TASkills).isdisjoint(unassignedClass.courseRequirement):
        checkFlag.append(True)
    else:
        checkFlag.append(False)
    

def checkTAResponsibilitiesClashWithCourseRecitation(unassignedClass,ta):
    if unassignedClass.courseRecitation != None:
        for k in ta.TAResponsibilities.keys():
            if k in unassignedClass.courseRecitation:
                if checkTimingClash(ta.TAResponsibilities[k].strip(),unassignedClass.courseRecitation[k].strip()):
                    checkFlag.append(False)
                else:
                    checkFlag.append(True)
            else:
                checkFlag.append(True)
    else:
        checkFlag.append(True)
        
def checkTimingClash(Time1 , Time2):
    booleanFlag = False
    x1 = Time1.split(" ")
    x2 = x1[0].split(":")
    
    y1 = Time2.split(" ")
    y2 = y1[0].split(":")
    
    
    if x1[1]=="AM" and int(x2[0]) == 12:
        hr1 = 0
    elif x1[1]=="PM" and int(x2[0]) <= 12:
        hr1 = (12 + int(x2[0]))*60
    else:
        hr1 = int(x2[0])*60
    min1 = int(x2[1])
    TotalMinStart1 = hr1 + min1
    TotalMinEnd1 = TotalMinStart1 + DurTA
    
    if y1[1]=="AM" and int(y2[0]) == 12:
        hr2 = 0
    elif y1[1]=="PM" and int(y2[0]) <= 12:
        hr2 = (12 + int(y2[0]))*60
    else:
        hr2 = int(y2[0])*60
    min2 = int(y2[1])
    TotalMinStart2 = hr2 + min2
    TotalMinEnd2 = TotalMinStart2 + DurClass
    
    if TotalMinStart2 > TotalMinEnd1 and TotalMinStart2 < TotalMinStart1:
        booleanFlag = True
        return booleanFlag
    if TotalMinEnd1 > TotalMinStart2 and TotalMinEnd1 < TotalMinEnd2:
        booleanFlag = True
        return booleanFlag 
    if TotalMinStart1 == TotalMinStart2 or TotalMinEnd1 == TotalMinEnd2:
        booleanFlag = True
        return booleanFlag
    
    return booleanFlag 
   
main()