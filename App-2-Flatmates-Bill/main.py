from flat import Bill, Flatmate
from report import PdfReport

amount = float(input("Hey user, enter the bill amount: "))
period = input("What is the bill period? E.g. December 2020: ")

name1 = input("What is your name? ")
days_in_house1 = int(input(f"How many days did {name1} stay in the house during the bill period? "))

name2 = input("What is the name of other flatmate? ")
days_in_house2 = int(input(f"How many days did {name2} stay in the house during the bill period? "))

the_bill = Bill(amount=amount, period= period)
flatmate1 = Flatmate(names=name1, days_in_house=days_in_house1)
flatmate2 = Flatmate(names=name2, days_in_house=days_in_house2)

print(f"{flatmate1.names} pays: ",flatmate1.pays(bill=the_bill, flatemate2=flatmate2))
print(f"f{flatmate2.names} pays: ",flatmate2.pays(bill=the_bill, flatemate2=flatmate1))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatemate1=flatmate1, flatemate2= flatmate2, bill=the_bill)



