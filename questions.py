# pallindrom
value = int(input("Enter a number: "))
rev_value = str(value)[::-1]
print(rev_value, value)
if str(value) == rev_value:
    print("The number is a pallindrom")
else:
    print("The number is not a pallindrom")
