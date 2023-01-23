#
#
#
def GetEmpName():
    empname = input("Enter employee name: ")
    return empname
#for the next three functions, you need to convert the input to a float, e.g., varname = float(input('descripion of input:  '))
#write the GetHoursWorked function
def GetHoursWorked():
    hoursWorked = float(input("Enter hours worked: "))
    return hoursWorked
#write the GetHourlyRate function
def GetHourlyRate():
    hourlyrate = float(input("Enter hourly rate: "))
    return hourlyrate
# write the GetTaxRate function
def GetTaxRate():
    taxRate = float(input("Enter Tax Rate: "))
    return taxRate



def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(empname, hours, hourlyrate,grosspay, taxrate, incometax, netpay):
    print("Name:  ", empname) 
    print("Hours Worked: ", f"{hours:,.2f}")
    # write the lines of code to display hourlyrate, grosspay, taxrate, incometax and netpay with correct formatting
    # taxrate needs to be formatted as percentage
    print("Hourly Rate: ", f"{hourlyrate:,.2f}")
    print("Gross Pay: ", f"{grosspay:,.2f}")
    print("Tax Rate: ", f"{taxrate:,%.2f}")
    print("Income Tax: ", f"{incometax:,.2f}")
    print("Net Pay: ", f"{netpay:,.2f}")


    print()
def PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay):    
    print()
    print(f"Total Number Of Employees: {TotEmployees}")
    print(f"Total Hours Worked: {TotHours:,.2f}")
    # write the code to print  TotGrossPay, TotTax, and TotNetpay with 2 decimal places
    print(f"Total gross pay: {TotGrossPay:,.2f}")
    print(f"Total tax: {TotTax:,.2f}")
    print(f"Total Net Pay: {TotNetPay:,.2f}")

if __name__ == "__main__":
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break
        # write the code to assign to hours the return value from GetHoursWorked
        hoursWorked = GetHoursWorked()
        # write the code to assign to hourlyrate the return value from GetHourlyRate
        hourlyrate = GetHourlyRate()
        # write the code to assign to taxrate the return value from GetTaxRate
        taxRate = GetTaxRate()
        grosspay, incometax, netpay = CalcTaxAndNetPay(hoursWorked, hourlyrate, taxRate)
        print(empname, hoursWorked, hourlyrate, taxRate, incometax, netpay)
        TotEmployees += 1
        TotHours += hoursWorked
        # write the code to increment the other total variables with the appropriate values
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay


    PrintTotals (TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay)
