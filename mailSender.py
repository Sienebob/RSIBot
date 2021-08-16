import yagmail

try:
    #initializing the server connection
    yag = yagmail.SMTP(user='your@gmail.com', password='pass')
    #sending the email
    yag.send(to='your@gmail.com', subject='Testing Yagmail', contents='Hurray, it worked!')
    print("Email sent successfully")
except:
    print("Error, email was not sent")