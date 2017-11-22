text = "This is %s formatted string" %("replacement")
print(text)

text = "The %%s format string is not as %s, but still very %s." %("robust", "useful")
print(text)


import datetime
today = datetime.date.today()
text = '{today.day}/{today.month}/{today.year}'.format(today=today)
print(text)
print(today)
