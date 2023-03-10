def email():

    sender = "manavpythonwork@gmail.com"

    reciever = "pramod.nimesh@teleperformancedibs.com"

    sub = "Work"

    message = "Hey! PFA."

   

    mail = MIMEMultipart()

    mail["From"] = sender

    mail["To"] = reciever

    mail["Subject"] = sub

    mail.attach(MIMEText(message,'plain'))

 

    part = MIMEBase('application', "octet-stream")

    part.set_payload(open("Q7.xlsx", "rb").read())

    encoders.encode_base64(part)

    part.add_header('Content-Disposition', 'attachment; filename="Q7.xlsx"')

    mail.attach(part)

 

    msg = mail.as_string()

   

    server = smtplib.SMTP("smtp.gmail.com",587)

    server.starttls()

    server.login(sender,"Bigboyzbang24")

    server.sendmail(sender,reciever,msg)

    server.quit()

 

 

def main():

    excel()

    email()

    close = input("Press any key to exit")

if __name__ == '__main__':

    main()