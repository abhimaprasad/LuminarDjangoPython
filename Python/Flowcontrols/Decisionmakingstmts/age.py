month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
birth_year=int(input("enter the birth year"))
birth_month=int(input("enter the birth month"))
birth_date=int(input("enter the birth date"))
present_year=int(input("enter the year"))
present_month=int(input("enter the month"))
present_date=int(input("enter the date"))
if (birth_date > present_date):
      present_date = present_date + month[birth_month - 1]
      present_month = present_month - 1
if (birth_month > present_month):
      present_year = present_year - 1
      present_month = present_month + 12
final_date = present_date - birth_date
final_month = present_month - birth_month
final_year = present_year - birth_year
print(final_year)
print(final_month)
print(final_date)