from fpdf import FPDF


class Bill:
    """
    object that contains data about a bill:
     1. Total amount
     2. perood
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    object that represents a flatmate that pays a bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    """
    creates a PDF class that contains a data about
    the flatmates such as their names and how much
    they each have to pay
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format="A4")
        pdf.add_page()

        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))
        # Add some info
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=1, align="C", ln=1)
        # Insert Period - value
        pdf.cell(w=100, h=40, txt="Period:", border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)
        # Insert First Flatmate
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=150, h=40, txt=flatmate1_pay, border=1, ln=1)
        # Insert Second Flatmate
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=1)
        pdf.cell(w=150, h=40, txt=flatmate2_pay, border=1, ln=1)

        pdf.output(self.filename)


"TEST"
the_bill = Bill(amount=120, period="March 2021")
john = Flatmate("John", 20)
merry = Flatmate("merry", 25)

print("John pays: ", john.pays(the_bill, merry))
print("merry pays: ", merry.pays(the_bill, john))

pdf_period = PdfReport(filename="report.pdf")
pdf_period.generate(flatmate1=john, flatmate2=merry, bill=the_bill)
