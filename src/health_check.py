#!/usr/bin/env python3

import os
import emails
import shutil
import psutil
import socket

def check_cpu_health():
    usage = psutil.cpu_percent(1)
    print("CPU Usage: ", usage)
    return usage < 80

def check_disk_health():
    usage = shutil.disk_usage("/")
    print("disk usage: ", usage)
    return (usage.free/usage.total)*100 > 20

def check_main_mem_health():
    amount_free = psutil.virtual_memory()[1] >> 20
    return amount_free > 500

def check_localhost_resol():
    try:
        ip = socket.gethostbyname('localhost')
        print("IP: ", ip)
        if ip == "127.0.0.1":
            return True
        return False
    except socket.error:
        return False

def send_notification_email(error_email_subjs):
    sender = "automation@example.com"
    recipient = "{}@example.com".format(os.environ.get('USER'))
    body = r"Please check your system and resolve the issue as soon as possible."
    for email_sub in error_email_subjs:
        message = emails.generate_email(sender, recipient, email_sub, body, None)
        emails.send_email(message)

if __name__ == '__main__':
    error_email_subjs = []
    if not check_cpu_health():
        error_email_subjs.append("Error - CPU usage is over 80%")

    if not check_disk_health():
        error_email_subjs.append("Error - Available disk space is less than 20%")

    if not check_main_mem_health():
        error_email_subjs.append("Error - Available memory is less than 500MB")

    if not check_localhost_resol():
        error_email_subjs.append("Error - localhost cannot be resolved to 127.0.0.1")

    if len(error_email_subjs) > 0:
        send_notification_email(error_email_subjs)
