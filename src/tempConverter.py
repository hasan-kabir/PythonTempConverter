temp = int(input("Enter the temperature :"))
method = input("Enter C or F to convert into Celcius or Ferhenheit :")


def convertIntoF(cTemp):
    return (cTemp * (9/5)) + 32
def convertIntoC(fTemp):
    return (fTemp -32) * 5/9


if method.upper() == "F":
    # convert into fahrenheit
    print("The ",temp, " ^C in Fahrenheit is :", convertIntoF(temp),"^F")
elif method.upper() == "C":
    # convert into celcius
    print("The ",temp, " ^F in Celcius is :", convertIntoC(temp),"^C")
else:
    print("Enter right conversion method as either C or F")
