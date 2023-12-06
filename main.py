import smtplib

email = ""
password = ""

connection = smtplib.SMTP()
connection.starttls()
connection.login(user=email, password=password)
connection.sendmail(from_addr=email, to_addrs=to_email, msg="")
connection.close()