import os
import smtplib
import shutil
from pathlib import Path
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from datetime import datetime


# Read counter
def read_counter():
    # Read counter
    path = Path(__file__).parent / "counter.txt"
    f = open(path, 'r+')
    data = int(f.read())
    return data


# Read and Update counter
def read_and_update_counter():
    # Read counter
    path = Path(__file__).parent / "counter.txt"
    f = open(path, 'r+')
    data = int(f.read())
    # Update counter
    new_counter = str(data + 1)
    # Write new counter
    f.seek(0)
    f.write(new_counter)
    f.truncate()
    f.close()
    return new_counter


# Read current date
def read_date():
    return str(datetime.today().strftime('%Y-%m-%d'))


# Send mail
def sendmail(sender_email, sender_password, receivers_email, mail_subject, mail_body, attached_file_path, bcc_mail=''):
    # Mail content, format, encoding
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receivers_email
    message['Subject'] = Header(mail_subject, 'utf-8')
    if bcc_mail:
        message['Bcc'] = bcc_mail
    message.attach(MIMEText(mail_body))

    # Build the attachment
    attachment = MIMEBase('application', 'octet-stream')
    attachment.set_payload(open(attached_file_path, 'rb').read())
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attached_file_path))
    message.attach(attachment)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(message)
        print("Send email successfully!!!")
        server.close()
    except smtplib.SMTPException:
        print("Failed to send mail!!!")


# Delete folder and its content except last n number of dirs
def del_dir(num_of_dir, dir_name):
    basedir = Path(__file__).resolve().parent.parent
    dir_name = dir_name
    dir_path = os.path.join(basedir, dir_name)
    dir_list = [os.path.join(dir_path, f) for f in sorted(os.listdir(dir_path))]
    dir_list = dir_list[:len(dir_list) - num_of_dir]
    for folder in dir_list:
        try:
            shutil.rmtree(folder)
        except OSError as e:
            print("Error: %s : %s" % (folder, e.strerror))


# Delete file except last n number of files
def del_file(num_of_file, dir_name):
    basedir = Path(__file__).resolve().parent.parent
    dir_name = dir_name
    dir_path = os.path.join(basedir, dir_name)
    file_list = [os.path.join(dir_path, f) for f in sorted(os.listdir(dir_path))]
    file_list = file_list[:len(file_list) - num_of_file]
    for file in file_list:
        os.remove(file)


# Keep number of directories and files
def keep_reports(number, dir_name, file_dir):
    del_dir(number, dir_name)
    del_file(number, file_dir)


# Send email
def send_email(sender, password, receivers):
    bcc_mail = ''
    email_subject = 'Test Report'
    email_body = "Dear Sir, Please check this report."
    attached_file_path = Path(__file__).parent / f"../ReportHtml/report_{read_date()}_{read_counter()}.html"
    sendmail(sender, password, receivers, email_subject, email_body, attached_file_path, bcc_mail)
