
def CalculateGrade(AnswerKey):
    grade=0
    DenemeKey = input("Enter answers:")
    for x in range(10):
        if(AnswerKey[x]==DenemeKey[x]):
            grade=grade+10
    return grade

def GetNameInputs():
    Name = input("Enter name:")
    LastName = input("Enter last name:")
    tup=(Name,LastName)
    return tup
    

def AddDataToDic():
    Grades={}
    for x in range(5):
        TempNames=GetNameInputs()
        Grades[TempNames]=CalculateGrade(AnswerKey)
    return Grades

def FindAverage(Grades):
    Total=0
    for x in Grades.values():
     Total=Total+x
     Average=Total/5
    return Average
    
def AboveAverage(Grades):
    for key,value in Grades.items():
        
        if(value>FindAverage(Grades)):
            
            print("Name: ", key[1],", ",key[0][0],".", "Score: ", value)
         
def FindStudent(Grades):
    SearchName=input("Who are you searching for?")
    for key in Grades.keys():
        if SearchName in key:
            print(key[0]," ",key[1]," recieved ",Grades[key])



AnswerKey = input("Enter answer key:")
Grades=AddDataToDic()
print(Grades)
print("Average:",FindAverage(Grades))
AboveAverage(Grades)
FindStudent(Grades)




