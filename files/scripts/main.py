import os.path
import webbrowser
from fpdf import FPDF
from Bill import Bill
from Flatmate import Flatmate


# inputs
from files.scripts.PdfReport import PdfReport

bill_amount = float(input("Hey User Enter bill amount: "))
period = input("Enter a period: ")
name1 = input("Enter your name: ")
name1_days = int(input(f"Enter how many days {name1} was in house: "))
name2 = input("Enter you roommates Name: ")
name2_days = int(input(f"Enter how many days {name2} was in house: "))

the_bill = Bill(amount=bill_amount, period=period)

firstPerson = Flatmate(name1, name1_days)
secondPerson = Flatmate(name2, name2_days)

print(f"{firstPerson.name} pays: ", firstPerson.pays(the_bill, secondPerson))
print(f"{secondPerson.name} pays: ", secondPerson.pays(the_bill, firstPerson))

pdf_period = PdfReport(filename=f"report{the_bill.period}.pdf")
pdf_period.generate(flatmate1=firstPerson, flatmate2=secondPerson, bill=the_bill)
