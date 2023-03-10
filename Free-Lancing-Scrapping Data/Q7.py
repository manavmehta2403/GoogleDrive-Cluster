import pandas as pd
import openpyxl
import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 


def excel():
    #read the excel file as data frame
    df_April = pd.read_excel("Assign.xlsx","April")
    df_May = pd.read_excel("Assign.xlsx","May")
    df_Master_Sheet=pd.concat([df_April, df_May])
    #checks the output
    print(df_Master_Sheet)


    ### Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter('Q7.xlsx', engine='openpyxl')

    ### Convert the dataframe to an XlsxWriter Excel object.
    df_Master_Sheet.to_excel(writer, sheet_name='Master Sheet', index = False)
    ##
    ### Close the Pandas Excel writer and output the Excel file.
    writer.save()


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
