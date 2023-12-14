import pandas as pd
import random as rd
import datetime as dt
import smtplib
import os

date = dt.datetime.now()
MONTH = date.month
DAY = date.day
EMAIL = os.environ.get("email")
PASSWORD = os.environ.get("password")

info = pd.read_csv("birthdays.csv")

def check_date(df):
    global MONTH, DAY 
    for i in range(len(df)):
        if df.loc[i, "month"] == MONTH and df.loc[i, "day"] == DAY:
            return df.loc[i]
    return None

def send_email(person):
    global EMAIL, PASSWORD
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, 
                            to_addrs=person.loc["email"], 
                            msg=sort_letter(person.loc["name"]))

def sort_letter(name):
    num = rd.randint(1, 3)
    file_name = f"./letter_templates/letter_{num}.txt"
    with open(file_name, mode="r") as file:
        letter = file.read()
        letter = letter.replace("[NAME]", name)
    return letter
    

person = check_date(info)
if not person.empty:
    send_email(person)
