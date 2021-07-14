
def calculateAge(currentyear,yearofbirth):
    age=currentyear -yearofbirth
    return age
    
def userInputDates():
 yearofbirth= int (input ( "yearofbirth"))
 currentyear=int (input("currentyear"))
 return calculateAge (currentyear,yearofbirth)
print (userInputDates()) 