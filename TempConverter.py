validCheck = True

while validCheck == True:
    temp = input("Insert a temperature number : ")
    try:
        temp = float(temp)
        validCheck = False
    except:
        print ("Enter a valid number")
        
validCheck2 = True
while validCheck2 == True:
    cOrF = input("Input C or F for Celsius/Fahrenheit : ")
    if cOrF == 'C' or cOrF == 'c':
        outputTemp = (temp * (9/5)) + 32
        print (str(f"{outputTemp:.2f}") + "F")
        validCheck2 = False
    elif cOrF == 'F' or cOrF == 'f':
        outputTemp = (temp - 32) * (5/9)
        print (str(f"{outputTemp:.2f}") + "C")
        validCheck2 = False
    else:
        print ("Invalid Character")



