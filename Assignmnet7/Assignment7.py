#overtime py
#calculates pay and overtime for a week
#Assignment7

def getWage():
    wage=float(input("Enter your hourly wage: "))
    return wage

def getHours():
    hours=float(input("Enter your hours: "))
    return hours

def calculatePay():
    rate=getWage()
    hrs=getHours()
    regpay=0
    pay=0
    OT=0
    if hrs > 44:
        #pay=rate * (44 + ((hrs-44)*1.5))
        regpay=rate * hrs
        OT=rate *(hrs-44)*1.5
        pay=regpay+OT
    else:
        regpay=rate * hrs
        pay=regpay
    display(regpay, OT, pay)

def display(reg, ot, pay):
    print("Your regular pay is", reg)
    print("Your overtime pay is",ot)
    print("Your total pay is", pay)

def main():
    calculatePay()

main()
