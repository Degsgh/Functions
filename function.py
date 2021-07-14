#calculate incl price
def calculateinclprice(exclPrice, vatTax):
    inclPrice = exclPrice + (exclPrice* vatTax)
    return inclPrice
#User gives exclusive Tax rate
def userInputExclTaxRate():
    exclPrice = float(input("Enter exclPrice"))
    vatTax = float(input("Enter tax rate"))
    return calculateinclprice(exclPrice,vatTax)


print(userInputExclTaxRate())
