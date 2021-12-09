import smtplib
from email.message import EmailMessage

msg=EmailMessage()
sender_email="durga.prasad@bitsinglass.com"
Password="imvdurga@13Prasad"
receiver_email="durga.vandharani@bitsinglass.com"

msg['From']=sender_email
msg['Subject']='Automation Test Report'
msg['To']=receiver_email
msg.set_content("Hi Team,\nPlease find the attached automation test report below.\n\n\n\n  Best Regards,\nDurga")

files = 'test_AllElementsPresent_09_December_2021_05_41PM.pdf'
for file in files:
    with open('C:/Users/dvandhar/PycharmProjects/LinkedInProject/test_LoginProcess/'+files, 'rb') as f:
        file_data = f.read()
        file_name = "test_AllElementsPresent_09_December_2021_05_41PM.pdf"

    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(sender_email, Password)
server.send_message(msg)
server.quit()
print("Email sent successfully")