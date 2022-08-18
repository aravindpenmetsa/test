#!/usr/bin/env python3

import os
import reports
import emails
import datetime

'''
    This script sends an email with a pdf containing the summary of
    uploaded catalog.
'''

def create_summary_for_report(data_dir_path):
    feedback = ""
    for data_file_name in os.listdir(data_dir_path):
        with open(os.path.join(data_dir_path, data_file_name)) as data_file:
            feedback += r"\n"
            for idx, line in enumerate(data_file):
                if idx == 0:
                    feedback += r"name:" + line.strip()
                elif idx == 1:
                    feedback += r"weight:" + line.strip()
                else:
                    break
                feedback += r"\n"
    return feedback

if __name__ == "__main__":
    data_path = '../data/supplier-data/descriptions/'
    pdf_report_path = '/home/aravind508/processed.pdf'
    # Read data and create summary
    summary_text = create_summary_for_report(data_path)
    # Generate PDF data from this.
    title = "Process updated on " + str(datetime.datetime.now())
    reports.genarate(pdf_report_path, title, summary_text)
    #Sending email
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    message = emails.generate_email(sender, receiver, subject, summary_text, pdf_report_path)
    emails.send(message)
