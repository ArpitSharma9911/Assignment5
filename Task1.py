#Task1 : Create a Dictionary of Student Marks
report_card={'Ankit': 75, 'Ankur':80, "Bhaskar": 70, "Bhimar": 85, "Sahitya":60 }
print(report_card)
name=input("Enter your name: ")
if name in report_card.keys():
    print("{}'s marks are: {}".format(name,report_card[name]))
    print(f"{name}'s marks are: {report_card[name]}")
else:
    print("{} is not present in report card ".format(name))
