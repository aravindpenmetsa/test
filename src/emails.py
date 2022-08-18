#!/usr/bin/env python3

import os
import email.message
import mimetypes
import smtplib

def generate_email(sender, recipient, subject, body, attachment_path):
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    if attachment_path != None:
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split("/", 1)
        with open(attachment_path, mode="rb") as attachment_file:
            message.add_attachment(attachment_file.read(),
                                maintype=mime_type,
                                subtype=mime_subtype,
                                filename=os.path.basename(attachment_path)
                                )
    return message

def send_email(message):
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()
