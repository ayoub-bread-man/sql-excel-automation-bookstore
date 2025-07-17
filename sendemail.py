import smtplib
from email.message import EmailMessage





def send_mail(year , month , file_name , file_path  ): 
    msg = EmailMessage()
    msg['Subject'] = f"Monthly Report - {year}-{month:02}"
    msg['From'] = "your_email@gmail.com"
    msg['To'] = "reciver@example.com"
    msg.set_content("Hi, attached is the sales report for this month.")

    # Attach the Excel file
    with open(file_path, 'rb') as f:
        file_data = f.read()
        msg.add_attachment(file_data, maintype='application', subtype='vnd.openxmlformats-officedocument.spreadsheetml.sheet', filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login("your_email@gmail.com", "your_app_password")
        smtp.send_message(msg)

    print(" Email sent successfully.")
