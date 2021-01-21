import datetime
currentDate=datetime.date.today()
strDueDate=input("Enter a due date in mm/dd/yy format: ")
dueDate=datetime.datetime.strptime(strDueDate,"%m/%d/%y").date()
daysLeft=dueDate-currentDate
print(f"You have {daysLeft} days left to finish")