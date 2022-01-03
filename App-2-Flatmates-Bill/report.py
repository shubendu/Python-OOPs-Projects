import webbrowser
import os

from fpdf import FPDF


class PdfReport:
    """
    Generate PDF containing information about bill
    """

    def __init__(self,filename):
        self.filename = filename

    def generate(self,flatemate1,flatemate2, bill):

        flatemate1_pay = str(round(flatemate1.pays(bill=bill, flatemate2=flatemate2), 2))
        flatemate2_pay = str(round(flatemate2.pays(bill=bill, flatemate2=flatemate1), 2))
        pdf = FPDF(unit="pt")
        pdf.add_page()

        #Add icon
        pdf.image("files/house.png", w=30, h=30)

        #Insert title
        pdf.set_font(family="Times", size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatemates Bill", border=0, align='C', ln=1)

        #Insert Period label and value
        pdf.set_font(family="Times", size=14)
        pdf.cell(w=100,h=40, txt="Period:", border = 0)
        pdf.cell(w=150,h=40, txt=bill.period, border = 0,ln=1)

        # Insert name and due amount name of the first flatemate
        pdf.cell(w=100, h=25, txt=flatemate1.names, border=0)
        pdf.cell(w=150, h=25, txt=flatemate1_pay, border=0,ln=1)

        # Insert name and due amount name of the first flatemate
        pdf.cell(w=100, h=25, txt=flatemate2.names, border=0)
        pdf.cell(w=150, h=25, txt=flatemate2_pay, border=0, ln=1)

        os.chdir("files")
        pdf.output(self.filename)
        #open file
        webbrowser.open(self.filename)