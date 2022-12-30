import yagmail
import os
import pandas


sender = 'mmmm@gmail.com'

subject = 'This is the subject'

yag = yagmail.SMTP(user=sender, password=os.getenv("PASSWORD"))
# First select Tools/Secrets; Give name to the key, then go to your gmail and apply apps password
# Uses getenv to prevent the vialization of password from other users.

df = pandas.read_csv('contacts.csv')

for index, row in df.iterrows():
  receiver = row['email']
  content = [f"""Hi, {row['name']},
You have to pay {row['amount']}""", 'text.txt']
  yag.send(to=receiver, subject=subject, contents=content)
  print('Email is sent')
