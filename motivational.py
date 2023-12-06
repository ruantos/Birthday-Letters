import smtplib
import random as rd
import datetime as dt

email = ""
password = ""

def check_date():
    date = dt.datetime.now()
    weekday = date.weekday()
    if weekday == 2:
        message = get_quote()
        send_email(message)

def get_quote():
    with open("quotes.txt", mode="r") as file:
        quotes_list = file.readlines()
        quote = rd.choice(quotes_list)
    subject = "Subject:Happy Birthday, Anonymous\n\n"
    message = subject + quote
    return message
    
def send_email(message):
    global email, password
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=email, msg=message)
        connection.close()

check_date()
