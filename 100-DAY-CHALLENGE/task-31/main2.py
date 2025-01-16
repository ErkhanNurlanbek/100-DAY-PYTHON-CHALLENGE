import datetime as dt
import smtplib
import random
#my_email = 'erkhan208@gmail.com'
#password = 'password(Lesson 245)'

#connection = smtplib.SMTP('smtp.gmail.com')
#connection.starttls()
#connection.login(user=my_email, password=password)
#connection.sendmail(from_addr=my_email, to_addrs='emailtosendemailto@yahoo.com', msg='Hello')
#connection.close()
#
# now = dt.datetime.now()
# dateofbirth = dt.datetime(year= , month=, day=)
# year = now.year
# day = now.day
# month = now.month
# print(month)
# print(year)
# print(type(now))
MY_EMAIL = 'randomemail@gmail.com'
MY_PASSWORD = 'qwertyuiop'

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 3:
    with open('quotes.txt') as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.sendmail(from_addr=MY_EMAIL, to_addrs='anotherrandomemail@gmail.com', msg=f'Subject:Thursday Motivation\n\n{quote}')