from datetime import date

today= date.today()

print(f"Today's date: {today.year}-{today.month:02d}-{today.day:02d}")

#02d gives the month as 08 instead of just 8.It's a format specifier
#: tells that we are about to specify a format